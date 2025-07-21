from budget_utilities import Transaction, save_data, load_data, calc_total


def menu_display():
    print("\n===== PERSONAL BUDGET TRACKER =====")
    print("-" * 40)
    print("\nBudget Tracker Menu:")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Calculate Total by Category")
    print("4. Exit")
    print("-" * 40)


def prime():
    transactions = load_data()
    while True:
        menu_display()
        in_req = int(input("Select an option (1-4): "))
        if in_req == 1:
            category = input("\nEnter category: ")
            item = input("Enter item (optional, press Enter to skip): ")
            if not item.strip():
                item = None
            amount = input("Enter amount: ")
            try:
                transaction = Transaction(category, float(amount), item=item)
                transactions.append(transaction)
                save_data(transactions)
                print("Transaction added successfully.")
            except ValueError:
                print("\nInvalid amount. Please enter a numeric value.")
        elif in_req == 2:
            if not transactions:
                print("\nNo transactions found.")
            else:
                print("\nTransactions:")
                for transaction in transactions:
                    print(transaction)
        elif in_req == 3:
            if not transactions:
                print("\nNo transactions to calculate totals.")
            else:
                totals = calc_total(transactions)
                print("\nTotal by Category:")
                for category, total in totals.items():
                    print(f"{category}: ₦{total:.2f}")
        elif in_req == 4:
            print("Exiting the budget tracker...")
            break
        else:
            print("Invalid option. Please try again.")


prime()
