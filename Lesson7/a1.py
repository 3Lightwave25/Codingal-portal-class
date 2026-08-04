# 1) Store values in `v`, `w`, `x`, `y`, and `z`.

# 2) Calculate the expression (v + w) * x / y and store the result back in `z`.

# 3) Print the value of `z` with a message.

# 4) Store a name in `name` and a number in `age`.

# 5) Check this condition using `or` and `and`:
#    - The code checks if `name` is "Alex"
#      OR (if `name` is "John" AND `age` is 2 or more).
#    - If the condition is true, print the welcome message.
#    - Otherwise, print the goodbye message.

v=234
w=387
x=907
y=454
z=761
Calc=(v + w) * x / y
z=Calc
print("The answer to a random equation is: ",z)
Name="John"
Age=23
if (Name=="John" and Age>=2) or Name=="Alex":
    print("Hello! Welcome.")
else:
    print("Goodbye, See you later.")
