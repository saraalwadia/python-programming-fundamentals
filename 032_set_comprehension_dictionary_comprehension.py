###########################################################
# Dictionary and Set Comprehension in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand Dictionary Comprehension.
- Understand Set Comprehension.
- Learn how to create dictionaries using comprehension.
- Learn how to create sets using comprehension.
- Use conditions with comprehensions.
- Use if / else with comprehensions.
- Practice working with lists, dictionaries, and sets.
- Understand when to use each type of comprehension.


Topics Covered:

PART 1:
Dictionary Comprehension

PART 2:
Basic Dictionary Comprehension

PART 3:
Dictionary Comprehension with Conditions

PART 4:
Dictionary Comprehension with if / else

PART 5:
Dictionary Comprehension from Two Lists

PART 6:
Working with Dictionaries

PART 7:
Set Comprehension

PART 8:
Set Comprehension with Conditions

PART 9:
Remove Duplicates Using Set Comprehension

PART 10:
List vs Dictionary vs Set Comprehension

PART 11:
Practice Exercises
"""


# ===========================================================
# PART 1: Dictionary Comprehension
# ===========================================================


"""
Dictionary comprehension is a short way
to create a dictionary.

Basic syntax:

{
    key: value
    for item in iterable
}


Example:

numbers = [1, 2, 3]

result = {
    number: number ** 2
    for number in numbers
}
"""


# ===========================================================
# PART 2: Basic Dictionary Comprehension
# ===========================================================


numbers = [1, 2, 3, 4, 5]


squares = {
    number: number ** 2
    for number in numbers
}


print(squares)


# Output:
#
# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25
# }


# ===========================================================
# PART 3: Normal Loop vs Dictionary Comprehension
# ===========================================================


# Normal for loop


numbers = [1, 2, 3, 4, 5]


squares = {}


for number in numbers:

    squares[number] = number ** 2


print(squares)


# Dictionary comprehension


squares = {
    number: number ** 2
    for number in numbers
}


print(squares)


# Both produce the same result.



# ===========================================================
# PART 4: Dictionary Comprehension with range()
# ===========================================================


numbers = range(1, 6)


result = {
    number: number * 10
    for number in numbers
}


print(result)


# ===========================================================
# PART 5: Dictionary Comprehension with Condition
# ===========================================================


"""
We can add an if condition.

Syntax:

{
    key: value
    for item in iterable
    if condition
}
"""


numbers = range(1, 11)


even_numbers = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}


print(even_numbers)


# ===========================================================
# PART 6: Odd Numbers
# ===========================================================


odd_numbers = {
    number: number ** 2
    for number in numbers
    if number % 2 != 0
}


print(odd_numbers)


# ===========================================================
# PART 7: Dictionary Comprehension with if / else
# ===========================================================


"""
We can use if / else to decide
which value should be stored.
"""


numbers = range(1, 6)


result = {
    number: "Even" if number % 2 == 0 else "Odd"
    for number in numbers
}


print(result)


# ===========================================================
# PART 8: Pass and Fail
# ===========================================================


marks = {
    "Sara": 95,
    "Joe": 80,
    "Ali": 45,
    "Mohammed": 70
}


results = {
    name: "Pass" if mark >= 50 else "Fail"
    for name, mark in marks.items()
}


print(results)


# ===========================================================
# PART 9: Filter a Dictionary
# ===========================================================


marks = {
    "Sara": 95,
    "Joe": 80,
    "Ali": 45,
    "Mohammed": 70
}


passed_students = {
    name: mark
    for name, mark in marks.items()
    if mark >= 50
}


print(passed_students)


# ===========================================================
# PART 10: Get High Marks
# ===========================================================


high_marks = {
    name: mark
    for name, mark in marks.items()
    if mark >= 80
}


print(high_marks)


# ===========================================================
# PART 11: Convert Dictionary Values
# ===========================================================


prices = {
    "Laptop": 1000,
    "Mouse": 50,
    "Keyboard": 80
}


new_prices = {
    product: price * 1.10
    for product, price in prices.items()
}


print(new_prices)


# The prices were increased by 10%.



# ===========================================================
# PART 12: Convert Dictionary Keys
# ===========================================================


students = {
    "sara": 95,
    "joe": 80,
    "ali": 90
}


uppercase_students = {
    name.upper(): mark
    for name, mark in students.items()
}


print(uppercase_students)


# ===========================================================
# PART 13: Dictionary Comprehension from Two Lists
# ===========================================================


names = [
    "Sara",
    "Joe",
    "Ali"
]


marks = [
    95,
    80,
    90
]


students = {
    name: mark
    for name, mark in zip(names, marks)
}


print(students)


# ===========================================================
# PART 14: Dictionary Comprehension with Strings
# ===========================================================


word = "Python"


letters = {
    letter: word.count(letter)
    for letter in word
}


print(letters)


# ===========================================================
# PART 15: Set Comprehension
# ===========================================================


"""
Set comprehension is similar to
list comprehension.

The main difference:

List:

[expression for item in iterable]


Set:

{expression for item in iterable}


A set does not allow duplicate values.
"""


# ===========================================================
# PART 16: Basic Set Comprehension
# ===========================================================


numbers = [1, 2, 3, 4, 5]


squares = {
    number ** 2
    for number in numbers
}


print(squares)


# ===========================================================
# PART 17: Set Comprehension with Duplicates
# ===========================================================


numbers = [
    1,
    2,
    2,
    3,
    3,
    4,
    5,
    5
]


unique_numbers = {
    number
    for number in numbers
}


print(unique_numbers)


# Duplicate values are automatically removed.



# ===========================================================
# PART 18: Set Comprehension with Condition
# ===========================================================


numbers = range(1, 11)


even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}


print(even_numbers)


# ===========================================================
# PART 19: Set of Squares
# ===========================================================


numbers = [
    1,
    2,
    2,
    3,
    3,
    4
]


squares = {
    number ** 2
    for number in numbers
}


print(squares)


# ===========================================================
# PART 20: Set Comprehension with Strings
# ===========================================================


word = "programming"


letters = {
    letter
    for letter in word
}


print(letters)


# Duplicate letters are removed.



# ===========================================================
# PART 21: Convert Letters to Lowercase
# ===========================================================


word = "Python PROGRAMMING"


letters = {
    letter.lower()
    for letter in word
    if letter != " "
}


print(letters)


# ===========================================================
# PART 22: Set of Even Squares
# ===========================================================


numbers = range(1, 11)


result = {
    number ** 2
    for number in numbers
    if number % 2 == 0
}


print(result)


# ===========================================================
# PART 23: List vs Dictionary vs Set Comprehension
# ===========================================================


"""
List Comprehension:

- Uses []
- Keeps duplicates.
- Has indexes.


Example:

numbers = [
    number
    for number in range(5)
]


Dictionary Comprehension:

- Uses {}
- Stores key : value.
- Keys must be unique.


Example:

numbers = {
    number: number ** 2
    for number in range(5)
}


Set Comprehension:

- Uses {}
- Stores unique values.
- Does not have indexes.


Example:

numbers = {
    number ** 2
    for number in range(5)
}
"""


# ===========================================================
# PART 24: Compare the Three Types
# ===========================================================


numbers = [1, 2, 2, 3, 3, 4]


# List comprehension


list_result = [
    number
    for number in numbers
]


print("List:", list_result)


# Set comprehension


set_result = {
    number
    for number in numbers
}


print("Set:", set_result)


# Dictionary comprehension


dictionary_result = {
    number: number ** 2
    for number in numbers
}


print("Dictionary:", dictionary_result)


# ===========================================================
# PART 25: Nested Dictionary Comprehension
# ===========================================================


"""
Dictionary comprehension can also be
used with more complex data.
"""


students = {
    "Sara": 95,
    "Joe": 80,
    "Ali": 45
}


student_results = {

    name: {
        "mark": mark,
        "result": "Pass" if mark >= 50 else "Fail"
    }

    for name, mark in students.items()
}


print(student_results)


# ===========================================================
# PART 26: Practical Example - Product Prices
# ===========================================================


products = {
    "Laptop": 1200,
    "Mouse": 30,
    "Keyboard": 80,
    "Monitor": 300
}


# Get products that cost more than 50.


expensive_products = {
    product: price
    for product, price in products.items()
    if price > 50
}


print(expensive_products)


# ===========================================================
# PART 27: Practical Example - Increase Prices
# ===========================================================


products = {
    "Laptop": 1200,
    "Mouse": 30,
    "Keyboard": 80
}


updated_products = {
    product: price * 1.20
    for product, price in products.items()
}


print(updated_products)


# Prices increased by 20%.



# ===========================================================
# PART 28: Practical Example - Student Grades
# ===========================================================


students = {
    "Sara": 95,
    "Joe": 80,
    "Ali": 45,
    "Mohammed": 70,
    "Lina": 55
}


excellent_students = {
    name: mark
    for name, mark in students.items()
    if mark >= 90
}


print(excellent_students)


# ===========================================================
# PART 29: Practical Example - Unique Characters
# ===========================================================


text = "Hello Python"


unique_characters = {
    character.lower()
    for character in text
    if character != " "
}


print(unique_characters)


# ===========================================================
# PART 30: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a dictionary using
# dictionary comprehension.
#
# Use numbers from 1 to 10.
#
# The key should be the number.
#
# The value should be the square.
#
# Expected:
#
# {
#     1: 1,
#     2: 4,
#     ...
#     10: 100
# }
# -----------------------------------------------------------


# Exercise 2:
#
# Create a dictionary containing
# only even numbers from 1 to 20.
#
# The key should be the number.
#
# The value should be number * 10.
# -----------------------------------------------------------


# Exercise 3:
#
# Given:
#
# marks = {
#     "Sara": 95,
#     "Joe": 80,
#     "Ali": 45,
#     "Mohammed": 70
# }
#
# Create a new dictionary containing
# only students who passed.
# -----------------------------------------------------------


# Exercise 4:
#
# Given:
#
# marks = {
#     "Sara": 95,
#     "Joe": 80,
#     "Ali": 45,
#     "Mohammed": 70
# }
#
# Create a new dictionary where
# each student has:
#
# "Pass" if mark >= 50
# "Fail" otherwise.
# -----------------------------------------------------------


# Exercise 5:
#
# Given:
#
# names = ["Sara", "Joe", "Ali"]
# marks = [95, 80, 90]
#
# Create a dictionary using
# dictionary comprehension.
#
# Expected:
#
# {
#     "Sara": 95,
#     "Joe": 80,
#     "Ali": 90
# }
# -----------------------------------------------------------


# Exercise 6:
#
# Given:
#
# numbers = [1, 2, 2, 3, 4, 4, 5]
#
# Use set comprehension to create
# a set containing unique numbers.
# -----------------------------------------------------------


# Exercise 7:
#
# Given:
#
# word = "programming"
#
# Use set comprehension to get
# the unique characters.
# -----------------------------------------------------------


# Exercise 8:
#
# Given:
#
# numbers = range(1, 21)
#
# Use set comprehension to create
# a set containing only even squares.
#
# Example:
#
# {4, 16, 36, ...}
# -----------------------------------------------------------


# Exercise 9:
#
# Given:
#
# products = {
#     "Laptop": 1200,
#     "Mouse": 30,
#     "Keyboard": 80,
#     "Monitor": 300
# }
#
# Create a dictionary containing
# products that cost more than 100.
# -----------------------------------------------------------


# Exercise 10:
#
# Create a dictionary where:
#
# keys = numbers from 1 to 10
#
# values =
#
# "Even" if the number is even
# "Odd" otherwise.
#
# Example:
#
# {
#     1: "Odd",
#     2: "Even",
#     3: "Odd"
# }
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


"""
Dictionary and Set Comprehension Summary:


Dictionary Comprehension:

{
    key: value
    for item in iterable
}


With condition:

{
    key: value
    for item in iterable
    if condition
}


With if / else:

{
    key: value_if_true
    if condition
    else value_if_false
    for item in iterable
}


Set Comprehension:

{
    expression
    for item in iterable
}


With condition:

{
    expression
    for item in iterable
    if condition
}


Remember:

List Comprehension
    ->
Creates a list.

Dictionary Comprehension
    ->
Creates a dictionary.

Set Comprehension
    ->
Creates a set and removes duplicates.


Important:

Dictionary:
    key : value


Set:
    unique values only


Use comprehensions when they make
the code shorter AND readable.

If the comprehension becomes too
complicated, use a normal loop.
"""


###########################################################
# END OF DICTIONARY AND SET COMPREHENSION
###########################################################