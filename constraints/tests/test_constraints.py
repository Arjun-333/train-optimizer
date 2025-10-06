# tests/test_constraints.py
import pytest
from constraints.constraints import (
    check_fitness, check_cleaning, check_job_card,
    check_depot_capacity, validate_train_assignment
)
from data.sample_data import trains, depots

def test_check_fitness():
    assert check_fitness(trains[0]) == True
    assert check_fitness(trains[1]) == False

def test_check_cleaning():
    assert check_cleaning(trains[0]) == True
    assert check_cleaning(trains[1]) == False

def test_check_job_card():
    assert check_job_card(trains[0]) == True
    assert check_job_card(trains[1]) == False

def test_check_depot_capacity():
    assert check_depot_capacity(depots[0], 1) == True
    assert check_depot_capacity(depots[1], 1) == False

def test_validate_train_assignment():
    valid, reasons = validate_train_assignment(trains[0], depots[0], 0)
    assert valid == True
    assert reasons == []

    valid, reasons = validate_train_assignment(trains[1], depots[1], 1)
    assert valid == False
    assert "fitness overdue" in reasons or "needs cleaning" in reasons
