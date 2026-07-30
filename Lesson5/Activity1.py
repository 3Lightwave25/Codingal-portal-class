# ==========================================

# WEATHER OUTFIT PICKER

# ==========================================

# PART 1:

# Ask the user to enter today's temperature in Celsius

# Store the value in the variable `temperature`

# PART 2:

# If the temperature is below 20°C:

# - Set `outfit` to "jacket"

# - Display that it is cold and recommend the jacket

# Otherwise:

# - Set `outfit` to "t-shirt"

# - Display that it is warm and recommend the t-shirt

# PART 3:

# Ask the user whether it is raining (yes/no)

# Store the response in `is_raining`

# PART 4:

# If it is raining, remind the user to bring an umbrella

# PART 5:

# Ask the user to enter the wind speed in km/h

# Store the value in `wind_speed`

# PART 6:

# If the wind speed is greater than 30 km/h:

# - Set `needs_windbreaker` to "yes"

# - Recommend wearing a windbreaker over the chosen outfit

# Otherwise:

# - Set `needs_windbreaker` to "no"

# - Inform the user that a windbreaker is not needed

# PART 7:

# Ask the user whether there are puddles on the ground (yes/no)

# Store the response in `has_puddles`

# PART 8:

# If there are puddles:

# - Choose "boots"

# Otherwise:

# - Choose "sneakers"

# Display the recommended footwear

# PART 9:

# Print a blank line and display a message indicating

# that the weather check is complete

# PART 10:

# Print a summary showing:

# - Temperature

# - Outfit chosen

# - Whether it is raining

# - Whether a windbreaker is needed

# - Shoes chosen
temperature=int(input("What is today's weather in celsius?: "))
if temperature<20:
    outfit="Jacket"
    print("It is cold outside, you should wear a jacket")
else:
    outfit="T-shirt"
    print("It is warm ouside, you should wear a T-shirt")
is_raining=input("Is it raining today? Yes or No: ")
if is_raining=="Yes":
    Rain="umbrella"
    print("Dont forget an umbrella today!!")
wind_speed=int(input("What is the wind speed in km/h?: "))
if wind_speed>30:
    wind_breaker="yes"
    print("Wear a windbreaker over you chosen outfit then!")
else:
    wind_breaker="No"
    print("You do not need a windbreaker then!")
has_puddles=input("Are there puddles on the ground?: ")
if has_puddles=="Yes":
    Shoes="Boots"
    print("Wear boots then")
else:
    Shoes="sneakers"
    print("Wear sneakers then!")
print("***weather check complete***")
print("Summary: ")
print(temperature)
print(outfit)
print("Winder breaker: ",wind_breaker)
print(Shoes)




