accounts = []

def find_account(name):
    for account in accounts:
        if account["name"] == name:
            return account
    raise ValueError("Account not found")


def create_account(name, initial_balance):
    if initial_balance < 0:
        raise ValueError("Balance cannot be negative")
    for account in accounts:
        if account["name"] == name:
            raise ValueError("Account already exists")

    account = {"name": name, "balance": initial_balance, "transactions": []}
    accounts.append(account)
    return account


def deposit(name, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    account = find_account(name)
    account["balance"] += amount
    account["transactions"].append({"type": "Deposit", "amount": amount})
    return account["balance"]


def withdraw(name, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")
    account = find_account(name)
    if amount > account["balance"]:
        raise ValueError("Insufficient funds")
    account["balance"] -= amount
    account["transactions"].append({"type": "Withdrawal", "amount": amount})
    return account["balance"]


def show_account(name):
    account = find_account(name)
    print("Name:", account["name"])
    print("Balance:", account["balance"])
    for t in account["transactions"]:
        print(t["type"], t["amount"])


# ---------- Testing ----------
create_account("Chloe", 100)

deposit("Chloe", 50)
deposit("Chloe", 25)

withdraw("Chloe", 30)
withdraw("Chloe", 20)

try:
    withdraw("Chloe", 1000)
except ValueError as e:
    print("Error:", e)

try:
    create_account("Chloe", 50)
except ValueError as e:
    print("Error:", e)

show_account("Chloe")