import random
import math

n1 = "Random Number Challenge"

print("========== FUN NUMBER TOOL ==========")

n2 = random.randint(1, 10)
print("Your lucky number:", n2)

n3 = ["Play football", "Watch a movie", "Solve a riddle", "Listen to music"]
n4 = random.choice(n3)

print("Today's activity:", n4)

n5 = random.randint(1, 5)

print("\nTry to find the hidden number between 1 and 5!")

while True:
    n6 = int(input("Enter your answer: "))

    if n6 == n5:
        print("Well done! You got it right.")
        break
    else:
        print("That is incorrect. Try once more!")

n7 = float(input("\nEnter any decimal value: "))

print("Rounded up value:", math.ceil(n7))
print("Rounded down value:", math.floor(n7))

n8 = 10
n9 = -5

print("Result after copying the sign:", math.copysign(n8, n9))

n10 = int(input("Enter a negative value: "))
print("Absolute result:", math.fabs(n10))

n11 = int(input("Enter the first value for GCD: "))
n12 = int(input("Enter the second value for GCD: "))

print("Greatest common divisor:", math.gcd(n11, n12))

print("\n========== FINAL RESULTS ==========")
print("Lucky number:", n2)
print("Activity selected:", n4)
print("Hidden number:", n5)
print("===================================")