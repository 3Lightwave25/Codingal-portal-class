"""
1) Add the activity details.
   a) Mention the activity name as "Farm Harvest Calculator".
   b) Introduce the program as a harvest and earnings calculator.

2) Store harvest values.
   a) Use the assignment operator `=` to store harvest from five fields.
   b) Store each field's harvest in separate variables.

3) Use arithmetic operators.
   a) Use `+` to calculate the total harvest.
   b) Use `/` to calculate the average harvest per field.
   c) Use `*` to calculate total earnings.

4) Display total, average, and earnings.
   a) Print the total harvest in kilograms.
   b) Print the average harvest per field.
   c) Print the total earnings in rupees.

5) Use floor division and modulus.
   a) Use `//` to calculate the number of full 25 kg bags.
   b) Use `%` to calculate the leftover grain.
   c) Print the full bags and leftover amount.

6) Use comparison operators.
   a) Compare this year's harvest with last year's harvest.
   b) Use `>` to check if this year is better.
   c) Use `==` to check if both years are the same.
   d) Use `>=` to check if this year is at least as good.

7) Use assignment operators.
   a) Use `+=` to add bonus crop to the total.
   b) Use `-=` to subtract grain saved as seeds.
   c) Print the updated harvest after each change.

8) Calculate the final bag count.
   a) Use floor division again after adjustments.
   b) Print the final number of bags packed.
"""

h1=123
h2=145
h3=187
h4=110
h5=206
print("Total harvest: ",h1+h2+h3+h4+h5)
T=h1+h2+h3+h4+h5
print("Average harvest= ",T/5)
Cost=100
print("Total cost= ",T*Cost)
fb=25
print("Total 25kg bags= ",T//fb)
print("Leftover= ",T%fb)
tl=536
print("Last year's harverst= ",tl)
if T>tl:
    print("This year's harvest is better")
elif T==tl:
    print("Last year was the same")
else:
    print("Last year's harvest was better")
bc=123
ss=31
u=T+bc-ss
print("Updated harvest: ",u)
print("Final number of bags: ",u//fb)

