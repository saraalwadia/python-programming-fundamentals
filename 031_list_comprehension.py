###########################################################
# List Comprehension in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand what list comprehension is.
- Learn the basic syntax.
- Create lists using loops.
- Add conditions to list comprehensions.
- Use if / else with list comprehensions.
- Work with strings.
- Work with nested loops.
- Understand when list comprehension is useful.


Topics Covered:

PART 1:
What is List Comprehension?

PART 2:
Basic List Comprehension

PART 3:
List Comprehension with range()

PART 4:
List Comprehension with Conditions

PART 5:
List Comprehension with if / else

PART 6:
Working with Strings

PART 7:
Working with Existing Lists

PART 8:
Nested List Comprehension

PART 9:
Dictionary Comprehension

PART 10:
Set Comprehension

PART 11:
Normal Loop vs Comprehension

PART 12:
Practice Exercises
"""


# ===========================================================
# PART 1: What is List Comprehension?
# ===========================================================


"""
List comprehension is a short way to create a list.

Instead of writing:

numbers = []

for i in range(5):

    numbers.append(i)


We can write:

numbers = [i for i in range(5)]


Basic syntax:

[expression for item in iterable]
"""


# ===========================================================
# PART 2: Basic List Comprehension
# ===========================================================


numbers = [i for i in range(5)]


print(numbers)


# Output:
# [0, 1, 2, 3, 4]


# ===========================================================
# PART 3: Normal For Loop vs List Comprehension
# ===========================================================


# Normal for loop


numbers = []


for i in range(5):

    numbers.append(i)


print(numbers)


# List comprehension


numbers = [i for i in range(5)]


print(numbers)


# Both produce the same result.



# ===========================================================
# PART 4: Create a List of Squares
# ===========================================================


squares = []


for i in range(1, 6):

    squares.append(i ** 2)


print(squares)


# The same example using comprehension:


squares = [
    i ** 2
    for i in range(1, 6)
]


print(squares)


# ===========================================================
# PART 5: Multiply Every Number
# ===========================================================


numbers = [1, 2, 3, 4, 5]


result = [
    number * 2
    for number in numbers
]


print(result)


# ===========================================================
# PART 6: List Comprehension with range()
# ===========================================================


numbers = [
    i
    for i in range(1, 11)
]


print(numbers)


# ===========================================================
# PART 7: Even Numbers
# ===========================================================


"""
We can add a condition:

[expression for item in iterable if condition]
"""


numbers = [
    i
    for i in range(1, 11)
    if i % 2 == 0
]


print(numbers)


# ===========================================================
# PART 8: Odd Numbers
# ===========================================================


odd_numbers = [
    i
    for i in range(1, 11)
    if i % 2 != 0
]


print(odd_numbers)


# ===========================================================
# PART 9: Numbers Greater Than 5
# ===========================================================


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


result = [
    number
    for number in numbers
    if number > 5
]


print(result)


# ===========================================================
# PART 10: Positive Numbers
# ===========================================================


numbers = [
    -5,
    -2,
    0,
    3,
    7,
    -1,
    10
]


positive_numbers = [
    number
    for number in numbers
    if number > 0
]


print(positive_numbers)


# ===========================================================
# PART 11: List Comprehension with if / else
# ===========================================================


"""
We can also use if / else.

Syntax:

[expression_if_true if condition else expression_if_false
 for item in iterable]
"""


numbers = [1, 2, 3, 4, 5]


result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]


print(result)


# ===========================================================
# PART 12: Convert Numbers to Even / Odd
# ===========================================================


numbers = range(1, 11)


result = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]


print(result)


# ===========================================================
# PART 13: Pass / Fail
# ===========================================================


marks = [
    95,
    80,
    45,
    70,
    30
]


results = [
    "Pass" if mark >= 50 else "Fail"
    for mark in marks
]


print(results)


# ===========================================================
# PART 14: Working with Strings
# ===========================================================


name = "Sara"


letters = [
    letter
    for letter in name
]


print(letters)


# ===========================================================
# PART 15: Convert String to Uppercase
# ===========================================================


names = [
    "sara",
    "joe",
    "ali",
    "mohammed"
]


upper_names = [
    name.upper()
    for name in names
]


print(upper_names)


# ===========================================================
# PART 16: Filter Names
# ===========================================================


names = [
    "Sara",
    "Joe",
    "Ali",
    "Mohammed",
    "Lina"
]


long_names = [
    name
    for name in names
    if len(name) > 4
]


print(long_names)


# ===========================================================
# PART 17: Names Containing a Specific Letter
# ===========================================================


names = [
    "Sara",
    "Joe",
    "Ali",
    "Mohammed",
    "Lina"
]


names_with_a = [
    name
    for name in names
    if "a" in name.lower()
]


print(names_with_a)


# ===========================================================
# PART 18: List of Tuples
# ===========================================================


students = [
    ("Sara", 95),
    ("Joe", 80),
    ("Ali", 45),
    ("Mohammed", 70)
]


names = [
    student[0]
    for student in students
]


print(names)


# ===========================================================
# PART 19: Get Student Marks
# ===========================================================


marks = [
    student[1]
    for student in students
]


print(marks)


# ===========================================================
# PART 20: Get Passing Students
# ===========================================================


passing_students = [
    student
    for student in students
    if student[1] >= 50
]


print(passing_students)


# ===========================================================
# PART 21: List Comprehension with Dictionaries
# ===========================================================


students = [

    {
        "name": "Sara",
        "mark": 95
    },

    {
        "name": "Joe",
        "mark": 80
    },

    {
        "name": "Ali",
        "mark": 45
    },

    {
        "name": "Mohammed",
        "mark": 70
    }
]


student_names = [
    student["name"]
    for student in students
]


print(student_names)


# ===========================================================
# PART 22: Passing Students from Dictionaries
# ===========================================================


passed_students = [
    student["name"]
    for student in students
    if student["mark"] >= 50
]


print(passed_students)


# ===========================================================
# PART 23: Nested List Comprehension
# ===========================================================


"""
A list comprehension can contain
more than one for loop.

Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


Normal loop:

result = []

for row in matrix:

    for number in row:

        result.append(number)
"""


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


result = []


for row in matrix:

    for number in row:

        result.append(number)


print(result)


# The same example using comprehension:


result = [
    number
    for row in matrix
    for number in row
]


print(result)


# ===========================================================
# PART 24: Nested Loops with range()
# ===========================================================


result = [

    (x, y)

    for x in range(3)

    for y in range(3)
]


print(result)


# ===========================================================
# PART 25: Dictionary Comprehension
# ===========================================================


"""
Comprehension can also be used
with dictionaries.

Syntax:

{key: value for item in iterable}
"""


numbers = [1, 2, 3, 4, 5]


squares = {
    number: number ** 2
    for number in numbers
}


print(squares)


# ===========================================================
# PART 26: Dictionary Comprehension with Condition
# ===========================================================


numbers = range(1, 11)


even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}


print(even_squares)


# ===========================================================
# PART 27: Set Comprehension
# ===========================================================


"""
Set comprehension works similarly
to list comprehension.

The result will be a set,
so duplicate values are removed.
"""


numbers = [1, 2, 2, 3, 3, 4, 5]


squares = {
    number ** 2
    for number in numbers
}


print(squares)


# ===========================================================
# PART 28: Remove Duplicates
# ===========================================================


names = [
    "Sara",
    "Joe",
    "Sara",
    "Ali",
    "Joe"
]


unique_names = {
    name
    for name in names
}


print(unique_names)


# ===========================================================
# PART 29: List Comprehension with Function
# ===========================================================


def square(number):

    return number ** 2


numbers = [1, 2, 3, 4, 5]


result = [
    square(number)
    for number in numbers
]


print(result)


# ===========================================================
# PART 30: List Comprehension with Lambda
# ===========================================================


square = lambda number: number ** 2


numbers = [1, 2, 3, 4, 5]


result = [
    square(number)
    for number in numbers
]


print(result)


# ===========================================================
# PART 31: When NOT to Use List Comprehension
# ===========================================================


"""
List comprehension is useful for
short and simple operations.

Avoid very complicated comprehensions.

For example, this can become
difficult to read:

result = [
    x * 2
    for x in numbers
    if x > 5
    if x % 2 == 0
]


In complicated situations,
a normal for loop may be clearer.
"""


# ===========================================================
# PART 32: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a list containing
# numbers from 1 to 20
# using list comprehension.
# -----------------------------------------------------------


# Exercise 2:
#
# Create a list containing
# the squares of numbers
# from 1 to 10.
# -----------------------------------------------------------


# Exercise 3:
#
# Create a list containing
# only even numbers from 1 to 50.
# -----------------------------------------------------------


# Exercise 4:
#
# Create a list containing
# only odd numbers from 1 to 50.
# -----------------------------------------------------------


# Exercise 5:
#
# Given:
#
# numbers = [10, 20, 30, 40, 50]
#
# Create a new list where
# every number is multiplied by 3.
# -----------------------------------------------------------


# Exercise 6:
#
# Given:
#
# names = ["sara", "joe", "ali", "mohammed"]
#
# Create a new list containing
# all names in uppercase.
# -----------------------------------------------------------


# Exercise 7:
#
# Given:
#
# names = ["Sara", "Joe", "Ali", "Mohammed"]
#
# Create a list containing
# names longer than 4 characters.
# -----------------------------------------------------------


# Exercise 8:
#
# Given:
#
# marks = [95, 80, 45, 70, 30]
#
# Create a list containing:
#
# "Pass" if mark >= 50
# "Fail" otherwise.
# -----------------------------------------------------------


# Exercise 9:
#
# Given:
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# Use list comprehension to create
# one flat list containing all numbers.
# -----------------------------------------------------------


# Exercise 10:
#
# Create a dictionary using
# dictionary comprehension.
#
# Example:
#
# numbers = [1, 2, 3, 4, 5]
#
# Expected result:
#
# {
#     1: 1,
#     2: 4,
#     3: 9,
#     4: 16,
#     5: 25
# }
# -----------------------------------------------------------


# Exercise 11:
#
# Given:
#
# students = [
#     ("Sara", 95),
#     ("Joe", 80),
#     ("Ali", 45),
#     ("Mohammed", 70)
# ]
#
# Use list comprehension to get
# only the names of students
# who passed.
# -----------------------------------------------------------


# Exercise 12:
#
# Given:
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# Create a list containing
# the square of only even numbers.
#
# Expected:
#
# [4, 16, 36]
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


"""
List Comprehension Summary:


Basic:

[expression for item in iterable]


With condition:

[expression for item in iterable if condition]


With if / else:

[
    expression_if_true
    if condition
    else expression_if_false
    for item in iterable
]


Examples:

[x for x in numbers]

[x * 2 for x in numbers]

[x for x in numbers if x % 2 == 0]

[
    "Even" if x % 2 == 0 else "Odd"
    for x in numbers
]


Important:

List comprehension
    ->
Short way to create lists.


Dictionary comprehension
    ->
Short way to create dictionaries.


Set comprehension
    ->
Short way to create sets.


Use comprehension when the logic
is simple and readable.

Use a normal loop when the logic
becomes complicated.
"""


###########################################################
# END OF LIST COMPREHENSION
###########################################################