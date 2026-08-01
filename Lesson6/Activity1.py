# ==========================================

# SMART SCHOOL DAY PLANNER

# ==========================================

# PART 1:

# Display a welcome message explaining what the program does

# PART 2:

# Ask the user to enter:

# - The current day of the week

# - The weather (sunny, rainy, or cloudy)

# - Whether their homework is completed (yes or no)

# Store the responses in appropriate variables

# PART 3:

# Print a heading for the user's daily plan

# PART 4:

# Use an if-elif-else statement to determine the type of day:

# - Weekend (Saturday or Sunday)

# - Monday

# - Friday

# - Tuesday, Wednesday, or Thursday

# - Otherwise, display an invalid day message

# PART 5:

# If the weather is sunny AND the homework is completed,

# recommend going to the park after school

# PART 6:

# If the weather is rainy OR cloudy,

# remind the user to pack an umbrella

# PART 7:

# If the homework is NOT completed,

# remind the user to finish it before going out

# PART 8:

# Combine AND, OR, and NOT operators to suggest the best plan:

# - If it is rainy and homework is not done,

# recommend staying indoors and finishing homework

# - Else if it is sunny, homework is done, and it is a school day,

# recommend getting ready for a great school day

# - Else if it is a sunny weekend,

# recommend spending time outdoors

# - Otherwise, display a general motivational message

# PART 9:

# Print a completion message wishing the user a wonderful day

n1=str(input("What is the current day of the week?: "))
n2=str(input("What is the weather right now?: "))
n3=str(input("Did You complete your homework? Yes or no: "))
print("Daily Plan")
if n1=="Saturday" or n1=="Sunday":
    print("Weekend, enjoy your time!")
elif n1=="Monday":
    print("First day of the week,pack your weekly planner")
elif n1=="Friday":
    print("Last school day!Return library books.")
elif n1=="Tuesday"or n1=="Wednesday" or n1=="Thursday":
    print("Regular school day, stay focused.")
else:
    print("Error, Day not recognised. Please check the spelling.(Must start with capitalised letter.)")

if n2=="Sunny" and n3=="Yes":
    print("Then go out to play in the park!")
if n2=="Rainy" or n2=="Cloudy":
    print("Dont forget to pack an umbrella before gong out.")
if n3=="No":
    print("Complete your homework before going out")
if n3=="No" and n2=="Rainy":
    print("Stay indoors and complete your homework.")
elif (not(n1=="Sunday") or not(n1=="Saturday")) and n2=="Sunny" and n3=="Yes":
    print("Get ready for a great school day.")
elif (n1=="Saturday" or n1=="Sunday") and n2=="Sunny":
    print("Perfect weekend weather, head outside and have fun")
else:
    print("Take it one step at a time, You got this!")
print("Plan complete have a wonderfull day")
