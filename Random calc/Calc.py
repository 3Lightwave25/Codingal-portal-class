def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b
if __name__ == "__main__":
    op=float(input("Enter Operation(1 for addition, 2 for subtraction, 3 for multiplication, 4 for division): ")) 
    n1=float(input("Enter first number: "))
    n2=float(input("Enter second number: "))
    if op==1:
        print("Result:", add(n1, n2))
    elif op==2:
        print("Result:", subtract(n1, n2))
    elif op==3:
        print("Result:", multiply(n1, n2))
    elif op==4:
        print("Result:", divide(n1, n2))
    else:
        print("Invalid operation!")
