###########################################################
# Lambda Functions in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand what a lambda function is.
- Learn the syntax of lambda functions.
- Understand the difference between def and lambda.
- Use lambda functions with one argument.
- Use lambda functions with multiple arguments.
- Use lambda functions with sorted().
- Prepare for map() and filter().


Topics Covered:

PART 1:
What is a Lambda Function?

PART 2:
Basic Lambda Function

PART 3:
Lambda with One Argument

PART 4:
Lambda with Multiple Arguments

PART 5:
Lambda with Two Numbers

PART 6:
Lambda with Conditions

PART 7:
Lambda vs Normal Function

PART 8:
Lambda with sorted()

PART 9:
Lambda with Lists of Dictionaries

PART 10:
Practice Exercises
"""


# ===========================================================
# PART 1: What is a Lambda Function?
# ===========================================================


"""
A lambda function is a small anonymous function.

Anonymous means that the function does not
necessarily have a name.

Syntax:

lambda arguments: expression


Example:

lambda x: x * 2


This function receives x
and returns x * 2.
"""


# ===========================================================
# PART 2: Basic Lambda Function
# ===========================================================


double = lambda x: x * 2


print(double(5))

print(double(10))


# ===========================================================
# PART 3: Lambda with One Argument
# ===========================================================


"""
A lambda function can receive one argument.
"""


square = lambda x: x ** 2


print(square(4))

print(square(10))


# ===========================================================
# PART 4: Lambda with Multiple Arguments
# ===========================================================


"""
A lambda function can receive
more than one argument.
"""


add = lambda x, y: x + y


print(add(5, 3))


subtract = lambda x, y: x - y


print(subtract(10, 4))


multiply = lambda x, y: x * y


print(multiply(6, 5))


# ===========================================================
# PART 5: Lambda vs Normal Function
# ===========================================================


"""
Normal function:

def add(x, y):

    return x + y


Lambda:

lambda x, y: x + y
"""


def add_function(x, y):

    return x + y


print(add_function(10, 5))


add_lambda = lambda x, y: x + y


print(add_lambda(10, 5))


# Both produce the same result.



# ===========================================================
# PART 6: Lambda with Strings
# ===========================================================


name_length = lambda name: len(name)


print(name_length("Sara"))

print(name_length("Mohammed"))


# ===========================================================
# PART 7: Lambda with Conditions
# ===========================================================


"""
A lambda can contain a conditional expression.

Syntax:

lambda x: value_if_true if condition else value_if_false
"""


check_number = lambda x: "Even" if x % 2 == 0 else "Odd"


print(check_number(10))

print(check_number(7))


# ===========================================================
# PART 8: Lambda with Positive and Negative Numbers
# ===========================================================


check_number = lambda x: (
    "Positive"
    if x > 0
    else "Negative"
    if x < 0
    else "Zero"
)


print(check_number(10))

print(check_number(-5))

print(check_number(0))


# ===========================================================
# PART 9: Lambda with sorted()
# ===========================================================


"""
sorted() can sort a list.

By default, sorted() sorts values
in ascending order.
"""


numbers = [5, 2, 9, 1, 7]


print(sorted(numbers))


# ===========================================================
# PART 10: sorted() with reverse
# ===========================================================


print(sorted(numbers, reverse=True))


# ===========================================================
# PART 11: sorted() with Lambda
# ===========================================================


"""
We can use lambda with sorted()
to tell Python what value to use
for sorting.
"""


names = [
    "Sara",
    "Joe",
    "Mohammed",
    "Ali"
]


result = sorted(
    names,
    key=lambda name: len(name)
)


print(result)


# Names are sorted according to length.



# ===========================================================
# PART 12: Sort by Last Character
# ===========================================================


names = [
    "Sara",
    "Joe",
    "Ali",
    "Mohammed"
]


result = sorted(
    names,
    key=lambda name: name[-1]
)


print(result)


# ===========================================================
# PART 13: Lambda with Dictionaries
# ===========================================================


"""
Suppose we have a list of dictionaries.
"""


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
        "mark": 90
    }
]


# Sort students by mark.


students_sorted = sorted(
    students,
    key=lambda student: student["mark"]
)


print(students_sorted)


# ===========================================================
# PART 14: Sort from Highest to Lowest
# ===========================================================


students_sorted = sorted(
    students,
    key=lambda student: student["mark"],
    reverse=True
)


print(students_sorted)


# ===========================================================
# PART 15: Sort Students by Name
# ===========================================================


students_sorted = sorted(
    students,
    key=lambda student: student["name"]
)


print(students_sorted)


# ===========================================================
# PART 16: Lambda with a Tuple
# ===========================================================


students = [

    ("Sara", 95),

    ("Joe", 80),

    ("Ali", 90)

]


# Sort by mark.


result = sorted(
    students,
    key=lambda student: student[1]
)


print(result)


# ===========================================================
# PART 17: Lambda with max()
# ===========================================================


numbers = [10, 25, 7, 40, 15]


largest = max(numbers)


print(largest)


# ===========================================================
# PART 18: Lambda with min()
# ===========================================================


smallest = min(numbers)


print(smallest)


# ===========================================================
# PART 19: max() with Dictionaries
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
        "mark": 90
    }
]


best_student = max(
    students,
    key=lambda student: student["mark"]
)


print(best_student)


# ===========================================================
# PART 20: Lambda with Strings
# ===========================================================


words = [
    "Python",
    "AI",
    "Programming",
    "Data"
]


longest_word = max(
    words,
    key=lambda word: len(word)
)


print(longest_word)


# ===========================================================
# PART 21: Lambda with User Input
# ===========================================================


number = int(input("Enter a number: "))


result = lambda x: x * 2


print("Result:", result(number))


# ===========================================================
# PART 22: Lambda Calculator
# ===========================================================


add = lambda x, y: x + y

subtract = lambda x, y: x - y

multiply = lambda x, y: x * y

divide = lambda x, y: x / y


print(add(10, 5))

print(subtract(10, 5))

print(multiply(10, 5))

print(divide(10, 5))


# ===========================================================
# PART 23: Lambda with a Dictionary
# ===========================================================


operations = {

    "+": lambda x, y: x + y,

    "-": lambda x, y: x - y,

    "*": lambda x, y: x * y,

    "/": lambda x, y: x / y
}


print(operations["+"](10, 5))

print(operations["-"](10, 5))

print(operations["*"](10, 5))

print(operations["/"](10, 5))


# ===========================================================
# PART 24: Lambda with sorted() and Dictionaries
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


products_sorted = sorted(
    products,
    key=lambda product: product["price"]
)


print(products_sorted)


# ===========================================================
# PART 25: Important Note
# ===========================================================


"""
Lambda functions are useful for small,
simple operations.

Use def when:

- The function is complex.
- The function contains multiple statements.
- The function needs a descriptive name.
- The function will be reused many times.

Use lambda when:

- The operation is very small.
- We need a function temporarily.
- We are working with functions such as:
    sorted()
    map()
    filter()
"""


# ===========================================================
# PART 26: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a lambda function that
# multiplies a number by 5.
#
# Example:
#
# multiply_by_five(4)
#
# Output:
#
# 20
# -----------------------------------------------------------


# Exercise 2:
#
# Create a lambda function that
# returns the square of a number.
# -----------------------------------------------------------


# Exercise 3:
#
# Create a lambda function that
# checks whether a number is:
#
# Even
# or
# Odd
# -----------------------------------------------------------


# Exercise 4:
#
# Create a lambda function that
# returns the length of a string.
# -----------------------------------------------------------


# Exercise 5:
#
# Create a list of numbers.
#
# Use sorted() and lambda
# to sort the numbers according
# to their distance from zero.
#
# Example:
#
# [-10, 2, -3, 5]
#
# Expected:
#
# [2, -3, 5, -10]
# -----------------------------------------------------------


# Exercise 6:
#
# Create a list of students:
#
# students = [
#     ("Sara", 95),
#     ("Joe", 80),
#     ("Ali", 90)
# ]
#
# Use sorted() and lambda
# to sort students by mark.
# -----------------------------------------------------------


# Exercise 7:
#
# Create a list of dictionaries
# containing product names and prices.
#
# Use sorted() and lambda
# to sort products by price.
# -----------------------------------------------------------


# Exercise 8:
#
# Use max() and lambda
# to find the student with
# the highest mark.
# -----------------------------------------------------------


# Exercise 9:
#
# Use min() and lambda
# to find the student with
# the lowest mark.
# -----------------------------------------------------------


# Exercise 10:
#
# Create a dictionary containing
# calculator operations.
#
# Use lambda functions for:
#
# +
# -
# *
# /
#
# Then ask the user for:
#
# first number
# operation
# second number
#
# and print the result.
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


"""
Lambda Functions Summary:

We learned:

- What lambda functions are.
- lambda syntax.
- Lambda with one argument.
- Lambda with multiple arguments.
- Lambda with conditions.
- Lambda vs def.
- Lambda with sorted().
- Lambda with max().
- Lambda with min().
- Lambda with lists.
- Lambda with tuples.
- Lambda with dictionaries.
- Lambda with user input.


Important:

Lambda syntax:

lambda arguments: expression


Example:

square = lambda x: x ** 2


Lambda functions are designed for
small and simple operations.
"""


###########################################################
# END OF LAMBDA FUNCTIONS
###########################################################