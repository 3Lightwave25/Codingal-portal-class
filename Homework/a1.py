
n1 = int(input("Enter homework time in minutes: "))

if n1 > 60:
    n2 = "start homework now"
    print("You have a long homework session ahead.")
else:
    n2 = "finish homework quickly"
    print("Your homework session should be short.")

n3 = input("Will you have free time after homework? (yes/no): ")

if n3 == "yes":
    print("Tip: spend your free time doing a hobby you enjoy!")

print("===== YOUR DAILY SCHEDULE =====")
print("Homework duration:", n1, "minutes")
print("Suggested plan:", n2)
print("Free time available:", n3)
