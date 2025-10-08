# data/sample_data.py
from datetime import datetime
from optimizer.models import Train, Depot, JobCard

# Simple sample dataset for quick Week-1 tests
trains = [
    Train(
        id="T1",
        name="Train A",
        earliest=datetime(2025,10,6,6,0),
        latest=datetime(2025,10,6,12,0),
        priority=9.0,
        job_cards=[JobCard("JC1", duration_min=180, required_parts={"pad":2})],
        cleaning_min=20
    ),
    Train(
        id="T2",
        name="Train B",
        earliest=datetime(2025,10,6,7,0),
        latest=datetime(2025,10,6,18,0),
        priority=7.5,
        job_cards=[JobCard("JC2", duration_min=120, required_parts={"filter":1})],
        cleaning_min=15
    ),
    Train(
        id="T3",
        name="Train C",
        earliest=datetime(2025,10,6,10,0),
        latest=datetime(2025,10,6,22,0),
        priority=6.0,
        job_cards=[],
        cleaning_min=30
    ),
    Train(
        id="T4",
        name="Train D",
        earliest=datetime(2025,10,6,6,0),
        latest=datetime(2025,10,6,22,0),
        priority=8.0,
        job_cards=[JobCard("JC3", duration_min=240, required_parts={"pad":1,"filter":1})],
        cleaning_min=0
    ),
]

depots = [
    Depot(id="D1", name="Depot East", capacity=2, working_start_hour=6, working_end_hour=22),
    Depot(id="D2", name="Depot West", capacity=1, working_start_hour=6, working_end_hour=20),
]

spare_parts = {
    "pad": 3,
    "filter": 2
}
