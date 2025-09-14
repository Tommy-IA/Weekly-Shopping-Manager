print("Welcome to your personal shopping manager!")
print("Start setting your budget and adding products to your shopping list, type 'done' when you have finished.\n")

products = {}
budget_input = input("Insert your weekly budget in £: ")
budget = float(budget_input.replace("£","").strip())

while True:
    product = input("Enter a product (or 'done' to finish): ")
    if product.lower() == 'done':
        break
    if not product:
        print("Please enter a valid product name.")
        continue
    
    price_input = input(f"Price for {product}: ").strip()
    price = float(price_input.replace("£","").strip())
    products[product] = price

print("\nYour weekly shopping: ")
total = 0.0
for product, price in products.items():
    print(f"- {product}: {price:.2f} £")
    total += price

print(f"\nTotal bill: {total:.2f} £")

while total > budget and products:
    over = total - budget
    print(
        f"\nWarning! You are spending too much this week! Your budget is {budget:.2f} £",
        f"You are over {over:.2f} £, please eliminate something."
    )
    eliminate = input("Which item do you want to eliminate? ").strip().lower()
    matches = [k for k in products if k.lower() == eliminate]
    if matches:
        del products[matches[0]]
        total = sum(products.values())
    else:
        print(f"{eliminate} not found in your list.")

left = budget - total
if total <= budget:
    print(f"\n You are within budget. You still have {left:.2f} £ left.")
else:
    print("\n You are still over budget.")

print("\nThe final list is:")
if not products:
    print("(empty)")
else:
    for product, price in products.items():
        print(f"- {product}: {price:.2f} £")


    
