expenses = []

def add_expense(amount, category, description):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    expense = {"amount": amount, "category": category, "description": description}
    expenses.append(expense)
    return expense

def calculate_total_expenses():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def calculate_total_by_category(category):
    total = 0
    for expense in expenses:
        if expense["category"] == category:
            total += expense["amount"]
    return total

def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['category']} - {expense['description']}: ${expense['amount']}")


# Add multiple expenses
add_expense(25.50, "Food", "Lunch")
add_expense(10, "Transport", "Bus")
add_expense(5, "Food", "Snack")
add_expense(40, "Health", "Vitamins")

# Invalid expense
try:
    add_expense(-5, "Food", "Bad expense")
except ValueError as e:
    print("Error:", e)

# Totals
print("Total expenses:", calculate_total_expenses())
print("Total for Food:", calculate_total_by_category("Food"))

# Show all expenses
print("\nAll expenses:")
show_expenses()