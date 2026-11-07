
print("=== Grocery Billing Queue ===\n")

# PART 1: Counters
low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True

# PART 2: Outer while loop
while billing == True:
    name = str(input("What is your name?: "))
    item_count = int(input(f"Hello {name}, How many items are you buying?: "))

    # PART 3: Invalid item count
    if item_count <= 0:
        print("Invalid, please try again.")
        continue

    print(f"\nBilling for {name}: ")
    customer_total = 0
    item_number = 1

    # PART 4: Inner while loop
    while item_number <= item_count:
        item_name = str(input("The item name: "))
        item_price = int(input("Item price (In Dollars $): "))
        item_quantity = int(input("Item quantity: "))

        # PART 5: Validation and calculations
        if item_price <= 0 or item_quantity <= 0:
            print("Invalid, Please enter positive values above 0.")
            continue

        item_total = item_price * item_quantity
        customer_total += item_total

        print(f"{item_name}: {item_quantity} x {item_price} = {item_total}$")

        if item_price < 50:
            low_price_items += item_quantity
        elif item_price >= 50 and item_price <= 100:
            medium_price_items += item_quantity
        elif item_price > 100:
            high_price_items += item_quantity

        item_number += 1

    # PART 6: Finish customer
    customers_served += 1
    total_sales += customer_total

    print(f"\n{name}'s total bill: ${customer_total}")

    next_customer = input("Next customer? (yes/no): ").lower()

    if next_customer != "yes":
        billing = False

# PART 7: Daily report
print("\n=== Daily Sales Report ===")

bands = [
    ("Low Price Items", low_price_items),
    ("Medium Price Items", medium_price_items),
    ("High Price Items", high_price_items)
]

for band_name, count in bands:
    print(band_name + ": ", end="")
    for i in range(count):
        print("*", end="")
    print()

print("Customers served:", customers_served)
print("Total sales: $", total_sales)
