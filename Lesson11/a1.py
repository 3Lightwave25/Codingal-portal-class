# PART 1:

# Display the ATM welcome message

# Create counters to track the number of notes dispensed:

# - 100-unit notes

# - 50-unit notes

# - 20-unit notes

# - 10-unit notes

# - 5-unit notes

# - 1-unit notes

# Also create counters for customers served and total money dispensed

# PART 2:

# Create a Boolean variable called `serving`

# Set it to True so the ATM can continue serving customers

# PART 3:

# Create an outer while loop that continues while `serving` is True

# This loop should handle one customer per iteration

# PART 4:

# Ask the customer to enter their name

# Ask the customer to enter the withdrawal amount

# Store both values in variables

# PART 5:

# Check whether the withdrawal amount is valid

# If the amount is less than or equal to 0:

# - Display an invalid amount message

# - Use `continue` to return to the beginning of the while loop

# PART 6:

# Display the amount that will be dispensed

# Create a variable called `remaining` and store the withdrawal amount in it

# Create a counter called `idx` and start it at 1

# PART 7:

# Create an inner while loop that runs through 6 denominations

# Use if-elif-else to determine the note value based on `idx`:

# - 1 → 100

# - 2 → 50

# - 3 → 20

# - 4 → 10

# - 5 → 5

# - 6 → 1

# PART 8:

# Inside the inner while loop:

# Calculate how many notes of the current denomination are needed

# using integer division (`//`)

#

# If the number of notes is greater than 0:

# - Print the number and value of the notes

# - Subtract the dispensed amount from `remaining`

# - Update the appropriate denomination counter

#

# Increase `idx` by 1 after each iteration

# PART 9:

# After the inner while loop finishes:

# Increase the number of customers served by 1

# Add the withdrawal amount to the total amount dispensed

# Print a transaction completion message

print("Welcome to the ATM!")
hund=0
fift=0
twen=0
ten=0
five=0
one=0
total=0
cs=0
serving=True
while serving:
    n1=str(input("What is your name?: "))
    n2=int(input("What is the amount you want to withdraw?: "))
    if n2<=0:
        print("Invalid, Error(Please try again)")
        continue
    print("Dispensing amount",n2,"For",n1)
    remaining=n2
    idx=1
    while idx<=6:
        if idx==1:
            value=100
        elif idx==2:
            value=50
        elif idx==3:
            value=20
        elif idx==4:
            value=10
        elif idx==5:
            value=5
        else:
            value=1
        count=remaining//value
        if count>0:
            print(count,"x",value)
            print("Amount= ",count*value)
            remaining=remaining-(count*value)
        idx=idx+1
    cs=cs+1
    total=total+n2
    print("Transaction complete. Thank you ",n1,"for using our ATM")
    n3=str(input("Next customer, Yes or No?: "))
    if n3=="No":
        serving=False
print("Customer served:",cs,", Total dispensed amount: ",total,)








