###########################################################
# Modules and Imports in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand what a module is.
- Learn how to import modules.
- Learn different ways to import.
- Learn how to use functions from modules.
- Learn how to import specific functions.
- Learn how to use aliases.
- Learn how to create and import our own module.
- Understand the difference between a module and a package.
- Practice using common Python modules.


Topics Covered:

PART 1:
What is a Module?

PART 2:
Import a Module

PART 3:
Using Functions from a Module

PART 4:
Import Specific Functions

PART 5:
Using Aliases

PART 6:
The math Module

PART 7:
The random Module

PART 8:
The datetime Module

PART 9:
The os Module

PART 10:
Creating Our Own Module

PART 11:
Importing Our Own Module

PART 12:
Different Import Styles

PART 13:
__name__ == "__main__"

PART 14:
Practice Exercises
"""


# ===========================================================
# PART 1: What is a Module?
# ===========================================================


"""
A module is a Python file that contains code.

A module can contain:

- Variables
- Functions
- Classes

We can import a module and use its code
in another Python file.

For example:

math.py
random.py
datetime.py

are modules available in Python.

Benefits of modules:

- Organize code.
- Reuse code.
- Make programs easier to maintain.
- Avoid repeating the same code.
"""


# ===========================================================
# PART 2: Import a Module
# ===========================================================


"""
We use the import keyword to import a module.

Syntax:

import module_name
"""


import math


print(math.pi)


# ===========================================================
# PART 3: Using Functions from a Module
# ===========================================================


"""
After importing a module,
we can access its functions using:

module_name.function_name()
"""


number = 25


print(math.sqrt(number))


print(math.pow(2, 3))


# sqrt()
# Returns the square root.


# pow()
# Raises a number to a power.



# ===========================================================
# PART 4: Constants from a Module
# ===========================================================


print("Pi:", math.pi)

print("Euler's number:", math.e)



# ===========================================================
# PART 5: Import Specific Functions
# ===========================================================


"""
Instead of importing the entire module,
we can import a specific function.

Syntax:

from module import function
"""


from math import sqrt


print(sqrt(49))


# We can now use sqrt()
# without writing math.sqrt()



# ===========================================================
# PART 6: Import Multiple Functions
# ===========================================================


from math import sqrt, pow


print(sqrt(64))

print(pow(2, 4))



# ===========================================================
# PART 7: Using an Alias
# ===========================================================


"""
An alias gives a module another name.

Syntax:

import module as alias
"""


import math as m


print(m.sqrt(100))

print(m.pi)



# ===========================================================
# PART 8: The random Module
# ===========================================================


"""
The random module is used to generate
random values.
"""


import random


# Random integer between 1 and 10.


number = random.randint(1, 10)


print("Random number:", number)



# ===========================================================
# PART 9: random.choice()
# ===========================================================


"""
choice() selects one random item
from a sequence.
"""


names = [
    "Sara",
    "Joe",
    "Ali",
    "Mohammed"
]


random_name = random.choice(names)


print("Random student:", random_name)



# ===========================================================
# PART 10: random.shuffle()
# ===========================================================


"""
shuffle() changes the order of the items
in a list randomly.
"""


students = [
    "Sara",
    "Joe",
    "Ali",
    "Mohammed"
]


random.shuffle(students)


print(students)



# ===========================================================
# PART 11: The datetime Module
# ===========================================================


"""
datetime is used to work with:

- Dates
- Times
- Current date
- Current time
"""


import datetime


today = datetime.date.today()


print("Today's date:", today)



# Current date and time.


now = datetime.datetime.now()


print("Current date and time:", now)



# ===========================================================
# PART 12: Import Specific datetime
# ===========================================================


from datetime import date


today = date.today()


print("Today:", today)



# ===========================================================
# PART 13: The os Module
# ===========================================================


"""
The os module allows Python
to interact with the operating system.
"""


import os


# Get the current working directory.


current_directory = os.getcwd()


print("Current directory:")

print(current_directory)



# ===========================================================
# PART 14: Check if a File Exists
# ===========================================================


filename = "students.txt"


if os.path.exists(filename):

    print("File exists.")


else:

    print("File does not exist.")



# ===========================================================
# PART 15: List Files and Folders
# ===========================================================


"""
os.listdir() returns the files and folders
inside a directory.
"""


files = os.listdir()


print("Files and folders:")

print(files)



# ===========================================================
# PART 16: Create a Folder
# ===========================================================


"""
os.mkdir() creates a new folder.

The example is commented so that
the folder is not created every time
the program runs.
"""


# folder_name = "my_folder"
#
# if not os.path.exists(folder_name):
#
#     os.mkdir(folder_name)
#
#     print("Folder created.")



# ===========================================================
# PART 17: Different Import Styles
# ===========================================================


"""
There are several ways to import modules.

1. import module

2. import module as alias

3. from module import function

4. from module import function1, function2
"""


# Example 1:


import math


print(math.sqrt(16))


# Example 2:


import math as m


print(m.sqrt(16))


# Example 3:


from math import sqrt


print(sqrt(16))


# Example 4:


from math import sqrt, floor


print(sqrt(16))

print(floor(4.8))



# ===========================================================
# PART 18: Creating Our Own Module
# ===========================================================


"""
We can create our own module.

For example, create a file:

my_functions.py

Inside it:

def add(a, b):

    return a + b


def subtract(a, b):

    return a - b


Then we can import it into another Python file.

Example:

import my_functions

result = my_functions.add(10, 5)

print(result)
"""


# ===========================================================
# PART 19: Example of Our Own Module
# ===========================================================


"""
Suppose we have a file called:

calculator.py

Inside calculator.py:

def add(a, b):

    return a + b


def subtract(a, b):

    return a - b


def multiply(a, b):

    return a * b


Then another file can use:

import calculator


print(calculator.add(10, 5))
"""


# The code above is an explanation only.
# The module must actually exist before importing it.



# ===========================================================
# PART 20: __name__
# ===========================================================


"""
Every Python file has a special variable:

__name__

When a file is run directly,
Python sets:

__name__ = "__main__"


This allows us to check whether
a file is being run directly
or imported into another file.
"""


def display():

    print("Hello from the module.")


if __name__ == "__main__":

    display()


# This is very common when creating modules.



# ===========================================================
# PART 21: Mini Example
# ===========================================================


"""
Imagine we have:

calculator.py
"""


def add(a, b):

    return a + b


def subtract(a, b):

    return a - b


def multiply(a, b):

    return a * b


def divide(a, b):

    if b == 0:

        return "Cannot divide by zero."

    return a / b


print(add(10, 5))

print(subtract(10, 5))

print(multiply(10, 5))

print(divide(10, 5))



# ===========================================================
# PART 22: Practice with random
# ===========================================================


"""
Generate a random number between 1 and 100.
"""


random_number = random.randint(1, 100)


print("Random number:", random_number)



# ===========================================================
# PART 23: Mini Project - Random Student
# ===========================================================


"""
Create a program that randomly selects
one student from a list.
"""


students = [
    "Sara",
    "Joe",
    "Ali",
    "Mohammed",
    "Lina"
]


selected_student = random.choice(students)


print("Today's student is:", selected_student)



# ===========================================================
# PART 24: Mini Project - Random Password
# ===========================================================


"""
Generate a simple random password.

This is only a learning example.
"""


characters = [
    "A",
    "B",
    "C",
    "1",
    "2",
    "3",
    "@",
    "#"
]


password = ""


for i in range(6):

    password += random.choice(characters)


print("Generated password:", password)



# ===========================================================
# PART 25: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Import the math module.
#
# Ask the user for a number.
#
# Print:
#
# - Square root
# - Power of 2
# - Absolute value
# -----------------------------------------------------------


# Exercise 2:
#
# Import the random module.
#
# Generate a random number
# between 1 and 50.
# -----------------------------------------------------------


# Exercise 3:
#
# Create a list of names:
#
# Sara
# Joe
# Ali
# Mohammed
#
# Use random.choice()
# to select a random student.
# -----------------------------------------------------------


# Exercise 4:
#
# Use datetime
# to print today's date.
# -----------------------------------------------------------


# Exercise 5:
#
# Use os.getcwd()
# to print the current directory.
# -----------------------------------------------------------


# Exercise 6:
#
# Use os.listdir()
# to print all files and folders
# in the current directory.
# -----------------------------------------------------------


# Exercise 7:
#
# Create a file called:
#
# calculator.py
#
# Add these functions:
#
# add()
# subtract()
# multiply()
# divide()
#
# Then import calculator.py
# into another Python file.
# -----------------------------------------------------------


# Exercise 8:
#
# Create a module called:
#
# student.py
#
# Add a function:
#
# display_student(name, age)
#
# Then import the module
# and call the function.
# -----------------------------------------------------------


# Exercise 9:
#
# Create a module called:
#
# numbers.py
#
# Add:
#
# is_even(number)
#
# The function should return True
# if the number is even.
# -----------------------------------------------------------


# Exercise 10:
#
# Create a simple random game.
#
# The computer generates
# a random number between 1 and 10.
#
# The user tries to guess the number.
#
# Print:
#
# "Correct"
#
# or:
#
# "Wrong"
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


"""
Modules and Imports Summary:

We learned:

- What a module is.
- import
- from ... import ...
- import ... as ...
- math
- random
- datetime
- os
- os.getcwd()
- os.listdir()
- os.path.exists()
- Creating our own modules.
- Importing our own modules.
- __name__
- __main__


Important:

Modules help us organize and reuse code.

Instead of putting everything in one file,
we can divide our program into multiple files
and import the code we need.
"""


###########################################################
# END OF MODULES AND IMPORTS
###########################################################