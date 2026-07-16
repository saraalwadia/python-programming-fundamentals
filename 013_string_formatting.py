# ===========================================================
# String Formatting in Python
# ===========================================================


"""
Teaching Notes:

Lesson Objectives:
- Understand different ways to combine text and variables.
- Learn old and modern string formatting techniques.
- Compare different formatting approaches.
- Use f-strings for writing clean and readable code.


Prerequisites:
- Variables
- Strings
- Concatenation
- Type Conversion
- String Methods


What is String Formatting?

String formatting is the process of inserting variables
and values inside strings to create dynamic messages.


Example:

name = "Sara"

Output:

Hello Sara


Python provides different ways:

1. String Concatenation (+)
2. Old Style Formatting (%)
3. format() Method
4. f-Strings (Recommended)


-----------------------------------------------------------

PART 1:
String Concatenation (+)

- The oldest and simplest method.
- Uses + operator.
- Works only with strings.
- Numbers must be converted using str().


Example:

"My age is " + str(age)


Problems:
- Code becomes difficult to read with many variables.
- Requires manual conversion.


-----------------------------------------------------------

PART 2:
Old Style Formatting (%)

Format Specifiers:

%s --> String

%d --> Integer

%f --> Float


Example:

"My age is %d" % age


Advantages:
- Shorter than concatenation.


Disadvantages:
- Old style.
- Less readable with many variables.


-----------------------------------------------------------

PART 3:
format() Method

Uses placeholders:

{}


Example:

"Hello {}".format(name)


Can use:
- Positions
- Named arguments
- Number formatting


-----------------------------------------------------------

PART 4:
f-Strings

Introduced in Python 3.6.

Recommended modern approach.


Syntax:

f"Text {variable}"


Advantages:

- Easy to read.
- Supports expressions.
- Supports functions.
- Supports formatting.


Example:

f"Total = {price * quantity}"


-----------------------------------------------------------

Important Notes:

- f-strings are preferred in modern Python.
- Choose formatting method based on readability.
- String formatting is used everywhere:
    - Reports
    - User messages
    - Logging
    - Applications


"""



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


# Format specifiers:

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


# Multiple variables are placed inside a tuple


print(
    "My name is %s and I am %d years old."
    % (name, age)
)




###########################################################
# Formatting Float Numbers with %
###########################################################


price = 15.6789



# %.2f:
# Show two digits after decimal point


print("Price = %.2f" % price)



# %.1f:
# Show one digit after decimal point


print("Price = %.1f" % price)




###########################################################
# 3. String format() Method
###########################################################


# Another way to format strings
# using format()


name = "Sara"

age = 20



print(
    "My name is {} and I am {} years old."
    .format(name, age)
)




###########################################################
# Using Positions with format()
###########################################################


print(
    "My name is {0} and I am {1} years old."
    .format(name, age)
)



print(
    "I am {1} years old and my name is {0}."
    .format(name, age)
)




###########################################################
# Using Names with format()
###########################################################


print(
    "My name is {n} and I am {a} years old."
    .format(n=name, a=age)
)




###########################################################
# Formatting Numbers using format()
###########################################################


number = 1234.56789



# Show 2 decimal places

print(
    "Number = {:.2f}".format(number)
)




###########################################################
# 4. f-Strings (Modern Method)
###########################################################


# Introduced in Python 3.6
# Recommended formatting method today.


name = "Sara"

age = 22



print(
    f"My name is {name} and I am {age} years old."
)




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

print(
    "My name is " 
    + name 
    + " and I am " 
    + str(age)
)



# % formatting

print(
    "My name is %s and I am %d"
    % (name, age)
)



# format()

print(
    "My name is {} and I am {}"
    .format(name, age)
)



# f-string

print(
    f"My name is {name} and I am {age}"
)




###########################################################
# Practice
###########################################################


"""
Create variables:

student = "Sara"
course = "Python"
hours = 50


Print:

Sara is taking Python course for 50 hours.


Use:

1. Concatenation

2. % formatting

3. format()

4. f-string


"""