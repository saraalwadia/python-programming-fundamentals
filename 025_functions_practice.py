###########################################################
# Functions - Practice Exercises
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Practice defining functions.
- Practice calling functions.
- Practice using parameters and arguments.
- Practice using return.
- Practice using if statements inside functions.
- Practice using loops inside functions.
- Practice using lists with functions.
- Practice using dictionaries with functions.
- Practice using default parameters.
- Practice returning multiple values.
- Combine functions with previously learned concepts.


Topics Covered:

PART 1:
Basic Function Practice

PART 2:
Parameters and Arguments

PART 3:
Return Values

PART 4:
Functions with Conditions

PART 5:
Functions with Loops

PART 6:
Functions with Lists

PART 7:
Boolean Functions

PART 8:
Default Parameters

PART 9:
Multiple Return Values

PART 10:
Calculator Function

PART 11:
Functions with Dictionary

PART 12:
Mini Project

PART 13:
Final Exercises
"""


# ===========================================================
# PART 1: Basic Function Practice
# ===========================================================


# Exercise 1:
#
# Create a function called greet()
# that prints:
#
# Hello, Python!


def greet():

    print("Hello, Python!")


greet()


# ===========================================================
# PART 2: Function with a Parameter
# ===========================================================


# Exercise 2:
#
# Create a function that receives a name
# and prints a welcome message.


def welcome(name):

    print("Welcome", name)


welcome("Sara")

welcome("Joe")

welcome("Mohammed")


# ===========================================================
# PART 3: Function with Two Parameters
# ===========================================================


# Exercise 3:
#
# Create a function that receives two numbers
# and prints their sum.


def add_numbers(num1, num2):

    print(num1 + num2)


add_numbers(10, 20)

add_numbers(5, 7)


# ===========================================================
# PART 4: Return a Value
# ===========================================================


# Exercise 4:
#
# Create a function that receives two numbers
# and returns their sum.


def add(num1, num2):

    return num1 + num2


result = add(10, 20)

print("Result:", result)


# The returned value can be used later.


result = add(10, 20)

result = result * 2

print(result)


# ===========================================================
# PART 5: Even or Odd Function
# ===========================================================


# Exercise 5:
#
# Create a function called is_even()
# that returns True if the number is even
# and False if the number is odd.


def is_even(number):

    return number % 2 == 0


print(is_even(10))

print(is_even(7))


# ===========================================================
# PART 6: Positive, Negative or Zero
# ===========================================================


# Exercise 6:
#
# Create a function that receives a number
# and returns:
#
# "Positive"
# "Negative"
# "Zero"


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
# PART 7: Function with a Loop
# ===========================================================


# Exercise 7:
#
# Create a function that prints numbers
# from 1 to 10.


def print_numbers():

    for number in range(1, 11):

        print(number)


print_numbers()


# ===========================================================
# PART 8: Function with a Loop and Condition
# ===========================================================


# Exercise 8:
#
# Create a function that receives a number
# and prints all even numbers from 0
# to that number.


def print_even_numbers(number):

    for i in range(number + 1):

        if i % 2 == 0:

            print(i)


print_even_numbers(20)


# ===========================================================
# PART 9: Function with a List
# ===========================================================


# Exercise 9:
#
# Create a function that receives a list
# of names and prints each name.


def print_names(names):

    for name in names:

        print(name)


students = [
    "Sara",
    "Joe",
    "Ali",
    "Mohammed"
]


print_names(students)


# ===========================================================
# PART 10: Calculate List Sum
# ===========================================================


# Exercise 10:
#
# Create a function that receives a list
# of numbers and returns their sum.


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
# PART 11: Find the Largest Number
# ===========================================================


# Exercise 11:
#
# Create a function that receives a list
# of numbers and returns the largest number.


def find_max(numbers):

    largest = numbers[0]

    for number in numbers:

        if number > largest:

            largest = number

    return largest


numbers = [
    10,
    50,
    20,
    80,
    30
]


print("Largest:", find_max(numbers))


# ===========================================================
# PART 12: Count Even Numbers
# ===========================================================


# Exercise 12:
#
# Create a function that receives a list
# and returns how many even numbers it contains.


def count_even(numbers):

    count = 0

    for number in numbers:

        if number % 2 == 0:

            count += 1

    return count


numbers = [
    1,
    2,
    4,
    7,
    8,
    10
]


print("Even numbers:", count_even(numbers))


# ===========================================================
# PART 13: Search in a List
# ===========================================================


# Exercise 13:
#
# Create a function that receives:
#
# 1. A list
# 2. A value to search for
#
# The function should return True
# if the value exists.
#
# Otherwise, return False.


def search_number(numbers, target):

    for number in numbers:

        if number == target:

            return True

    return False


numbers = [
    10,
    20,
    30,
    40
]


print(search_number(numbers, 20))

print(search_number(numbers, 100))


# ===========================================================
# PART 14: Default Parameter
# ===========================================================


# Exercise 14:
#
# Create a function that receives a name.
#
# If no name is provided,
# use "Guest" as the default.


def greet_user(name="Guest"):

    print("Hello", name)


greet_user("Sara")

greet_user()


# ===========================================================
# PART 15: Function with Multiple Return Values
# ===========================================================


# Exercise 15:
#
# Create a function that receives
# a student's name and age
# and returns both values.


def student_info(name, age):

    return name, age


result = student_info("Sara", 23)

print(result)


# We can unpack the returned values.


name, age = student_info("Sara", 23)


print("Name:", name)

print("Age:", age)


# ===========================================================
# PART 16: Grade Function
# ===========================================================


# Exercise 16:
#
# Create a function that receives a mark
# and returns the grade:
#
# 90 - 100 -> Excellent
# 80 - 89  -> Very Good
# 70 - 79  -> Good
# 60 - 69  -> Fair
# Below 60 -> Fail


def get_grade(mark):

    if mark >= 90:

        return "Excellent"

    elif mark >= 80:

        return "Very Good"

    elif mark >= 70:

        return "Good"

    elif mark >= 60:

        return "Fair"

    else:

        return "Fail"


print(get_grade(95))

print(get_grade(83))

print(get_grade(72))

print(get_grade(50))


# ===========================================================
# PART 17: Age Classification
# ===========================================================


# Exercise 17:
#
# Create a function that receives age
# and returns:
#
# Child -> below 18
# Adult -> 18 to 64
# Old   -> 65 and above


def check_age(age):

    if age < 18:

        return "Child"

    elif age < 65:

        return "Adult"

    else:

        return "Old"


print(check_age(10))

print(check_age(25))

print(check_age(70))


# ===========================================================
# PART 18: Calculator Function
# ===========================================================


# Exercise 18:
#
# Create a calculator function that receives:
#
# num1
# operator
# num2
#
# The function should support:
#
# +
# -
# *
# /
#
# and return the result.


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
# PART 19: Function with Dictionary
# ===========================================================


# Exercise 19:
#
# Create a dictionary containing students
# and their marks.
#
# Create a function that receives the dictionary
# and a student name.
#
# Return the student's mark if the student exists.


students = {

    "Sara": 95,

    "Joe": 85,

    "Ali": 90,

    "Mohammed": 78
}


def get_student_mark(students, name):

    if name in students:

        return students[name]

    return "Student not found"


print(get_student_mark(students, "Sara"))

print(get_student_mark(students, "Ali"))

print(get_student_mark(students, "John"))


# ===========================================================
# PART 20: Mini Project - Student Information
# ===========================================================


"""
Mini Project:

Create a small student information program.

The program should:

1. Ask the user for the student's name.
2. Ask for three marks.
3. Calculate the average.
4. Determine the grade.
5. Display the student's information.

Use separate functions for:

- Calculating the average.
- Determining the grade.
- Displaying the information.
"""


def calculate_average(mark1, mark2, mark3):

    return (mark1 + mark2 + mark3) / 3


def get_grade_from_average(average):

    if average >= 90:

        return "Excellent"

    elif average >= 80:

        return "Very Good"

    elif average >= 70:

        return "Good"

    elif average >= 60:

        return "Fair"

    else:

        return "Fail"


def display_student(name, average, grade):

    print("Student:", name)

    print("Average:", average)

    print("Grade:", grade)


student_name = input("Enter student name: ")

mark1 = float(input("Enter mark 1: "))

mark2 = float(input("Enter mark 2: "))

mark3 = float(input("Enter mark 3: "))


average = calculate_average(
    mark1,
    mark2,
    mark3
)


grade = get_grade_from_average(average)


display_student(
    student_name,
    average,
    grade
)


# ===========================================================
# PART 21: Final Practice Exercises
# ===========================================================


# Exercise 20:
#
# Create a function called multiply(a, b)
# that returns the multiplication of two numbers.


# -----------------------------------------------------------
# Exercise 21:
#
# Create a function called find_min(numbers)
# that returns the smallest number in a list.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 22:
#
# Create a function called count_odd(numbers)
# that returns the number of odd values
# in a list.
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 23:
#
# Create a function called reverse_text(text)
# that returns the text reversed.
#
# Example:
#
# reverse_text("Sara")
#
# Output:
#
# "araS"
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 24:
#
# Create a function called count_vowels(text)
# that returns the number of vowels
# in the given string.
#
# Vowels:
#
# a, e, i, o, u
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 25:
#
# Create a function called is_palindrome(text)
# that returns True if the text is a palindrome.
#
# Example:
#
# "madam" -> True
# "hello" -> False
# -----------------------------------------------------------


# -----------------------------------------------------------
# Exercise 26:
#
# Create a function that receives a list
# of numbers and returns a new list
# containing only the even numbers.
#
# Example:
#
# [1, 2, 3, 4, 5, 6]
#
# Output:
#
# [2, 4, 6]
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


"""
Functions Practice Summary:

We practiced:

- Creating functions.
- Calling functions.
- Parameters.
- Arguments.
- Positional arguments.
- Keyword arguments.
- Default parameters.
- return.
- if statements inside functions.
- for loops inside functions.
- Lists with functions.
- Dictionaries with functions.
- Boolean functions.
- Multiple return values.
- Combining multiple functions.
- Building a small project using functions.
"""


###########################################################
# END OF FUNCTIONS PRACTICE
###########################################################