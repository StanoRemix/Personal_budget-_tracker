from budget_utilities import Transaction, save_data, load_data, calc_total
def prime():
    transactions = load_data()
    print("\n-- Transactions --")
    for transaction in transactions:
        print(transaction)
    
    print("\n-- Total by Category --")
    grand_total = calc_total(transactions)
    for category, total in grand_total.items():
        print(f"{category}: ₦{total:.2f}")

prime()