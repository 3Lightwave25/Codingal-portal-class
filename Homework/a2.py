
print("=== Pool Entry Checker ===")
print("Answer 3 questions to find out which pool you can use.\n")

n1 = int(input("How old are you? "))
n2 = input("Can you swim? (yes / no): ").lower()
n3 = input("Is an adult with you? (yes / no): ").lower()

print()
print("=== Entry Decision ===")
print("-" * 32)

if n1 < 4:
    print("Age group: Toddler - splash pool only, always with an adult.")
elif n1 < 12:
    print("Age group: Child - main pool with an adult.")
elif n1 < 18:
    print("Age group: Teen - main pool alone if you can swim.")
else:
    print("Age group: Adult - all pools are open to you.")

if n2 != "yes" and n2 != "no":
    print("Input error: Please answer the swimming question with yes or no.")
    n4 = False
else:
    n4 = True

if n3 != "yes" and n3 != "no":
    print("Input error: Please answer the adult question with yes or no.")
    n5 = False
else:
    n5 = True

if n2 == "yes" and n3 == "yes":
    print("Deep pool: Entry allowed - you can swim and an adult is present.")

if n1 < 12 or n2 == "no":
    print("Shallow pool: Stay in the shallow area today.")

if n5 == True and not (n3 == "yes"):
    print("Reminder: No adult is with you - the lifeguard must be told.")

if n4 == False or n5 == False:
    print("Verdict: Cannot decide until both questions are answered properly.")
elif n1 >= 18 and n2 == "yes":
    print("Verdict: Full access. Enjoy your swim!")
elif n1 >= 12 and n2 == "yes" and n3 == "yes":
    print("Verdict: Main pool access with an adult nearby.")
elif n2 == "no" and not (n3 == "yes"):
    print("Verdict: Shallow end only. Please find an adult first.")
else:
    print("Verdict: Shallow end today - come back with an adult for more.")

print()
print("Have a safe swim!")
