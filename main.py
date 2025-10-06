# main.py
from data.sample_data import trains, depots
from constraints.constraints import validate_train_assignment

for train in trains:
    for depot in depots:
        valid, reasons = validate_train_assignment(train, depot, 0)
        print(f"{train['name']} -> {depot['name']}: {valid}, Reasons: {reasons}")
