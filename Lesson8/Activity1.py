"""
1) Add the activity details.
   a) Mention the activity name as "Custom Ride Builder".
   b) Mention the file name as `ride_builder.py`.
   c) Mention the lesson as "Nested Conditional Statements".

2) Display the welcome message.
   a) Print a title banner for the ride builder.
   b) Add blank lines to keep the output neat.

3) Show the first vehicle choices.
   a) Display Bike as option 1.
   b) Display Car as option 2.
   c) Ask the user to enter 1 or 2.

4) Check the main choice.
   a) Use `if` when the user chooses Bike.
   b) Use `elif` when the user chooses Car.
   c) Use `else` for an invalid choice.

5) Use nested conditions for Bike.
   a) Show bike type options only if the user picked Bike.
   b) Ask the user to choose Scooty or Mountain Bike.
   c) Use an inner `if-else` to display the selected bike details.

6) Use nested conditions for Car.
   a) Show car type options only if the user picked Car.
   b) Ask the user to choose Sedan or SUV.
   c) Use an inner `if-else` to display the selected car details.

7) Display ride details.
   a) Print the selected ride name.
   b) Print speed or seat information.
   c) Print what the ride is best used for.

8) Handle invalid input.
   a) Show an error message if the first choice is not 1 or 2.
   b) Ask the user to enter the correct option next time.

9) End the program.
   a) Print a closing banner.
   b) Display a message saying the custom ride is ready.
"""

print("-------------Welcome to ride builder-------------")
op=int(input("Choose your vehicle. Type 1 for Bike and 2 for Car: "))
if op==1:
    n1=str(input("Scooty or Mountain Bike?: "))
    if n1=="Scooty":
        print("Selected Bike: Scooty.")
        print("Speed: 100km/h")
        print("Suitable for city ride, daily work use.")
    elif n1=="Mountain Bike":
        print("Selected Bike: Mountain Bike.")
        print("Speed: 175km/h")
        print("Suitable for dirt biking or rugged trek.")
    else:
        print("Error, Please try again(Check your spelling and capitalization.)")
elif op==2:
    n2=str(input("Sedan or SUV?: "))
    if n2=="Sedan":
        print("Selected Car: Sedan.")
        print("Speed: 160km/h")
        print("Suitable for city ride, daily work use, and comfort.")
    elif n2=="SUV":
        print("Selected Car: SUV.")
        print("Speed: 210km/h")
        print("Suitable for rugged terrain and obstacles.")
    else:
        print("Error, Please try again")
else:
    print("Error, Please try again and only type 1 or 2.")


