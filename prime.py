from budget_utilities import Transaction
def test_transaction():
    test = Transaction("Food", 9000)
    print(test)
    print("As recorded:", test.to_rec())

test_transaction()