n1 = 27
n2 = 5
n3 = 0
n4 = 0

print("=" * 42)
print(" GUESS THE SECRET NUMBER")
print("=" * 42)
print("I picked a number from 1 to 50.")
print("You get 5 chances to find my number.")
print("I will give you clues after every incorrect answer.")
print()

while n3 < n2 and n4 != n1:
    n4 = int(input("Enter your number: "))
    n3 = n3 + 1

    if n4 == n1:
        print()
        print("Amazing! You found the number in", n3, "tries!")
        print("You are really good at this!")
    else:
        if n4 > n1:
            n5 = n4 - n1
        else:
            n5 = n1 - n4

        if n5 >= 20:
            print("Very far! Try a different number.")
        elif n5 >= 10:
            print("Not quite close yet.")
        elif n5 >= 5:
            print("You are getting closer!")
        else:
            print("So close! Keep trying!")

        n6 = n2 - n3
        if n6 > 0:
            print("Chances remaining: ", end="")
            for n7 in range(n6):
                print("Heart ", end="")
            print()
            print()

if n4 != n1:
    print("=" * 42)
    print("No more chances left!")
    print("The correct number was:", n1)
    print("=" * 42)