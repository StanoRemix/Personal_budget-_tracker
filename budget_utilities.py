from datetime import datetime
import json
import os

DATA_FILE = 'budget_data.json'


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump([d.to_rec() for d in data], f, indent=4)


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        records = json.load(f)
    return [Transaction(rec["category"], rec["amount"], rec["date"]) for rec in records]


class Transaction:
    def __init__(self, category, amount, date=None):
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')
        self.category = category
        self.amount = float(amount)

    def to_rec(self):
        return {
            'date': self.date,
            'category': self.category,
            'amount': self.amount
        }

    def __str__(self):
        return f"{self.date} | {self.category} | ₦{self.amount:.2f}"
