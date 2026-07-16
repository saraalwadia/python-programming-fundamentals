# ===========================================================
# String Concatenation
# ===========================================================


"""
Teaching Notes:

Lesson Objectives:
- Understand what string concatenation means.
- Learn how to join strings using the + operator.
- Combine variables with strings.
- Understand why numbers cannot be concatenated directly with strings.
- Learn how to convert values using str().

Prerequisites:
- Variables
- Strings
- input()
- Data Types


Topics Covered:

PART 1: What is String Concatenation?
- Concatenation means joining multiple strings together.
- Python uses the + operator to combine strings.
- The result is a new string.

Example:
"Hello " + "Python"

Output:
Hello Python


PART 2: Concatenating Variables
- Variables containing strings can be joined together.
- Spaces must be added manually.

Example:
first_name + " " + last_name


PART 3: Combining Strings with Variables
- We can create messages by combining text and variables.


PART 4: Concatenation Rules
- The + operator works between strings only.
- Strings cannot be joined directly with numbers.

Wrong:
"Age: " + 20

Correct:
"Age: " + str(20)


PART 5: Concatenation with User Input
- input() returns a string.
- User input can be directly concatenated with other strings.


Important Notes:
- Concatenation does not add spaces automatically.
- Always check the data type before combining values.
- str() converts other data types into strings.

Common Mistakes:
- Forgetting to add spaces between words.
- Trying to concatenate int or float with strings.
- Using + when f-strings would be easier for complex messages.

"""


# ===========================================================
# PART 1: Joining Two Strings
# ===========================================================


first_name = "Sara"
last_name = "Alwadia"


# Combine two strings using +

full_name = first_name + last_name


print(full_name)


# Output:
# SaraAlwadia



# ===========================================================
# PART 2: Adding Spaces Between Strings
# ===========================================================


# Space is also a string

full_name = first_name + " " + last_name


print(full_name)


# Output:
# Sara Alwadia



# ===========================================================
# PART 3: Concatenating Text with Variables
# ===========================================================


name = "Sara"


message = "Hello " + name


print(message)


# Output:
# Hello Sara



# ===========================================================
# PART 4: Concatenating Multiple Strings
# ===========================================================


country = "Palestine"

city = "Gaza"


sentence = "I live in " + city + ", " + country


print(sentence)


# Output:
# I live in Gaza, Palestine



# ===========================================================
# PART 5: String and Number Concatenation
# ===========================================================


age = 23


# This will cause an error:
# print("My age is " + age)


# Because:
# "My age is " -> string
# age          -> integer



# ===========================================================
# PART 6: Type Conversion using str()
# ===========================================================


# Convert integer into string

age = 20


message = "My age is " + str(age)


print(message)


# Output:
# My age is 20



# ===========================================================
# PART 7: Concatenation with User Input
# ===========================================================


name = input("Enter your name: ")


print("Welcome " + name)



# ===========================================================
# Practice
# ===========================================================


"""
Practice Tasks:

1. Create variables:

first_name
last_name
favorite_language


2. Print:

My name is Sara Alwadia and I like Python.


using string concatenation.


3. Ask the user for:
- Name
- Favorite food

Print:

Hello Sara, your favorite food is Pizza.


using concatenation.

"""