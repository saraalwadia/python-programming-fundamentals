# ===========================================================
# Type Conversion in Python
# ===========================================================


"""
Teaching Notes:

Lesson Objectives:
- Understand why we need type conversion.
- Learn how to convert strings into numbers.
- Use int() and float().
- Understand the difference between string concatenation
  and mathematical addition.

Prerequisites:
- Variables
- Data Types
- input()
- Arithmetic Operators


Topics Covered:

PART 1: What is Type Conversion?
- Type conversion means changing a value from one data type
  into another data type.

Examples:

String -> Integer
int("10")

String -> Float
float("10.5")

Integer -> String
str(10)


PART 2: input() and Type Conversion
- input() always returns a string.
- To perform calculations, we need to convert the input.

Example:

age = input("Enter age: ")

The result type:
str


Correct:

age = int(input("Enter age: "))


PART 3: int() Conversion
- Converts values into integers.
- Used when working with whole numbers.


PART 4: float() Conversion
- Converts values into decimal numbers.
- Used when we need more accuracy.


PART 5: String vs Number Operations

With strings:

"5" + "3"

Result:
"53"


With numbers:

5 + 3

Result:
8


Important Notes:
- Choose int() for whole numbers.
- Choose float() for decimal values.
- Mathematical operations require numeric data types.

Common Mistakes:
- Forgetting to convert input before calculations.
- Using int() with decimal values.
- Mixing strings and numbers.


"""


# ===========================================================
# PART 1: Convert Input to Integer
# ===========================================================


# input() returns string
# We convert it into integer using int()


number1 = int(input("Enter number 1: "))

number2 = int(input("Enter number 2: "))



# Now we can perform mathematical operations

result = number1 + number2



# Check data types

print(type(number1))

print(type(number2))


# Print result

print("Result =", result)



# ===========================================================
# PART 2: Circle Area Using User Input
# ===========================================================


"""
Task:

Calculate the area of a circle.

Formula:

Area = π * r²

"""


pi = 3.14


# Convert user input into float

radius = float(input("Enter radius: "))



# Calculate radius squared

radius_square = radius ** 2



# Calculate area

circle_area = pi * radius_square



print("Circle Area =", circle_area)



# ===========================================================
# PART 3: Difference Between Strings and Numbers
# ===========================================================


# input() returns strings

num1 = input("Enter number 1: ")

num2 = input("Enter number 2: ")



# ===========================================================
# String Concatenation
# ===========================================================


# + joins strings together

print(num1 + num2)


# Example:
# Input:
# 5
# 3
#
# Output:
# 53



# ===========================================================
# Mathematical Addition
# ===========================================================


# Convert strings into integers

print(int(num1) + int(num2))


# Example:
# Input:
# 5
# 3
#
# Output:
# 8



# ===========================================================
# Using Float Conversion
# ===========================================================


print(float(num1) + float(num2))



# ===========================================================
# Practice
# ===========================================================


"""
Practice Tasks:

1. Ask the user to enter:
   - Age
   - Birth year

   Calculate:
   Current year - birth year


2. Ask the user for:
   - Product price
   - Quantity

   Calculate total price.


3. Ask the user for two numbers:
   Print:
   - Sum
   - Difference
   - Multiplication
   - Division

"""