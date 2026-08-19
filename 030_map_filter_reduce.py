###########################################################
# Map, Filter and Reduce in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand map().
- Understand filter().
- Understand reduce().
- Learn how to use lambda with map().
- Learn how to use lambda with filter().
- Learn how to use lambda with reduce().
- Understand the difference between map(), filter(), and reduce().
- Practice working with lists and functions.


Topics Covered:

PART 1:
What are map(), filter(), and reduce()?

PART 2:
map()

PART 3:
map() with lambda

PART 4:
map() with a normal function

PART 5:
filter()

PART 6:
filter() with lambda

PART 7:
filter() with a normal function

PART 8:
reduce()

PART 9:
reduce() with lambda

PART 10:
Working with Strings

PART 11:
Working with Dictionaries

PART 12:
Combining map() and filter()

PART 13:
Mini Projects

PART 14:
Practice Exercises
"""


# ===========================================================
# PART 1: What are map(), filter(), and reduce()?
# ===========================================================


"""
These functions are used to process collections
such as lists.

map():
- Applies a function to every item.
- Usually used to transform data.

filter():
- Keeps only the items that satisfy a condition.

reduce():
- Combines all items into one final value.
"""


# ===========================================================
# PART 2: map()
# ===========================================================


"""
map() applies a function to every item
in a collection.

Syntax:

map(function, iterable)


Example:

numbers = [1, 2, 3, 4]

result = map(function, numbers)
"""


numbers = [1, 2, 3, 4, 5]


def double(number):

    return number * 2


result = map(double, numbers)


# map() returns a map object.
# We can convert it to a list.


result = list(result)


print(result)


# ===========================================================
# PART 3: map() with lambda
# ===========================================================


"""
Lambda makes map() shorter and easier
for simple operations.
"""


numbers = [1, 2, 3, 4, 5]


result = list(
    map(
        lambda number: number * 2,
        numbers
    )
)


print(result)


# ===========================================================
# PART 4: More map() Examples
# ===========================================================


numbers = [1, 2, 3, 4, 5]


# Square every number.


squares = list(
    map(
        lambda number: number ** 2,
        numbers
    )
)


print(squares)


# ===========================================================
# PART 5: Convert Strings to Uppercase
# ===========================================================


names = [
    "sara",
    "joe",
    "ali",
    "mohammed"
]


upper_names = list(
    map(
        lambda name: name.upper(),
        names
    )
)


print(upper_names)


# ===========================================================
# PART 6: Add a Value to Every Number
# ===========================================================


numbers = [10, 20, 30, 40]


result = list(
    map(
        lambda number: number + 5,
        numbers
    )
)


print(result)


# ===========================================================
# PART 7: map() with Multiple Lists
# ===========================================================


"""
map() can work with more than one iterable.

The function receives one value
from each iterable.
"""


numbers1 = [1, 2, 3]

numbers2 = [10, 20, 30]


result = list(
    map(
        lambda x, y: x + y,
        numbers1,
        numbers2
    )
)


print(result)


# ===========================================================
# PART 8: filter()
# ===========================================================


"""
filter() keeps only the items
that satisfy a condition.

Syntax:

filter(function, iterable)

The function should return:

True
or
False
"""


numbers = [1, 2, 3, 4, 5, 6]


def is_even(number):

    return number % 2 == 0


result = filter(is_even, numbers)


result = list(result)


print(result)


# ===========================================================
# PART 9: filter() with lambda
# ===========================================================


numbers = [1, 2, 3, 4, 5, 6]


even_numbers = list(
    filter(
        lambda number: number % 2 == 0,
        numbers
    )
)


print(even_numbers)


# ===========================================================
# PART 10: Filter Odd Numbers
# ===========================================================


numbers = [1, 2, 3, 4, 5, 6, 7, 8]


odd_numbers = list(
    filter(
        lambda number: number % 2 != 0,
        numbers
    )
)


print(odd_numbers)


# ===========================================================
# PART 11: Filter Positive Numbers
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


positive_numbers = list(
    filter(
        lambda number: number > 0,
        numbers
    )
)


print(positive_numbers)


# ===========================================================
# PART 12: Filter Names
# ===========================================================


names = [
    "Sara",
    "Joe",
    "Ali",
    "Mohammed",
    "Lina"
]


long_names = list(
    filter(
        lambda name: len(name) > 4,
        names
    )
)


print(long_names)


# ===========================================================
# PART 13: filter() with Dictionaries
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


passed_students = list(
    filter(
        lambda student: student["mark"] >= 50,
        students
    )
)


print(passed_students)


# ===========================================================
# PART 14: reduce()
# ===========================================================


"""
reduce() combines all items
into one final value.

reduce() is available inside
the functools module.

Syntax:

from functools import reduce

reduce(function, iterable)
"""


from functools import reduce


numbers = [1, 2, 3, 4, 5]


result = reduce(
    lambda x, y: x + y,
    numbers
)


print(result)


# The calculation is:

# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15


# ===========================================================
# PART 15: reduce() for Multiplication
# ===========================================================


numbers = [1, 2, 3, 4, 5]


result = reduce(
    lambda x, y: x * y,
    numbers
)


print(result)


# ===========================================================
# PART 16: Find the Largest Number with reduce()
# ===========================================================


numbers = [10, 25, 7, 40, 15]


largest = reduce(
    lambda x, y: x if x > y else y,
    numbers
)


print(largest)


# ===========================================================
# PART 17: Find the Smallest Number with reduce()
# ===========================================================


numbers = [10, 25, 7, 40, 15]


smallest = reduce(
    lambda x, y: x if x < y else y,
    numbers
)


print(smallest)


# ===========================================================
# PART 18: map() + filter()
# ===========================================================


"""
We can combine map() and filter().

Example:

1. Filter even numbers.
2. Multiply each even number by 2.
"""


numbers = [
    1,
    2,
    3,
    4,
    5,
    6
]


even_numbers = filter(
    lambda number: number % 2 == 0,
    numbers
)


result = map(
    lambda number: number * 2,
    even_numbers
)


result = list(result)


print(result)


# ===========================================================
# PART 19: filter() + map() with Names
# ===========================================================


names = [
    "Sara",
    "Joe",
    "Ali",
    "Mohammed",
    "Lina"
]


# Keep names with more than 3 characters.


filtered_names = filter(
    lambda name: len(name) > 3,
    names
)


# Convert them to uppercase.


result = map(
    lambda name: name.upper(),
    filtered_names
)


result = list(result)


print(result)


# ===========================================================
# PART 20: map() + filter() with Students
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


# Keep students who passed.


passed_students = filter(
    lambda student: student["mark"] >= 50,
    students
)


# Get only their names.


student_names = map(
    lambda student: student["name"],
    passed_students
)


student_names = list(student_names)


print(student_names)


# ===========================================================
# PART 21: map() vs filter() vs reduce()
# ===========================================================


"""
map():

Transforms every item.

Example:

[1, 2, 3]

map(x * 2)

Result:

[2, 4, 6]


filter():

Keeps some items.

Example:

[1, 2, 3, 4]

filter(even)

Result:

[2, 4]


reduce():

Combines all items into one value.

Example:

[1, 2, 3, 4]

reduce(sum)

Result:

10
"""


# ===========================================================
# PART 22: Mini Project - Process Marks
# ===========================================================


"""
Mini Project:

We have a list of marks.

Tasks:

1. Add 5 points to every mark.
2. Keep marks greater than or equal to 50.
3. Calculate the total of the final marks.
"""


marks = [
    40,
    55,
    60,
    30,
    75,
    90
]


# Step 1:
# Add 5 points.


updated_marks = map(
    lambda mark: mark + 5,
    marks
)


updated_marks = list(updated_marks)


print("Updated marks:")

print(updated_marks)


# Step 2:
# Keep passing marks.


passed_marks = filter(
    lambda mark: mark >= 50,
    updated_marks
)


passed_marks = list(passed_marks)


print("Passed marks:")

print(passed_marks)


# Step 3:
# Calculate total.


total = reduce(
    lambda x, y: x + y,
    passed_marks
)


print("Total:", total)


# ===========================================================
# PART 23: Mini Project - Product Prices
# ===========================================================


products = [

    {
        "name": "Laptop",
        "price": 1200
    },

    {
        "name": "Mouse",
        "price": 30
    },

    {
        "name": "Keyboard",
        "price": 80
    },

    {
        "name": "Monitor",
        "price": 300
    }
]


# Get products that cost more than 50.


expensive_products = filter(
    lambda product: product["price"] > 50,
    products
)


# Get only product names.


product_names = map(
    lambda product: product["name"],
    expensive_products
)


product_names = list(product_names)


print(product_names)


# ===========================================================
# PART 24: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a list:
#
# numbers = [1, 2, 3, 4, 5]
#
# Use map() to multiply
# every number by 3.
# -----------------------------------------------------------


# Exercise 2:
#
# Create a list of numbers.
#
# Use filter() to return
# only even numbers.
# -----------------------------------------------------------


# Exercise 3:
#
# Create a list of numbers.
#
# Use filter() to return
# only numbers greater than 10.
# -----------------------------------------------------------


# Exercise 4:
#
# Create a list of names.
#
# Use map() to convert
# all names to uppercase.
# -----------------------------------------------------------


# Exercise 5:
#
# Create a list of names.
#
# Use filter() to keep names
# that contain the letter "a".
# -----------------------------------------------------------


# Exercise 6:
#
# Use reduce() to calculate
# the sum of:
#
# [10, 20, 30, 40]
# -----------------------------------------------------------


# Exercise 7:
#
# Use reduce() to calculate
# the multiplication of:
#
# [1, 2, 3, 4, 5]
# -----------------------------------------------------------


# Exercise 8:
#
# Create a list of students:
#
# students = [
#     ("Sara", 95),
#     ("Joe", 80),
#     ("Ali", 45),
#     ("Mohammed", 70)
# ]
#
# Use filter() to keep
# students who passed.
# -----------------------------------------------------------


# Exercise 9:
#
# Use map() to get only
# the names of the students.
# -----------------------------------------------------------


# Exercise 10:
#
# Create a list of numbers.
#
# 1. Filter the even numbers.
# 2. Multiply them by 10.
# 3. Calculate their sum using reduce().
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


"""
Map, Filter and Reduce Summary:

map():
- Applies a function to every item.
- Used to transform data.

filter():
- Keeps items that satisfy a condition.
- The function should return True or False.

reduce():
- Combines items into one final value.
- Imported from functools.


Common pattern:

map(
    lambda x: ...,
    data
)


filter(
    lambda x: ...,
    data
)


reduce(
    lambda x, y: ...,
    data
)


Important:

map() -> Transform

filter() -> Select

reduce() -> Combine
"""


###########################################################
# END OF MAP, FILTER AND REDUCE
###########################################################