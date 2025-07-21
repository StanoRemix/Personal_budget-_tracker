from datetime import datetime
import json
import os
from collections import defaultdict

DATA_FILE = 'budget_data.json'


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump([d.to_rec() for d in data], f, indent=4)


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        records = json.load(f)
    return [Transaction(rec["category"], rec["amount"], rec["date"], rec.get("item")) for rec in records]


class Transaction:
    def __init__(self, category, amount, date=None, item=None):
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')
        self.category = category
        self.item = item or "General"
        self.amount = float(amount)

    def to_rec(self):
        return {
            'date': self.date,
            'category': self.category,
            'item': self.item,
            'amount': self.amount
        }

    def __str__(self):
        return f"{self.date} | Category: {self.category} | Item: {self.item} | Amount: ₦{self.amount:.2f}"


def calc_total(transactions):
    grand_total = defaultdict(float)
    for transaction in transactions:
        grand_total[transaction.category] += transaction.amount
    return dict(grand_total)