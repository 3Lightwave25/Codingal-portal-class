"""
1) Ask for agent details.
   a) Ask the user to enter their real name.
   b) Ask the user to enter their favourite gadget.
   c) Store both inputs as text values.

2) Store agent information.
   a) Create variables for agent number, speed rating, mission count, height, and active status.
   b) Use different data types such as integer, float, string, and Boolean.

3) Display each value and its data type.
   a) Print the agent name and gadget.
   b) Print number, rating, mission count, height, and active status.
   c) Use `type()` to show the data type of each value.

4) Convert values into text.
   a) Use `str()` to convert numbers into strings.
   b) Convert the Boolean value into text.
   c) Print the converted values and their new data types.

5) Create a secret code name.
   a) Use slicing to get the first three letters of the name.
   b) Use negative indexing to get the last letter.
   c) Join both parts to create the code name.

6) Reverse the gadget name.
   a) Use slicing with `[::-1]` to reverse the gadget text.
   b) Print the reversed gadget name.

7) Build the badge message.
   a) Create separate lines for the agent badge.
   b) Use string concatenation to join text and variables.
   c) Use `.upper()` to make important badge text uppercase.

8) Print the secret agent badge.
   a) Print a badge heading.
   b) Print all badge lines one by one.
   c) Print a closing line to complete the badge.
"""

n1=str(input("What is your real name?: "))
n2=str(input("What is your favorite gadget?: "))
an=76482
sr=4.4215
mc=27
acs= True 
print("Agent name: ",n1,type(n1))
print("Agent gadget: ",n2,type(n2))
print("Agent number: ",an,type(an))
print("Speed rating: ",sr,type(sr))
print("Mission count: ",mc,type(mc))
print("Active status: ",acs,type(acs))
an=str(an)
sr=str(sr)
mc=str(mc)
acs=str(acs)
print(type(an))
print(type(sr))
print(type(mc))
print(type(acs))
secret=n1[0:4]+n1[-1]
code=n2[::-1]
print("Reverse gadget: ",code)
badgeline1="AGENT "+secret.upper()
badgeline2="ID "+ an+"Missions: "+mc
badgeline3="Speed rating: "+sr+"Active status: "+acs
badgeline4="Secret gadget code"+code
print(badgeline1)
print(badgeline2)
print(badgeline3)
print(badgeline4)
