# tests/test_constraints.py
import pytest
from constraints.constraints import (
    check_fitness, check_cleaning, check_job_card,
    check_depot_capacity, validate_train_assignment
)
from data.sample_data import trains, depots

def test_check_fitness():
    assert check_fitness(trains[0]) == (True, "Fitness OK")
    assert check_fitness(trains[1]) == (False, "Fitness overdue")

def test_check_cleaning():
    assert check_cleaning(trains[0]) == (True, "Cleaning OK")
    assert check_cleaning(trains[1]) == (False, "Needs cleaning")

def test_check_job_card():
    assert check_job_card(trains[0]) == (True, "Job card ready")
    assert check_job_card(trains[1]) == (False, "Job card not ready")

def test_check_depot_capacity():
    assert check_depot_capacity(depots[0], 2) == (True, "Depot has capacity")
    assert check_depot_capacity(depots[1], 2) == (False, "Depot full")

def test_validate_train_assignment():
    valid, reasons = validate_train_assignment(trains[0], depots[0], 0)
    assert valid is True
    assert reasons == []

    valid, reasons = validate_train_assignment(trains[1], depots[1], 1)
    assert valid is False

    # Case-insensitive check
    expected_issues = ["fitness overdue", "needs cleaning"]
    reasons_lower = [r.lower() for r in reasons]
    assert any(issue in reasons_lower for issue in expected_issues), f"Unexpected reasons: {reasons}"
