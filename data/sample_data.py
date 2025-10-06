# data/sample_data.py
"""
Sample dataset of trains and depots for testing constraints.
"""

trains = [
    {
        "id": 1,
        "name": "Train A",
        "mileage": 12000,
        "fitness_due_at": 20000,
        "needs_cleaning": False,
        "job_card_ready": True,
        "priority": 5
    },
    {
        "id": 2,
        "name": "Train B",
        "mileage": 22000,
        "fitness_due_at": 20000,
        "needs_cleaning": True,
        "job_card_ready": False,
        "priority": 3
    },
    {
        "id": 3,
        "name": "Train C",
        "mileage": 18000,
        "fitness_due_at": 18000,
        "needs_cleaning": False,
        "job_card_ready": True,
        "priority": 4
    },
    {
        "id": 4,
        "name": "Train D",
        "mileage": 5000,
        "fitness_due_at": 15000,
        "needs_cleaning": True,
        "job_card_ready": True,
        "priority": 2
    },
    {
        "id": 5,
        "name": "Train E",
        "mileage": 16000,
        "fitness_due_at": 16000,
        "needs_cleaning": False,
        "job_card_ready": False,
        "priority": 1
    }
]

depots = [
    {"id": 1, "name": "Depot East", "capacity": 3},
    {"id": 2, "name": "Depot West", "capacity": 2}
]
