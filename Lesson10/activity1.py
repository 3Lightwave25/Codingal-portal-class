# ==========================================

# MY CHORE CHECKLIST COUNTDOWN

# ==========================================

# PART 1:

# Set the total number of chores for today

# Store the original number of chores

# Print how many chores need to be completed

# PART 2:

# Create a counter to keep track of completed chores

# Create a variable to keep track of the current chore number

# PART 3:

# Use a while loop to repeat as long as there are chores left to complete

# PART 4:

# Use if-elif-else statements to determine the chore name

# based on the current chore number:

# - Chore 1: Make your bed

# - Chore 2: Feed the pet

# - Chore 3: Take out the trash

# - Chore 4: Wash the dishes

# Store the chore name in a variable

#

# Ask the user whether the current chore is finished

# PART 5:

# If the user answers "yes":

# - Increase the completed chore counter by 1

# - Move to the next chore

# - Print a message saying the chore is completed

# Otherwise:

# - Tell the user to finish the chore and check again

# PART 6:

# After every check, calculate and print the number of chores remaining

# Print a blank line after the result

# PART 7:

# After the while loop finishes, print a message saying

# that all chores are complete

# Print a congratulatory message

# PART 8:

# Demonstrate what an infinite loop would look like safely

# Create a variable whose value will not change

# Create a safety counter

#

# Use a while loop whose condition would normally remain true

# Print a message explaining that the condition never changes

# Increase the safety counter each time

#

# If the safety counter reaches 3:

# Print a message explaining that the loop is being stopped

# Use break to exit the loop safely

# PART 9:

# Print the final chore checklist summary

# Display:

# - Total chores assigned

# - Total chores completed

# - Total chores remaining

# Print a line to mark the end of the summary

ct=4
ac=ct
print("4 Chores have to be completed today!")
counter=0
n1=1
while n1<=4:
    if n1==1:
        nextchore="Making your bed"
    elif n1==2:
        nextchore="Feeding the pet"
    elif n1==3:
        nextchore="Taking out the trash"
    elif n1==4:
        nextchore="Washing the dishes"
    else:
        print("Error")
    n2=input(f"Have you finished {nextchore}?(Yes or No): ")
    if n2=="Yes":
        n1=n1+1
        counter=counter+1
        print("Great job! Chore completed.")
    else:
        print("Finish it and check again!")
    print(4-counter,"Chores are remaining.")

print("All chores completed, you can go play games.")
print(counter,"Have been completed.")
print(4-counter,"Are remaining")

#v=0
#while True:
    #print(v)
    #v=v+1

