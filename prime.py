from budget_utilities import Transaction, save_data, load_data
def prime():
    print("Loading budget data...")
    transactions = load_data()
    print("Current Transactions:")
    for transaction in transactions:
        print(transaction)
    print("\nAdding a new transaction...")
    new_transaction = Transaction("Groceries", 1500.00)
    transactions.append(new_transaction)
    save_data(transactions)
    print("New transaction added successfully.")
    print("Updated Transactions:")
    for transaction in transactions:
        print(transaction)
prime()