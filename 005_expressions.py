# ===========================================================
# Lesson 05
# Expressions & Arithmetic Operators
# ===========================================================


"""
Teaching Notes:

Lesson Objectives:
- Understand what expressions are in Python.
- Learn arithmetic operators.
- Perform mathematical calculations using variables.
- Understand the order of operations.

Topics Covered:

PART 1: What are Expressions?
- An expression is a combination of values, variables, and operators.
- Python evaluates expressions and returns a result.

Examples:
    5 + 3
    price * quantity

PART 2: Arithmetic Operators:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Exponentiation (**)
- Floor Division (//)
- Modulus (%)

PART 3: Using Variables in Expressions:
- Variables can be used instead of writing values directly.
- Expressions make programs dynamic and reusable.

PART 4: Order of Operations:
Python follows mathematical rules:

1. Parentheses ()
2. Exponent **
3. Multiplication *
4. Division /
5. Floor Division //
6. Modulus %
7. Addition +
8. Subtraction -

Important Notes:
- Division (/) always returns a float.
- Floor division (//) removes the decimal part.
- Modulus (%) gives the remainder.
- Parentheses can change the calculation order.

Common Mistakes:
- Confusing / with //.
- Forgetting operator precedence.
- Using % as percentage (in this lesson it means remainder).


"""


# ===========================================================
# PART 1: Basic Arithmetic Operations
# ===========================================================


# Create two number variables

num1 = 10
num2 = 5



# ===========================================================
# Addition (+)
# ===========================================================

# Adds two values together

result = num1 + num2

print("Addition =", result)



# ===========================================================
# Subtraction (-)
# ===========================================================

# Subtracts the second value from the first value

result = num1 - num2

print("Subtraction =", result)



# ===========================================================
# Multiplication (*)
# ===========================================================

# Multiplies two values

result = num1 * num2

print("Multiplication =", result)



# ===========================================================
# Division (/)
# ===========================================================

# Divides one value by another
# Result is always float

result = num1 / num2

print("Division =", result)



# ===========================================================
# PART 2: Advanced Arithmetic Operators
# ===========================================================



# ===========================================================
# Exponentiation (**)
# ===========================================================

# Used to calculate powers

result = num1 ** 2

print("Power =", result)


# Example:
# 10² = 10 * 10 = 100



# ===========================================================
# Floor Division (//)
# ===========================================================

# Returns only the integer part of division

result = 10 // 3

print("Floor Division =", result)


# Normal division:
# 10 / 3 = 3.3333


# Floor division:
# 10 // 3 = 3



# ===========================================================
# Modulus (%)
# ===========================================================

# Returns the remainder after division

result = 10 % 3

print("Remainder =", result)


# Example:
# 10 / 3
# 3 * 3 = 9
# Remainder = 1



# ===========================================================
# PART 3: Expressions Using Variables
# ===========================================================


price = 50
quantity = 3


total = price * quantity


print("Total price =", total)



# ===========================================================
# PART 4: Order of Operations
# ===========================================================


# Python follows mathematical precedence:

# 1. Parentheses ()
# 2. Exponent **
# 3. Multiplication, Division, Floor Division, Modulus
# 4. Addition and Subtraction



result = 5 + 3 * 2


print(result)


# Explanation:
#
# 3 * 2 = 6
# 5 + 6 = 11



result = (5 + 3) * 2


print(result)


# Explanation:
#
# Parentheses first:
# 5 + 3 = 8
#
# Then:
# 8 * 2 = 16



# ===========================================================
# Practice
# ===========================================================


# 1. Create two variables:
#    length = 10
#    width = 5
#
#    Calculate rectangle area.


# 2. Create:
#    total_price = 100
#    discount = 20
#
#    Calculate the final price.


# 3. Try:
#    17 / 5
#    17 // 5
#    17 % 5
#
#    Explain the difference.