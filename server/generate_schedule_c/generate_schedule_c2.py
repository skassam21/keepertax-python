from pprint import pprint


def generate_schedule_c2(multipliers, transactions):
    """Schedule C calculation with additional categories."""
    return {
        "meal": 0,
        "car": 0,
        "payment": 0,
        "home": 0,
        "phone": 0,
    }


MULTIPLIERS_2 = {
    "meal": 0.5,
    "car": 0.4,
    "home": 0.1,
    "phone": 0.5,
}
TRANSACTIONS_2 = [
    {
        "id": "t1",
        "category": "meal",
        "amount": 32.5,
    },
    {
        "id": "t2",
        "category": "meal",
        "amount": 51.33,
    },
    {
        "id": "t3",
        "category": "car",
        "amount": 300.02,
    },
    {
        "id": "t4",
        "category": "car",
        "amount": 350.61,
    },
    {
        "id": "t5",
        "category": "meal",
        "amount": 49.68,
    },
    {
        "id": "t6",
        "category": "payment",
        "amount": 45.0,
    },
    {
        "id": "t7",
        "category": "home",
        "amount": 550.0,
    },
    {
        "id": "t8",
        "category": "phone",
        "amount": 81.98,
    },
    {
        "id": "t9",
        "category": "phone",
        "amount": 81.98,
    },
]


if __name__ == "__main__":
    pprint(generate_schedule_c2(MULTIPLIERS_2, TRANSACTIONS_2), indent=2)
