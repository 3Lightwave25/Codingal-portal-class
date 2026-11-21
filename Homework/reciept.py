def n1():
    print("Welcome to the Creative Corner!")
    print("Find all your drawing materials here.")

n1()

n2 = float(input("Enter the cost of one item in dollars: "))
n3 = int(input("How many items did you purchase? "))

def n4(n5, n6):
    n7 = n5 * n6
    return n7

n8 = n4(n2, n3)

n9 = round(n8, 2)
print("Your total bill is:", n9)

n10 = float(input("Enter the money you gave: "))

def n11(n12, n13):
    n14 = n12 - n13
    return n14

n15 = n11(n10, n9)
n16 = round(n15, 2)

def n17(n18):
    if n18 >= 5:
        return "You bought lots of supplies today!"
    else:
        return "Thank you for visiting our shop!"

n19 = n17(n3)

print("")
print("===== CUSTOMER RECEIPT =====")
print("Item Price:", n2)
print("Quantity:", n3)
print("Final Total:", n9)
print("Cash Received:", n10)
print("Your Change:", n16)
print(n19)
print("============================")