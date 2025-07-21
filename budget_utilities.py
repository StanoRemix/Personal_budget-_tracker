from datetime import datetime
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
        return f"{self.date} | {self.category} | ${self.amount:.2f}"