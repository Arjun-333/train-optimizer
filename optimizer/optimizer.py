# optimizer/optimizer.py
from typing import List, Dict, Optional
from datetime import timedelta
import time
from .models import Train, Depot, JobCard
from . import constraints
import copy

def greedy_optimizer(
    trains: List[Train],
    depots: List[Depot],
    spare_parts: Optional[Dict[str,int]] = None,
    time_step_minutes: int = 15,
) -> Dict:
    """
    Simple greedy optimizer prototype.
    Returns a dict: { schedule: [...], reasons: {...}, metrics: {...} }
    """
    t0 = time.perf_counter()
    spare = copy.deepcopy(spare_parts or {})
    occupancy: Dict[str, List[tuple]] = {d.id: [] for d in depots}  # depot_id -> list of (bay, start, end, train_id)
    assignments = []
    reasons: Dict[str, List[str]] = {}

    # sort trains: highest priority first, then earliest start
    sorted_trains = sorted(trains, key=lambda t: (-t.priority, t.earliest))

    for train in sorted_trains:
        reasons.setdefault(train.id, [])
        scheduled = False

        # For prototype: consider only first job_card if present, otherwise cleaning-only
        job_card = train.job_cards[0] if train.job_cards else None
        duration_min = job_card.duration_min if job_card else train.cleaning_min
        if duration_min <= 0:
            reasons[train.id].append("NO_WORK_TO_SCHEDULE")
            continue
        duration = timedelta(minutes=duration_min)
        step = timedelta(minutes=time_step_minutes)

        # Try to place
        for depot in depots:
            if scheduled:
                break
            for bay in range(1, depot.capacity + 1):
                start_time = train.earliest
                while start_time + duration <= train.latest:
                    end_time = start_time + duration
                    ok, code = constraints.can_assign(train, depot, start_time, end_time, bay, spare, occupancy, job_card)
                    if ok:
                        # reserve parts if needed
                        if job_card and job_card.required_parts:
                            constraints.reserve_parts(spare, job_card.required_parts)

                        occupancy[depot.id].append((bay, start_time, end_time, train.id))
                        assignments.append({
                            "train_id": train.id,
                            "train_name": train.name,
                            "depot_id": depot.id,
                            "depot_name": depot.name,
                            "job_id": job_card.id if job_card else "CLEAN",
                            "start": start_time.isoformat(),
                            "end": end_time.isoformat(),
                            "bay": bay,
                        })
                        reasons[train.id].append(f"ASSIGNED to {depot.name} bay {bay} start {start_time.isoformat()}")
                        scheduled = True
                        break
                    else:
                        # record a failing reason once (optional: record multiple attempts)
                        # We push the most frequent reason later; for simplicity append code
                        # but only if no prior identical code appended (avoid repetition).
                        if code not in reasons[train.id]:
                            reasons[train.id].append(code)
                    start_time += step
                if scheduled:
                    break

        if not scheduled:
            reasons[train.id].append("UNSCHEDULED")

    runtime_ms = int((time.perf_counter() - t0) * 1000)
    return {
        "schedule": assignments,
        "reasons": reasons,
        "metrics": {
            "runtime_ms": runtime_ms,
            "trains_count": len(trains),
            "scheduled_count": len(assignments),
        }
    }
