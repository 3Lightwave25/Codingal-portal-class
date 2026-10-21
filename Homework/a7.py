
n1 = 4
n2 = n1

print("You have", n2, "homework tasks to complete today!\n")

n3 = 0
n4 = 1

while n4 <= n1:

    if n4 == 1:
        n5 = "Math worksheet"
    elif n4 == 2:
        n5 = "Science reading"
    elif n4 == 3:
        n5 = "English writing"
    else:
        n5 = "Coding practice"

    n6 = input("Have you completed " + n5 + "? (yes/no): ")

    if n6 == "yes":
        n3 += 1
        n4 += 1
        print("Well done! One task finished.")
    else:
        print("Keep working on it and try again!")

    print("Tasks still remaining:", n1 - n3)
    print()

print("===== HOMEWORK FINISHED! =====")
print("Excellent work completing all your tasks!\n")

print("Now let's take a safe look at an infinite loop...")
n7 = 0
n8 = 0

while n7 <= 0:
    print("This condition stays true, so the loop would continue forever!")
    n8 += 1

    if n8 == 3:
        print("(The loop is being stopped here on purpose.)")
        break

print("\n===== HOMEWORK SUMMARY =====")
print("Tasks assigned:", n2)
print("Tasks completed:", n3)
print("Tasks remaining:", n1 - n3)
print("=======================================")
