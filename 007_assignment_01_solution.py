########################################################
# Variables
########################################################

# Question 1: Calculate the area of a rectangle

# Define the rectangle dimensions
length = 5
width = 10

# Calculate the area
recArea = length * width

# Print the result
print("Rectangle Area:", recArea)


########################################################
# Circle Area
########################################################

# Define the value of pi and the radius
pi = 3.14
r = 10

# Calculate the square of the radius
rSq = r * r      # You can also write: r ** 2

# Calculate the area of the circle
cirArea = pi * rSq

# Print the result
print("Circle Area:", cirArea)

# Print the text "cirArea"
print("cirArea")

# Print the value stored in the variable
print(cirArea)


########################################################
# Strings
########################################################

# Examples of writing strings using different quotation marks

# name1 = '"Sara"'
# name2 = "\"Sara\""
# name3 = '''Sara
# Mohamed
# '''


########################################################
# String Formatting with Numbers
########################################################

# Create a variable
age = 23

# %d is used for integer values
info = "My age is %d"

# Print using string formatting
print(info % age)

# Another example
print("I'm %d years old." % age)

# Print using commas
print("My age is", age, "years old.")


########################################################
# String Formatting with Text
########################################################

# Create string variables
name1 = "Adam"
name2 = "Mohammed"
name3 = "Joe"

# %s is used for strings
info = "My name is %s"

# Print different names
print(info % name1)
print(info % name2)
print(info % name3)


########################################################
# Multiple Variables
########################################################

# Create variables
myName = "Sara"
myAge = 22

# Create format strings
info_1 = "My name is %s. "
info_2 = "My age is %d."

# Incorrect example
# print("I'm %d years old %s" % age % name)

# Correct example
print(info_1 % myName + info_2 % myAge)