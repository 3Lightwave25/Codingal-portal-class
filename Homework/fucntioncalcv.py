def n1(n2, n3):
    return n2 + n3

def n4(n5, n6):
    return n5 - n6

def n7(n8, n9):
    return n8 * n9

def n10(n11, n12):
    return n11 / n12


n13 = "Calculator Program"

print("======= MY MATH CALCULATOR =======")

try:
    n14 = float(input("Enter your first value: "))
    n15 = float(input("Enter your second value: "))
    n16 = input("Choose an operation (add, subtract, multiply, divide): ")

    if n16 == "add":
        print("Answer:", n1(n14, n15))

    elif n16 == "subtract":
        print("Answer:", n4(n14, n15))

    elif n16 == "multiply":
        print("Answer:", n7(n14, n15))

    elif n16 == "divide":
        print("Answer:", n10(n14, n15))

    else:
        print("Invalid operation selected.")

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

finally:
    print("Calculator session ended. Thank you!")