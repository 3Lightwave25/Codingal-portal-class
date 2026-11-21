n1 = False
n8 = "Shopping calculator"

while not n1:

    try:
        n2 = float(input("Enter your total shopping cost: "))
        n3 = float(input("Enter discount percentage: "))
        n4 = int(input("How many people are sharing the bill? "))

        n5 = n2 * n3 / 100
        n6 = n2 - n5
        n7 = n6 / n4

    except ValueError:
        print("Invalid input! Please enter numbers.")

    except ZeroDivisionError:
        print("The number of people cannot be zero.")

    else:
        print("Amount after discount:", n6)
        print("Amount per person:", n7)
        n1 = True

    finally:
        print("Calculation attempt completed.")