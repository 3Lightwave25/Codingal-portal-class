def n1(n2, n3):
    n4 = n2 * (1 + 0.01 * n3)
    n4 = round(n4, 2)
    print(f"Your final amount is ${n4}")
    return n4


n1(150, 20)


def n5(n6):
    '''This function calculates the possible seating orders for guests.'''

    if n6 == 0 or n6 == 1:
        return 1
    else:
        return n6 * n5(n6 - 1)


n7 = "Seating calculation"

print(n5.__doc__)

print("1 guest:", n5(1))
print("2 guests:", n5(2))
print("3 guests:", n5(3))
print("5 guests:", n5(5))