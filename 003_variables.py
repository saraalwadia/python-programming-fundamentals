# ===========================================================
# Python Data Types & Variables
# ===========================================================


"""
Teaching Notes:

Lesson Objectives:
- Understand Python built-in data types.
- Learn how to check data types using type().
- Understand variables and how Python stores values.
- Learn variable naming conventions.
- Understand strings and multi-line strings.

Topics Covered:

PART 1: Introduction to Data Types
- Every value in Python has a specific data type.
- Data types define what operations can be performed.
- Python is dynamically typed.

PART 2: Basic Data Types:
- int      -> Whole numbers
- float    -> Decimal numbers
- str      -> Text
- bool     -> True or False

PART 3: Collection Data Types:
- list       -> Ordered and mutable collection
- tuple      -> Ordered and immutable collection
- set        -> Collection of unique values
- dictionary -> Key-value pairs

PART 4: Special Data Types:
- NoneType represents the absence of a value.
- Functions are objects in Python.

PART 5: Variables:
- Variables are used to store values.
- Python does not require declaring variable types.
- Variable type is determined automatically.
- Variable names are case-sensitive.

PART 6: Multi-line Strings:
- Triple quotes can create multi-line strings.

PART 7: Variable Naming Conventions:
- Use meaningful names.
- Use snake_case for multiple words.
- Avoid invalid variable names.

Important Notes:
- type() shows the data type of a value.
- 1 and "1" are different values.
- Variables store values, not the value name.
- Python variables do not have fixed types.

Common Mistakes:
- Confusing print(name) with print("name").
- Forgetting quotation marks for strings.
- Using spaces in variable names.
"""


# ===========================================================
# PART 1: Basic Data Types
# ===========================================================


# Integer (int)
# Stores whole numbers

print(type(1))


# Float
# Stores decimal numbers

print(type(1.0))


# String (str)
# Stores text values

print(type("1"))


# Boolean (bool)
# Stores True or False values

print(type(True))


# Negative numbers

print(type(-10))

print(type(-10.0))



# ===========================================================
# PART 2: Collection Data Types
# ===========================================================


# Tuple
# Ordered and immutable collection

print(type((1, 5, 3)))



# List
# Ordered and mutable collection

print(type([1, 5, 3, "S", False]))



# Dictionary
# Stores data as key-value pairs

print(type({"name": "John", "age": 30}))



# Set
# Stores unique values

print(type({1, 2, 3, 0}))



# ===========================================================
# PART 3: Special Data Types
# ===========================================================


# None represents no value

print(type(None))


# Functions are objects in Python

print(type(print))


# Type objects are also objects

print(type(type(1)))



# ===========================================================
# PART 4: Boolean Expressions
# ===========================================================


# Comparison operations return True or False

print(type(2 == 2))

print(2 == 2)



# ===========================================================
# PART 5: Variables
# ===========================================================


# A variable stores a value

name = "Sara"


print(name)



# "name" is a string, not the variable

print("name")



# Variable names are case-sensitive

Name = "Python"


print(name)

print(Name)



# ===========================================================
# PART 6: Multi-line Strings
# ===========================================================


# Triple quotes are used for multi-line strings

info = """
Name: Sara
Specialty: IT
"""


print(info)



# ===========================================================
# PART 7: Variable Naming Conventions
# ===========================================================


# Single word variable

name = "Sara"



# Multiple words using snake_case

full_name = "Sara Alwadia"



# Multiple words using camelCase

fullName = "Sara Alwadia"



# ===========================================================
# Practice
# ===========================================================


# 1. Create variables:
#    name
#    age
#    is_student


# 2. Print their values and types.


# 3. Create:
#    - A list of your favorite programming languages
#    - A dictionary containing student information


# 4. Check the type of each variable.