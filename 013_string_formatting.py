###########################################################
# String Formatting in Python
###########################################################

# String formatting is used to insert variables
# and values inside strings to create dynamic messages.



###########################################################
# 1. String Concatenation (+)
###########################################################

# The simplest way to combine strings
# using the + operator

first_name = "Sara"
last_name = "Alwadia"

full_name = first_name + " " + last_name

print(full_name)



###########################################################
# Concatenation with Numbers
###########################################################

age = 20


# We cannot concatenate string and integer directly

# This will cause an error:
# print("My age is " + age)


# Convert integer to string using str()

print("My age is " + str(age))



###########################################################
# 2. Old Style Formatting (%)
###########################################################

# Python supports old formatting using % operator.

# Common format specifiers:

# %s --> String
# %d --> Integer
# %f --> Float


name = "Sara"
age = 20
gpa = 93.51


print("Name: %s" % name)

print("Age: %d" % age)

print("GPA: %f" % gpa)



###########################################################
# Multiple Values using %
###########################################################

# When using multiple variables,
# put them inside a tuple ()

print("My name is %s and I am %d years old." % (name, age))



###########################################################
# Formatting Float Numbers with %
###########################################################

price = 15.6789


# %.2f means show only 2 digits after decimal point

print("Price = %.2f" % price)


# %.1f means show 1 digit after decimal point

print("Price = %.1f" % price)



###########################################################
# 3. String format() Method
###########################################################

# Another way to format strings
# using the format() function


name = "Sara"
age = 20


print("My name is {} and I am {} years old.".format(name, age))



###########################################################
# Using Positions with format()
###########################################################

# We can specify the position of values

print("My name is {0} and I am {1} years old.".format(name, age))


print("I am {1} years old and my name is {0}.".format(name, age))



###########################################################
# Using Names with format()
###########################################################

print("My name is {n} and I am {a} years old.".format(n=name, a=age))


###########################################################
# Formatting Numbers using format()
###########################################################

number = 1234.56789


# Show 2 decimal places

print("Number = {:.2f}".format(number))



###########################################################
# 4. f-Strings (Modern Method)
###########################################################

# Introduced in Python 3.6
# The recommended way to format strings today.


name = "Sara"
age = 22


print(f"My name is {name} and I am {age} years old.")



###########################################################
# f-String with Expressions
###########################################################

num1 = 10
num2 = 5


print(f"Sum = {num1 + num2}")

print(f"Multiplication = {num1 * num2}")



###########################################################
# f-String with Functions
###########################################################

text = "python"


print(f"Uppercase: {text.upper()}")

print(f"Length: {len(text)}")



###########################################################
# f-String Number Formatting
###########################################################

price = 15.6789


# Two decimal places

print(f"Price = {price:.2f}")



percentage = 0.756


# Percentage formatting

print(f"Percentage = {percentage:.2%}")



###########################################################
# f-String with Multiple Variables
###########################################################

student_name = "Ahmed"
university = "University of Palestine"
major = "IT"


print(
    f"""
Student Information
-------------------
Name: {student_name}
University: {university}
Major: {major}
"""
)



###########################################################
# Comparison Example
###########################################################

name = "Sara"
age = 20


# Concatenation

print("My name is " + name + " and I am " + str(age))


# % formatting

print("My name is %s and I am %d" % (name, age))


# format()

print("My name is {} and I am {}".format(name, age))


# f-string

print(f"My name is {name} and I am {age}")



###########################################################
# Practice
###########################################################

# Create variables:

student = "Sara"
course = "Python"
hours = 50


# Print:

# Sara is taking Python course for 50 hours.


# Use:
# 1. Concatenation
# 2. % formatting
# 3. format()
# 4. f-string