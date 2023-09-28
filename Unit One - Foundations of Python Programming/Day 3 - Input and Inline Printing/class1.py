age = 40
name = "steve"

# print a line that says "I am Steve and I am 40 years old" using the variables age and name
print("I am "+ name +" and I am " + str(age) +" years old.")
# I have to wrap non-string variables in str
# Alot of people/students have issues with all the opening and closing of quotation marks ("") and all the plus sign (++) variables

print(f"I am {name} and I am {age} years old.")
#f string is much simpler than regular string format
# f string automatically changes variables to strings, with no need of "", ++