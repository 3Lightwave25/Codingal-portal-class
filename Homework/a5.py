
print("====================================")
print("      Welcome to Trip Planner!      ")
print("====================================")
print()

print("Step 1: Choose your holiday")
print("  1 - Beach Trip")
print("  2 - Mountain Trip")
print()

n1 = int(input("Choose 1 or 2: "))
print()

if n1 == 1:
    print("Step 2: Choose a beach activity")
    print("1 - Swimming")
    print("  2 - Making Sandcastles")
    print()

    n2 = int(input("Choose 1 or 2: "))
    print()

    if n2 == 1:
        print("Your activity: Swimming")
        print("Best time: Morning")
        print("Bring along: Sunscreen and water")
    else:
        print("Your activity: Making Sandcastles")
        print("Best time: Evening")
        print("Bring along: A bucket and spade")

elif n1 == 2:
    print("Step 2: Choose a mountain activity")
    print("  1 - Hiking")
    print("  2 - Camping")
    print()

    n3 = int(input("Choose 1 or 2: "))
    print()

    if n3 == 1:
        print("Your activity: Hiking")
        print("Best for: Discovering nature trails")
        print("Bring along: Comfortable shoes")
    else:
        print("Your activity: Camping")
        print("Best for: Enjoying the outdoors")
        print("Bring along: A tent and flashlight")

else:
    print("Invalid option!")
    print("Enter 1 for a Beach Trip or 2 for a Mountain Trip.")

print()
print("====================================")
print("       Your trip plan is ready!     ")
print("       Have a great holiday!        ")
print("====================================")
