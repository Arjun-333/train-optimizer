# constraints/constraints.py

def check_fitness(train):
    """Check if train has exceeded its fitness threshold."""
    return train["mileage"] < train["fitness_due_at"]

def check_cleaning(train):
    """Check if train needs cleaning before scheduling."""
    return not train.get("needs_cleaning", False)

def check_job_card(train):
    """Check if job card is ready for this train."""
    return train.get("job_card_ready", False)

def check_depot_capacity(depot, assigned_count):
    """Check if depot has available slots left."""
    return assigned_count < depot["capacity"]

def validate_train_assignment(train, depot, assigned_count):
    """Run all constraints and return (bool, reasons)."""
    reasons = []

    if not check_fitness(train):
        reasons.append("fitness overdue")
    if not check_cleaning(train):
        reasons.append("needs cleaning")
    if not check_job_card(train):
        reasons.append("job card not ready")
    if not check_depot_capacity(depot, assigned_count):
        reasons.append("depot full")

    return (len(reasons) == 0, reasons)
