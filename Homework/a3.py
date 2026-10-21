
n1 = 1
n2 = 2
n3 = 4
n4 = 8

n5 = ["coding app", "math app", "reading app", "science app"]

n6 = input("Enter your name: ")
n7 = input("Which app do you want to use? ").lower()

print("\n--- Identity Operator Test ---")

if type(n6) is str:
    print("Your name has been saved as text.")

if type(n7) is not int:
    print("The app name is not stored as a number.")

print("\n--- Membership Operator Test ---")

if n7 in n5:
    print(n7, "is on the approved student app list.")
else:
    print(n7, "is not on the approved student app list.")

n8 = ["gaming app", "shopping app", "social media app"]

if n7 not in n8:
    print("This app is not listed as restricted.")
else:
    print("Access blocked because this app is restricted.")

print("\n--- App Permission Settings ---")

n9 = n1 | n2 | n3

print("Permission number:", n9)
print("Permission bits:", bin(n9))

if n9 & n1:
    print("Camera access: Enabled")

if n9 & n2:
    print("Microphone access: Enabled")

if n9 & n3:
    print("Storage access: Enabled")

if n9 & n4:
    print("Location access: Enabled")
else:
    print("Location access: Disabled")

print("\n--- Bit Shift Test ---")

n10 = n1 << 1

print("Camera bit value:", bin(n1))
print("Value after shifting left:", bin(n10))

n11 = n3 >> 1

print("Storage bit value:", bin(n3))
print("Value after shifting right:", bin(n11))

print("\n--- Final Access Result ---")

if n7 in n5 and n7 not in n8:
    print("Access approved for", n7)
else:
    print("Access refused for", n7)
