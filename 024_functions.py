###########################################################
# Functions in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand what a function is.
- Learn how to define a function using def.
- Learn how to call a function.
- Understand parameters and arguments.
- Understand positional and keyword arguments.
- Learn how to use default parameters.
- Understand the return statement.
- Understand the difference between print and return.
- Understand local and global variables.
- Use functions with if statements.
- Use functions with loops.
- Use functions with lists.
- Return multiple values from a function.


Topics Covered:

PART 1:
Basic Functions

PART 2:
Function Parameters and Arguments

PART 3:
Functions with Lists

PART 4:
Return Statement

PART 5:
print vs return

PART 6:
Positional and Keyword Arguments

PART 7:
Default Parameters

PART 8:
Functions with if Statements

PART 9:
Functions with Loops

PART 10:
Functions with Lists and Loops

PART 11:
Returning Multiple Values

PART 12:
Local and Global Variables

PART 13:
Boolean Functions

PART 14:
Calculator Using Functions

PART 15:
Common Mistakes

PART 16:
Exercises


Important Notes:

- A function is defined using def.
- A function does not run until it is called.
- Parameters are variables inside the function definition.
- Arguments are values passed to the function.
- return sends a value back from the function.
- print displays a value on the screen.
- Code inside a function must be indented.
"""


# ===========================================================
# PART 1: Basic Function
# ===========================================================


# A function is a reusable block of code.
#
# We define a function using the def keyword.


def display():

    print("Hello World")


# Calling the function:

display()


# A function can be called multiple times.

display()
display()


# ===========================================================
# PART 2: Function with Parameters
# ===========================================================


# Parameters allow us to pass data into a function.


def add(a, b):

    return a + b


# a and b are parameters.
#
# 10 and 20 are arguments.


result = add(10, 20)

print(result)


# Output:
#
# 30


# ===========================================================
# PART 3: Function with One Parameter
# ===========================================================


def hello_name(name):

    print("Hello", name)


hello_name("Sara")

hello_name("Yazan")

hello_name("Mohammed")


# ===========================================================
# PART 4: Functions with Lists
# ===========================================================


# A list can be passed to a function.


names = [
    "Sara",
    "Mohammed",
    "Yazan"
]


def display_names(names):

    for name in names:

        print("Welcome", name)


display_names(names)


# ===========================================================
# PART 5: Function with Multiple Parameters
# ===========================================================


def add_numbers(num1, num2):

    print(num1 + num2)


def subtract_numbers(num1, num2):

    print(num1 - num2)


def multiply_numbers(num1, num2):

    print(num1 * num2)


def divide_numbers(num1, num2):

    print(num1 / num2)


add_numbers(10, 5)

subtract_numbers(10, 5)

multiply_numbers(10, 5)

divide_numbers(10, 5)


# ===========================================================
# PART 6: Return Statement
# ===========================================================


# return sends a value back to the caller.


def sum_numbers(num1, num2):

    return num1 + num2


result = sum_numbers(10, 5)

print(result)


# We can also use the returned value in another operation.


result = sum_numbers(10, 5)

new_result = result * 2

print(new_result)


# ===========================================================
# PART 7: print vs return
# ===========================================================


# print displays a value.


def add_print(a, b):

    print(a + b)


add_print(10, 5)


# return sends the value back.


def add_return(a, b):

    return a + b


result = add_return(10, 5)

print(result)


# The important difference:
#
# print -> displays the value.
#
# return -> sends the value back so we can use it later.


# ===========================================================
# PART 8: Positional Arguments
# ===========================================================


def display_info(name, age):

    print("Name:", name)

    print("Age:", age)


# Positional arguments depend on their order.


display_info("Sara", 23)


# "Sara" -> name
# 23     -> age


# ===========================================================
# PART 9: Keyword Arguments
# ===========================================================


# We can specify the parameter name
# when calling the function.


display_info(
    name="Sara",
    age=23
)


# We can change the order when using keyword arguments.


display_info(
    age=23,
    name="Sara"
)


# ===========================================================
# PART 10: Default Parameters
# ===========================================================


# A default parameter has a default value.


def hello(name="Guest"):

    print("Hello", name)


hello("Sara")

hello()


# Output:
#
# Hello Sara
# Hello Guest


# Another example:


def power(number, exponent=2):

    return number ** exponent


print(power(5))

print(power(5, 3))


# When exponent is not provided,
# Python uses the default value 2.


# ===========================================================
# PART 11: Function with if Statement
# ===========================================================


def check_number(number):

    if number > 0:

        return "Positive"

    elif number < 0:

        return "Negative"

    else:

        return "Zero"


print(check_number(10))

print(check_number(-5))

print(check_number(0))


# ===========================================================
# PART 12: Boolean Function
# ===========================================================


# A function can return True or False.


def is_even(number):

    return number % 2 == 0


print(is_even(10))

print(is_even(7))


# Output:
#
# True
# False


# Another example:


def is_adult(age):

    return age >= 18


print(is_adult(20))

print(is_adult(15))


# ===========================================================
# PART 13: Function with a Loop
# ===========================================================


def print_numbers():

    for i in range(1, 6):

        print(i)


print_numbers()


# ===========================================================
# PART 14: Function with List and Loop
# ===========================================================


def print_students(students):

    for student in students:

        print("Student:", student)


students = [
    "Sara",
    "Yazan",
    "Mohammed",
    "Ali"
]


print_students(students)


# ===========================================================
# PART 15: Function to Calculate Sum
# ===========================================================


def calculate_sum(numbers):

    total = 0

    for number in numbers:

        total += number

    return total


numbers = [
    10,
    20,
    30,
    40
]


result = calculate_sum(numbers)

print("Total:", result)


# ===========================================================
# PART 16: Returning Multiple Values
# ===========================================================


# A function can return more than one value.


def get_info():

    name = input("Enter name: ")

    age = int(input("Enter age: "))

    return name, age


result = get_info()

print(result)


# Python returns the values as a tuple.
#
# Example:
#
# ('Sara', 23)


# We can unpack the values:


name, age = get_info()

print("Name:", name)

print("Age:", age)


# ===========================================================
# PART 17: Function with Parameters and Return
# ===========================================================


def student_info(name, age):

    return name, age


name = input("Enter name: ")

age = int(input("Enter age: "))


result = student_info(name, age)

print(result)


# We can also unpack the returned values.


name, age = student_info("Sara", 23)

print(name)

print(age)


# ===========================================================
# PART 18: Local Variables
# ===========================================================


# A variable created inside a function
# is usually a local variable.


def show_name():

    name = "Sara"

    print(name)


show_name()


# name exists inside the function.
#
# The following code would cause an error:
#
# print(name)
#
# because name was created inside the function.


# ===========================================================
# PART 19: Global Variables
# ===========================================================


# A variable created outside a function
# is a global variable.


name = "Sara"


def display_global_name():

    print(name)


display_global_name()


# The function can access the global variable.


# ===========================================================
# PART 20: Calculator Using Multiple Functions
# ===========================================================


def sum_function(num1, num2):

    return num1 + num2


def sub_function(num1, num2):

    return num1 - num2


def multiply_function(num1, num2):

    return num1 * num2


def div_function(num1, num2):

    return num1 / num2


num1 = float(input("Enter number 1: "))

num2 = float(input("Enter number 2: "))

operator = input("Enter operation (+, -, *, /): ")


if operator == "+":

    result = sum_function(num1, num2)


elif operator == "-":

    result = sub_function(num1, num2)


elif operator == "*":

    result = multiply_function(num1, num2)


elif operator == "/":

    if num2 != 0:

        result = div_function(num1, num2)

    else:

        result = "Cannot divide by zero."


else:

    result = "Invalid operator."


print("Result:", result)


# ===========================================================
# PART 21: Calculator Using One Function
# ===========================================================


def calculator(num1, operator, num2):

    if operator == "+":

        return num1 + num2

    elif operator == "-":

        return num1 - num2

    elif operator == "*":

        return num1 * num2

    elif operator == "/":

        if num2 != 0:

            return num1 / num2

        return "Cannot divide by zero."

    else:

        return "Invalid operator."


num1 = float(input("Enter number 1: "))

operator = input("Enter operation (+, -, *, /): ")

num2 = float(input("Enter number 2: "))


result = calculator(num1, operator, num2)

print("Result:", result)


# ===========================================================
# PART 22: Common Mistakes
# ===========================================================


# -----------------------------------------------------------
# Mistake 1:
# Defining a function without calling it.
# -----------------------------------------------------------


def say_hello():

    print("Hello")


# The function will not run until we call it.


say_hello()


# -----------------------------------------------------------
# Mistake 2:
# Wrong number of arguments.
# -----------------------------------------------------------


def add(a, b):

    return a + b


print(add(10, 20))


# The following code causes a TypeError
# because the function requires two arguments:
#
# print(add(10))


# -----------------------------------------------------------
# Mistake 3:
# Using print instead of return.
# -----------------------------------------------------------


def wrong_add(a, b):

    print(a + b)


result = wrong_add(10, 20)

print(result)


# result will be None.
#
# print displays the result,
# but it does not return the result.


# Correct version:


def correct_add(a, b):

    return a + b


result = correct_add(10, 20)

print(result)


# -----------------------------------------------------------
# Mistake 4:
# Code after return.
# -----------------------------------------------------------


def calculate(a, b):

    result = a + b

    return result

    # This code will never execute:
    #
    # print(result)


print(calculate(10, 5))


# return immediately ends the function.


# -----------------------------------------------------------
# Mistake 5:
# Missing indentation.
# -----------------------------------------------------------


# The following code causes IndentationError:
#
# def hello():
# print("Hello")


# Correct:


def hello():

    print("Hello")


hello()


# ===========================================================
# PART 23: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a function called greet()
# that prints:
#
# Hello, Python!


# -----------------------------------------------------------
# Exercise 2:
#
# Create a function called greet_user(name)
# that receives a name and prints:
#
# Hello Sara
#
# when the name is Sara.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 3:
#
# Create a function called add(a, b)
# that returns the sum of two numbers.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 4:
#
# Create a function called is_even(number)
# that returns True if the number is even
# and False if the number is odd.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 5:
#
# Create a function called check_age(age)
# that returns:
#
# "Child"  -> age less than 18
# "Adult"  -> age 18 or greater
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 6:
#
# Create a function called calculate_sum(numbers)
# that receives a list of numbers
# and returns their total.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 7:
#
# Create a function called print_students(students)
# that receives a list of student names
# and prints each name using a for loop.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 8:
#
# Create a calculator function:
#
# calculator(num1, operator, num2)
#
# It should support:
#
# +
# -
# *
# /
#
# and return the result.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 9:
#
# Create a function called get_student_info()
# that asks the user for:
#
# name
# age
#
# and returns both values.
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


# def
# -> Used to define a function.
#
# function call
# -> Executes the function.
#
# parameter
# -> A variable inside the function definition.
#
# argument
# -> A value passed to the function.
#
# positional argument
# -> Argument passed according to its position.
#
# keyword argument
# -> Argument passed using the parameter name.
#
# default parameter
# -> Parameter with a default value.
#
# return
# -> Sends a value back from the function.
#
# print
# -> Displays a value on the screen.
#
# local variable
# -> Variable created inside a function.
#
# global variable
# -> Variable created outside a function.
#
# ===========================================================
# END OF FUNCTIONS
# ===========================================================