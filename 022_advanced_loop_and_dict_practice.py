###########################################################
# Advanced If Statement & Dictionary Practice
###########################################################


"""
Teaching Notes:

Lesson Objectives:
- Practice using dictionaries.
- Understand if, elif, else with different conditions.
- Learn how to combine conditions using and / or.
- Learn nested if statements.
- Understand the modulus (%) operator.
- Solve simple decision-making problems.


Topics Covered:

PART 1: Dictionary
- Store data using key-value pairs.
- Keys must be unique.
- If a key is repeated, the last value replaces the previous one.


PART 2: If - Elif - Else
- Used to make decisions.
- Python checks conditions from top to bottom.
- The first True condition will execute.


PART 3: Logical Operators

and:
- Both conditions must be True.

or:
- At least one condition must be True.


PART 4: Nested If
- An if statement inside another if statement.
- Used when we have dependent conditions.


PART 5: Modulus Operator %
- Used to find the remainder.
- Useful for checking even and odd numbers.


Important Notes:
- Order of conditions matters.
- Put the most specific conditions first.
- Avoid unreachable conditions.
- Use indentation correctly.
- Be careful when combining conditions with and / or.
"""


# ===========================================================
# PART 1: Dictionary
# ===========================================================


# A dictionary stores data as:
#
# key : value


hobbies = {

    "sara": "football",

    "adam": "basketball",

    "Jo": "swimming",

    # Duplicate keys are not allowed.
    #
    # If the same key is used more than once,
    # the last value replaces the previous value.

    "Jo": "english"
}


print(hobbies)


# The output will be:
#
# {'sara': 'football', 'adam': 'basketball', 'Jo': 'english'}


# Another dictionary example:

people = {

    1: "Sara",

    2: "Mohammed"
}


print(people)


# ===========================================================
# PART 2: Positive, Negative or Zero
# ===========================================================


# Ask the user to enter a number.

number = float(input("Enter the number: "))


if number > 0:

    print("Positive")


elif number < 0:

    print("Negative")


else:

    print("Zero")


# Example:
#
# Enter the number: 10
# Positive
#
# Enter the number: -5
# Negative
#
# Enter the number: 0
# Zero


# ===========================================================
# PART 3: Simple Menu
# ===========================================================


# Ask the user to choose an item from a menu.

choice = int(input("Enter your choice: "))


if choice == 1:

    print("Coffee")


elif choice == 2:

    print("Tea")


elif choice == 3:

    print("Water")


else:

    print("Sorry, I don't know that")


# Example:
#
# Enter your choice: 1
# Coffee
#
# Enter your choice: 2
# Tea
#
# Enter your choice: 5
# Sorry, I don't know that


# ===========================================================
# PART 4: Certificate Grade
# ===========================================================


# Ask the user to enter their average.

av = float(input("Enter your average: "))


if av >= 90:

    print("Excellent")


elif av >= 80:

    print("Very good")


elif av >= 70:

    print("Good")


elif av >= 60:

    print("Fairly Good")


else:

    print("Not so good")


# Python checks the conditions from top to bottom.
#
# Once a condition is True,
# the remaining elif/else blocks are skipped.


# ===========================================================
# PART 5: Logical Operators (and / or)
# ===========================================================


x = int(input("Enter integer number: "))


# -----------------------------------------------------------
# AND
# -----------------------------------------------------------
#
# Both conditions must be True.
#
# Check if the number is between 0 and 20.

if x >= 0 and x <= 20:

    print("The number is between 0 and 20.")


else:

    print("The number is outside the range.")


# -----------------------------------------------------------
# OR
# -----------------------------------------------------------
#
# At least one condition must be True.
#
# Check if the number is outside the range 0 to 20.

if x < 0 or x > 20:

    print("The number is outside the range.")


else:

    print("The number is between 0 and 20.")


# Example:
#
# x = 10
#
# x >= 0  -> True
# x <= 20 -> True
#
# AND -> True
#
#
# x = 25
#
# x < 0  -> False
# x > 20 -> True
#
# OR -> True


# ===========================================================
# PART 6: Even or Odd
# ===========================================================


# The modulus operator % returns the remainder
# after division.


y = int(input("Enter integer number: "))


# Even numbers have a remainder of 0
# when divided by 2.

if y % 2 == 0:

    print("Even")


else:

    print("Odd")


# Example:
#
# 10 % 2 = 0 -> Even
# 7 % 2 = 1  -> Odd


# ===========================================================
# PART 7: Nested If Statement
# ===========================================================


# A nested if is an if statement
# inside another if statement.


gender = input("Enter gender: ").lower()

age = int(input("Enter your age: "))


if gender == "boy":

    # The second if is checked only
    # if the gender is "boy".

    if age > 0 and age < 18:

        print("Boy and child")


    elif age >= 18:

        print("Boy and adult")


    else:

        print("Wrong age")


elif gender == "girl":

    # The second if is checked only
    # if the gender is "girl".

    if age > 0 and age < 18:

        print("Girl and child")


    elif age >= 18:

        print("Girl and adult")


    else:

        print("Wrong age")


else:

    print("Unknown gender")


# Example:
#
# Enter gender: boy
# Enter your age: 15
# Boy and child
#
#
# Enter gender: girl
# Enter your age: 25
# Girl and adult
#
#
# Enter gender: cat
# Enter your age: 10
# Unknown gender


# ===========================================================
# PART 8: Combining Multiple Conditions
# ===========================================================


# We can combine multiple conditions
# using and / or.


age = int(input("Enter your age: "))


if age >= 18 and age <= 65:

    print("You are an adult.")


elif age > 65:

    print("You are older than 65.")


elif age > 0:

    print("You are under 18.")


else:

    print("Invalid age.")


# ===========================================================
# PART 9: More Specific Conditions First
# ===========================================================


# The order of conditions matters.


grade = float(input("Enter your grade: "))


if grade >= 90:

    print("Excellent")


elif grade >= 80:

    print("Very Good")


elif grade >= 70:

    print("Good")


elif grade >= 60:

    print("Pass")


else:

    print("Fail")


# Why does the order matter?
#
# If grade = 95:
#
# grade >= 90 -> True
#
# Python stops here.
#
# It does not check the remaining conditions.


# ===========================================================
# PART 10: Invalid / Valid Range
# ===========================================================


gpa = float(input("Enter your GPA: "))


if gpa < 0 or gpa > 100:

    print("Invalid value")


elif gpa >= 90:

    print("Excellent")


elif gpa >= 80:

    print("Very Good")


elif gpa >= 70:

    print("Good")


elif gpa >= 60:

    print("Pass")


else:

    print("Fail")


# The first condition checks whether
# the value is outside the valid range.


# ===========================================================
# PART 11: Common Mistake - = vs ==
# ===========================================================


# "=" is used for assignment.
#
# Example:

number = 10


# "==" is used for comparison.
#
# Example:

if number == 10:

    print("The number is 10")


# The following example is WRONG
# because "=" cannot be used for comparison:

# if number = 10:
#     print("The number is 10")

# This causes a SyntaxError.


# ===========================================================
# PART 12: Common Mistake - Wrong OR Condition
# ===========================================================


# Be careful when using OR.


# The following condition is usually NOT
# what we mean when checking if a number
# is between 0 and 20:

# if x >= 0 or x <= 20:
#     print("Between 0 and 20")


# Why?
#
# At least one condition will be True
# for almost every number.
#
# Correct:

if x >= 0 and x <= 20:

    print("Between 0 and 20")


# ===========================================================
# PART 13: Practice
# ===========================================================


# Exercise 1:
#
# Ask the user to enter a number.
# Print whether the number is:
#
# Positive
# Negative
# Zero


# Exercise 2:
#
# Ask the user to enter a number.
# Print whether the number is Even or Odd.


# Exercise 3:
#
# Create a menu:
#
# 1. Coffee
# 2. Tea
# 3. Water
#
# Print the selected drink.


# Exercise 4:
#
# Ask the user to enter their grade.
#
# 90 - 100 -> Excellent
# 80 - 89  -> Very Good
# 70 - 79  -> Good
# 60 - 69  -> Pass
# Below 60 -> Fail


# Exercise 5:
#
# Ask the user to enter their age and gender.
#
# Print whether the person is:
#
# Boy and Child
# Boy and Adult
# Girl and Child
# Girl and Adult
#
# Use a nested if statement.


# ===========================================================
# SUMMARY
# ===========================================================

# Dictionary
# -> Stores data using key-value pairs.
#
# if
# -> Executes code when a condition is True.
#
# elif
# -> Checks another condition if the previous one was False.
#
# else
# -> Executes when all previous conditions are False.
#
# and
# -> Both conditions must be True.
#
# or
# -> At least one condition must be True.
#
# Nested if
# -> An if statement inside another if statement.
#
# %
# -> Returns the remainder after division.
#
# ==
# -> Compares two values.
#
# =
# -> Assigns a value to a variable.
#
# ===========================================================
# END OF ADVANCED IF STATEMENT
# ===========================================================