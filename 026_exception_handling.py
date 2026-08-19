###########################################################
# Exception Handling in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand what an exception is.
- Understand why exceptions happen.
- Learn how to use try and except.
- Learn how to handle specific exceptions.
- Learn how to use multiple except blocks.
- Learn how to use else.
- Learn how to use finally.
- Handle errors caused by user input.
- Handle division by zero.
- Understand the difference between syntax errors and exceptions.
- Learn how to use raise.


Topics Covered:

PART 1:
What is an Exception?

PART 2:
Basic try / except

PART 3:
ValueError

PART 4:
ZeroDivisionError

PART 5:
Multiple Exceptions

PART 6:
else

PART 7:
finally

PART 8:
try / except with User Input

PART 9:
Checking List Index Errors

PART 10:
Dictionary Key Errors

PART 11:
Combining Exception Handling with Functions

PART 12:
raise Statement

PART 13:
Mini Project

PART 14:
Practice Exercises
"""


# ===========================================================
# PART 1: What is an Exception?
# ===========================================================


"""
An exception is an error that happens while the program
is running.

For example:

number = int("hello")

Python cannot convert "hello" into an integer,
so a ValueError occurs.

Without exception handling, the program stops.
"""


# -----------------------------------------------------------
# Example:
# This code will cause a ValueError.
# It is commented out so the rest of the file can run.
# -----------------------------------------------------------


# number = int("hello")



# ===========================================================
# PART 2: Basic try / except
# ===========================================================


"""
try:
    Code that may cause an error

except:
    Code that runs if an error happens
"""


try:

    number = int(input("Enter a number: "))

    print("Your number is:", number)


except:

    print("Something went wrong.")



# ===========================================================
# PART 3: ValueError
# ===========================================================


"""
ValueError happens when a function receives
a value of the correct type but an inappropriate value.

A common example is converting text to a number.
"""


try:

    number = int(input("Enter an integer: "))

    print("Number:", number)


except ValueError:

    print("Please enter a valid integer.")



# ===========================================================
# PART 4: ZeroDivisionError
# ===========================================================


"""
ZeroDivisionError happens when we try to divide
a number by zero.
"""


try:

    num1 = int(input("Enter first number: "))

    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)


except ZeroDivisionError:

    print("You cannot divide by zero.")



# ===========================================================
# PART 5: Multiple Exceptions
# ===========================================================


"""
A program can have more than one possible exception.

We can use multiple except blocks.
"""


try:

    num1 = int(input("Enter first number: "))

    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)


except ValueError:

    print("Please enter numbers only.")


except ZeroDivisionError:

    print("You cannot divide by zero.")



# ===========================================================
# PART 6: else
# ===========================================================


"""
The else block runs only when no exception occurs.

Structure:

try:
    code

except:
    code if error happens

else:
    code if no error happens
"""


try:

    number = int(input("Enter a number: "))


except ValueError:

    print("Invalid number.")


else:

    print("You entered:", number)



# ===========================================================
# PART 7: finally
# ===========================================================


"""
The finally block always runs.

It runs whether an exception happens or not.

Structure:

try:
    code

except:
    code if error happens

finally:
    code that always runs
"""


try:

    number = int(input("Enter a number: "))

    print("Number:", number)


except ValueError:

    print("Invalid input.")


finally:

    print("End of the operation.")



# ===========================================================
# PART 8: try / except with User Input
# ===========================================================


"""
User input is one of the most common places
where exceptions can happen.

For example:

int(input())

The user might enter:

10

which is valid.

But the user might enter:

hello

which causes ValueError.
"""


try:

    age = int(input("Enter your age: "))

    print("Your age is:", age)


except ValueError:

    print("Age must be a number.")



# ===========================================================
# PART 9: List Index Error
# ===========================================================


"""
IndexError happens when we try to access
an index that does not exist.
"""


numbers = [10, 20, 30]


try:

    print(numbers[5])


except IndexError:

    print("This index does not exist.")



# -----------------------------------------------------------
# Correct example
# -----------------------------------------------------------


print(numbers[0])

print(numbers[1])

print(numbers[2])



# ===========================================================
# PART 10: Dictionary Key Error
# ===========================================================


"""
KeyError happens when we try to access
a dictionary key that does not exist.
"""


students = {

    "Sara": 95,

    "Joe": 85,

    "Ali": 90
}


try:

    print(students["Mohammed"])


except KeyError:

    print("Student does not exist.")



# -----------------------------------------------------------
# A safer way using get()
# -----------------------------------------------------------


print(students.get("Sara"))

print(students.get("Mohammed"))


# get() returns None if the key does not exist.



# ===========================================================
# PART 11: Multiple Exceptions in a Function
# ===========================================================


"""
We can use exception handling inside functions.
"""


def divide_numbers(num1, num2):

    try:

        return num1 / num2


    except ZeroDivisionError:

        return "Cannot divide by zero."


result = divide_numbers(10, 2)

print(result)


result = divide_numbers(10, 0)

print(result)



# ===========================================================
# PART 12: Calculator with Exception Handling
# ===========================================================


"""
We can combine:

- Functions
- if statements
- user input
- exception handling

to create a safer calculator.
"""


def calculator(num1, operator, num2):

    if operator == "+":

        return num1 + num2

    elif operator == "-":

        return num1 - num2

    elif operator == "*":

        return num1 * num2

    elif operator == "/":

        if num2 == 0:

            return "Cannot divide by zero."

        return num1 / num2

    else:

        return "Invalid operator."


try:

    num1 = float(input("Enter first number: "))

    operator = input("Enter operation (+, -, *, /): ")

    num2 = float(input("Enter second number: "))

    result = calculator(num1, operator, num2)

    print("Result:", result)


except ValueError:

    print("Please enter valid numbers.")



# ===========================================================
# PART 13: raise Statement
# ===========================================================


"""
raise allows us to create an exception manually.

It is useful when we want to stop the program
when a specific condition is not valid.
"""


age = 15


if age < 18:

    raise ValueError("Age must be 18 or above.")


# The code below will not run because the exception
# above stops the program.

# print("Accepted")



# ===========================================================
# PART 14: raise with try / except
# ===========================================================


"""
We can use raise inside try / except
to handle our own validation rules.
"""


try:

    age = int(input("Enter your age: "))

    if age < 0:

        raise ValueError("Age cannot be negative.")

    print("Age:", age)


except ValueError as error:

    print("Error:", error)



# ===========================================================
# PART 15: Mini Project - Safe Number Input
# ===========================================================


"""
Mini Project:

Create a program that asks the user
to enter a number.

The program should:

1. Ask the user for a number.
2. Check if the input is valid.
3. Print the number.
4. Handle invalid input.
"""


try:

    number = float(input("Enter a number: "))

    print("You entered:", number)


except ValueError:

    print("Invalid input. Please enter a number.")



# ===========================================================
# PART 16: Mini Project - Student Information
# ===========================================================


"""
Mini Project:

Create a program that asks for:

- Student name
- Student age
- Student mark

The program should handle invalid numeric input.
"""


try:

    name = input("Enter student name: ")

    age = int(input("Enter student age: "))

    mark = float(input("Enter student mark: "))

    print()
    print("Student Information")
    print("-------------------")
    print("Name:", name)
    print("Age:", age)
    print("Mark:", mark)


except ValueError:

    print("Age and mark must be numbers.")



# ===========================================================
# PART 17: Complete Example
# ===========================================================


"""
This example combines:

- while loop
- try / except
- input
- if statement
- break

The program keeps asking the user for a number
until a valid number is entered.
"""


while True:

    try:

        number = int(input("Enter an integer: "))

        print("Valid number:", number)

        break


    except ValueError:

        print("Invalid input. Try again.")



# ===========================================================
# PART 18: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Ask the user to enter an integer.
#
# If the user enters invalid data,
# print:
#
# "Please enter an integer."


# -----------------------------------------------------------
# Exercise 2:
#
# Ask the user for two numbers.
#
# Divide the first number by the second number.
#
# Handle:
#
# - ValueError
# - ZeroDivisionError
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 3:
#
# Create a list:
#
# numbers = [10, 20, 30]
#
# Ask the user to enter an index.
#
# Print the value at that index.
#
# Handle IndexError.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 4:
#
# Create a dictionary:
#
# students = {
#     "Sara": 95,
#     "Joe": 85,
#     "Ali": 90
# }
#
# Ask the user for a student name.
#
# Print the student's mark.
#
# Handle KeyError.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 5:
#
# Create a function called safe_divide().
#
# The function should receive two numbers
# and return their division.
#
# Handle division by zero.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 6:
#
# Ask the user to enter their age.
#
# If the age is negative:
#
# raise ValueError
#
# Handle the error using try / except.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 7:
#
# Create a program that keeps asking the user
# to enter a number until they enter a valid number.
#
# Use:
#
# while
# try
# except
# break
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


"""
Exception Handling Summary:

We learned:

- What an exception is.
- try
- except
- ValueError
- ZeroDivisionError
- IndexError
- KeyError
- Multiple except blocks
- else
- finally
- raise
- Exception handling with functions.
- Exception handling with loops.
- Exception handling with user input.

Important:

Exception handling does not mean ignoring errors.

It means handling expected problems
and allowing the program to respond properly.
"""


###########################################################
# END OF EXCEPTION HANDLING
###########################################################