print("WELCOME TO THE ISMY SHOP")
print("*" * 20)

item = input("What do you want to buy? ")
price = float(input(f"What is the price of {item}? "))
quantity = float(input(f"How many {item} are you buying? "))

print(f"Added {quantity} {item} to shopping cart")
print(f"Subtotal: ${quantity * price}")
