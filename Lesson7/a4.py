## Instructions

#1. Accept three integer values from the user.

#2. Calculate the average of the three numbers.

#3. Display the calculated average.

#4. Compare the average with each of the three input values using conditional statements.

#5. If the average is greater than all three numbers, display a message indicating that it is higher than all three values.

#6. If the average is greater than only two of the input values, display a message indicating which two values are less than the average.

#7. If the average is greater than only one of the input values, display a message indicating which value is less than the average.

#8. If the average is not greater than any of the input values, display the message **"invalid input"**.

#9. Use `if`, `elif`, and `else` statements to implement the required logic.

#10. Display the output in a clear and readable format.

n1=int(input("Enter first Interger: "))
n2=int(input("Enter second Integer: "))
n3=int(input("Enter third Integer: "))
Total=n1+n2+n3
Mean=Total/3
print("The average is: ",Mean)
if Mean>n1 and Mean>n2 and Mean>n3:
    print("The average is higher than all three values")
elif (Mean>n1 and Mean>n2) or (Mean>n2 and Mean>n3) or (Mean>n1 and Mean>n3):
    print("Only 2 values are less than average.")
elif Mean>n1 or Mean>n2 or Mean>n3:
    print("The mean is only greater than one of the values")
else:
    print("Invalid Input.")
    