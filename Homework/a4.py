
print("=== GROCERY PRICE COMPARISON ===")

n1 = 12
n2 = 4
n3 = 8
n4 = 2
n5 = 4

n6 = (n1 + n2 + n3) * n4 / n5

print("\nPART 1 - This week's grocery cost")
print("Price for each person:", n6)

print("\nPART 2 - Sharing grocery items")

n7 = int(input("How many grocery items are there in total? "))
n8 = int(input("How many people will share the items? "))

if n8 == 0:
    print("Items cannot be divided between zero people.")
else:
    if n7 % n8 == 0:
        print(n7, "items can be shared equally among", n8, "people -", n7 // n8, "each.")
    else:
        print(n7, "items cannot be shared equally among", n8, "people -", n7 % n8, "items remaining.")

print("\nPART 3 - Correcting the weekly average")

n9 = 65
n10 = 4
n11 = 50
n12 = 80

n13 = n9 * n10
n14 = n13 - n11 + n12
n15 = n14 / n10

print("Original total:", n13)
print("Updated total:", n14)
print("Updated weekly average:", n15)

print("\nPART 4 - Comparing store prices")

n16 = 70
n17 = 75
n18 = 80

print("Store A:", n16, "| Store B:", n17, "| Store C:", n18)

if n15 < n16 and n15 < n17 and n15 < n18:
    n19 = "less expensive than all three stores"
elif n15 > n16 and n15 > n17 and n15 > n18:
    n19 = "more expensive than all three stores"
else:
    n19 = "between the prices of the three stores"

print("Your weekly average is", n19)

print("\n=== FINAL SUMMARY ===")
print("Grocery cost per person:", n6)
print("Corrected weekly average:", n15)
print("Price comparison:", n19)
