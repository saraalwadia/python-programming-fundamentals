###########################################################
# Practice Exercises - If, Dictionary & Loops
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Practice using if / elif / else.
- Practice using dictionaries.
- Practice using for loops.
- Practice using break.
- Practice using modulus operator %.
- Practice using lists.
- Solve simple programming problems.
- Combine multiple Python concepts in one problem.


Topics Covered:

PART 1:
Leap Year Check

- Use the modulus (%) operator.
- Understand divisibility.
- Practice using multiple conditions with and / or.


PART 2:
Months Dictionary

- Store data using key-value pairs.
- Use user input to access dictionary values.
- Practice dictionary keys and values.
- Practice using if to validate input.


PART 3:
Numbers Divisible by 7 and 5

- Use a for loop.
- Use if inside a loop.
- Use and to combine conditions.
- Store results in a list.


PART 4:
Search Using a Loop

- Search for a specific value.
- Use break to stop the loop.


PART 5:
Even and Odd Numbers

- Use the modulus (%) operator.
- Combine if with a for loop.


Important Notes:

- range() does not include the ending value.
- Dictionary keys must be unique.
- % returns the remainder.
- break stops the loop completely.
- Always validate user input when necessary.
"""


# ===========================================================
# PART 1: Leap Year or Normal Year
# ===========================================================


year = int(input("Enter year: "))


# A year is a leap year if:
#
# 1. It is divisible by 4
# AND
# 2. It is NOT divisible by 100
#
# OR
#
# 3. It is divisible by 400


if year % 400 == 0:

    print("Leap Year")


elif year % 100 == 0:

    print("Normal Year")


elif year % 4 == 0:

    print("Leap Year")


else:

    print("Normal Year")


# Examples:
#
# 2024 -> Leap Year
# 2023 -> Normal Year
# 1900 -> Normal Year
# 2000 -> Leap Year


# ===========================================================
# PART 2: Find Month Name Using Dictionary
# ===========================================================


months = {

    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec"
}


number = int(input("Enter Month Number: "))


# Check if the month number exists
# in the dictionary.

if number in months:

    print(months[number])

else:

    print("Invalid month number")


# -----------------------------------------------------------
# Another way using a for loop
# -----------------------------------------------------------


number = int(input("Enter Month Number: "))


for month_number in months:

    if month_number == number:

        print(months[month_number])

        break

else:

    print("Invalid month number")


# break:
# Stops the loop completely after finding the value.


# ===========================================================
# PART 3: Numbers Divisible by 7 and 5
# ===========================================================


numbers = []


# Check numbers between 1500 and 2700.
#
# The ending value 2701 is used because
# range() does not include the ending value.


for x in range(1500, 2701):

    if x % 7 == 0 and x % 5 == 0:

        numbers.append(x)


print(numbers)


# ===========================================================
# PART 4: Print Numbers Divisible by 7 and 5
# ===========================================================


for x in range(1500, 2701):

    if x % 7 == 0 and x % 5 == 0:

        print(x)


# ===========================================================
# PART 5: Store Results as Strings
# ===========================================================


numbers = []


for x in range(1500, 2701):

    if x % 7 == 0 and x % 5 == 0:

        numbers.append(str(x))


# join() combines all strings using ","

print(",".join(numbers))


# Example output:
#
# 1540,1575,1610,1645,...


# ===========================================================
# PART 6: Even Numbers
# ===========================================================


# Print even numbers from 1 to 20.


for number in range(1, 21):

    if number % 2 == 0:

        print(number)


# ===========================================================
# PART 7: Odd Numbers
# ===========================================================


# Print odd numbers from 1 to 20.


for number in range(1, 21):

    if number % 2 != 0:

        print(number)


# ===========================================================
# PART 8: Search for a Number
# ===========================================================


numbers = [
    10,
    20,
    30,
    40,
    50
]


search_number = int(input("Enter number to search: "))


found = False


for number in numbers:

    if number == search_number:

        found = True

        break


if found:

    print("Number found")

else:

    print("Number not found")


# ===========================================================
# PART 9: Find the First Even Number
# ===========================================================


numbers = [
    11,
    15,
    17,
    21,
    24,
    30
]


for number in numbers:

    if number % 2 == 0:

        print("First even number:", number)

        break


# ===========================================================
# PART 10: Practice Exercises
# ===========================================================


# -----------------------------------------------------------
# Exercise 1:
#
# Ask the user to enter a number.
# Print whether the number is:
#
# Positive
# Negative
# Zero
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 2:
#
# Ask the user to enter a number.
# Print whether the number is:
#
# Even
# Odd
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 3:
#
# Create a dictionary containing 5 students
# and their marks.
#
# Ask the user to enter a student's name.
# Print the student's mark.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 4:
#
# Print all numbers from 1 to 100
# that are divisible by 3.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 5:
#
# Print all numbers from 1 to 100
# that are divisible by both 3 and 5.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 6:
#
# Create a list of numbers.
#
# Search for a specific number.
#
# If the number is found:
# print "Found"
# and stop the loop using break.
#
# Otherwise:
# print "Not Found"
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 7:
#
# Create a dictionary containing months.
#
# Ask the user to enter a month number.
#
# Print the month name if it exists.
# Otherwise print "Invalid month".
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


# if / elif / else
# -> Used to make decisions.
#
# dictionary
# -> Stores data as key-value pairs.
#
# for
# -> Repeats code over a sequence.
#
# range()
# -> Generates a sequence of numbers.
#
# %
# -> Returns the remainder.
#
# and
# -> Both conditions must be True.
#
# break
# -> Stops the loop completely.
#
# list.append()
# -> Adds an item to a list.
#
# join()
# -> Combines strings into one string.
#
# ===========================================================
# END OF PRACTICE
# ===========================================================