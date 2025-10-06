# constraints/constraints.py
"""
Constraint validation functions for train scheduling.
Each function returns (bool, reason) for clarity and explainability.
"""

def check_fitness(train):
    """Check if train has exceeded its fitness threshold."""
    if train["mileage"] >= train["fitness_due_at"]:
        return False, "Fitness overdue"
    return True, "Fitness OK"

def check_cleaning(train):
    """Check if train needs cleaning before scheduling."""
    if train.get("needs_cleaning", False):
        return False, "Needs cleaning"
    return True, "Cleaning OK"

def check_job_card(train):
    """Check if job card is ready for this train."""
    if not train.get("job_card_ready", False):
        return False, "Job card not ready"
    return True, "Job card ready"

def check_depot_capacity(depot, assigned_count):
    """Check if depot has available slots left."""
    if assigned_count >= depot["capacity"]:
        return False, "Depot full"
    return True, "Depot has capacity"

def validate_train_assignment(train, depot, assigned_count):
    """
    Run all constraints and return (bool, reasons).
    Reasons is a list of strings explaining why assignment may fail.
    """
    reasons = []

    for check in [check_fitness, check_cleaning, check_job_card]:
        valid, reason = check(train)
        if not valid:
            reasons.append(reason)

    # Depot capacity check
    valid, reason = check_depot_capacity(depot, assigned_count)
    if not valid:
        reasons.append(reason)

    return (len(reasons) == 0, reasons)
