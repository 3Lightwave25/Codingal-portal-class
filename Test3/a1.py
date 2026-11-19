
n1 = "Alex"
n2 = "John"
n3 = "Sam"
n4 = "David"
n5 = "Ryan"

students = {
    n1: 85,
    n2: 92,
    n3: 76,
    n4: 68,
    n5: 95
}

total = 0

for score in students.values():
    total = total + score

average = total / 5

print("Class average:", average)

highest = max(students, key=students.get)
lowest = min(students, key=students.get)

print("Top scorer:", highest, students[highest])
print("Lowest scorer:", lowest, students[lowest])

n6 = input("Enter student name: ")

if n6 in students:
    print("Student score:", students[n6])
else:
    print("Student not found")
