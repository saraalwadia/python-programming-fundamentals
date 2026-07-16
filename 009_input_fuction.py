# ===========================================================
# Input Function in Python
# ===========================================================


"""
Teaching Notes:

Lesson Objectives:
- Understand how to receive data from the user.
- Learn how to use the input() function.
- Understand the returned data type from input().
- Combine user input with output.

Topics Covered:

PART 1: What is input()?
- input() is a built-in Python function.
- It allows the program to receive information from the user.
- The program pauses until the user enters a value.

Syntax:

input("message")


PART 2: Storing User Input
- The value entered by the user can be stored in a variable.
- The variable keeps the entered information for later use.


PART 3: Input Data Type
- input() always returns a string (str).
- Even if the user enters a number, Python treats it as text.

Example:

age = input("Enter age: ")

The type of age will be:
str


PART 4: Using Input with Output
- We can combine user input with print().
- We can create interactive programs.

Important Notes:
- input() waits for the user response.
- The message inside input() is displayed before receiving data.
- Use type() to check the returned value.

Common Mistakes:
- Expecting input() to return numbers automatically.
- Trying mathematical operations directly on input values.

Example mistake:

age = input("Enter age: ")
print(age + 1)  # Error


"""


# ===========================================================
# PART 1: Getting User Input
# ===========================================================


# input() allows the user to enter data

name = input("Enter your name: ")



# Print the entered value

print("Hello " + name)



# ===========================================================
# PART 2: Checking Input Type
# ===========================================================


# input() always returns a string

print(type(name))



# ===========================================================
# PART 3: More Examples
# ===========================================================


favorite_language = input("Enter your favorite programming language: ")


print("You like " + favorite_language)



# ===========================================================
# Practice
# ===========================================================


"""
Practice Tasks:

1. Ask the user to enter:
   - Name
   - Country

   Print:
   My name is ___ and I live in ___.


2. Ask the user for their favorite color.
   Print a sentence using the input.


3. Check the type of all inputs using type().

"""