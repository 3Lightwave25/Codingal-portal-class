
print("=== Power Calculator ===")

n1 = int(input("Enter the base number: "))
n2 = int(input("Enter the power: "))

n3 = 1

for n4 in range(1, n2 + 1):
    n3 = n3 * n1
    print("Step", n4, "- Current result:", n3)

print()
print(n1, "raised to the power of", n2, "equals", n3)
