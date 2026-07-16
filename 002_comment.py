# ===========================================================
# Lesson 02
# Comments & Documentation
# ===========================================================

"""
Teaching Notes:

Lesson Objectives:
- Understand why programmers write comments.
- Learn different types of comments in Python.
- Learn how to document code.
- Understand the difference between comments and docstrings.

Topics Covered:

PART 1: Why We Use Comments
- Comments explain the purpose of the code.
- Comments help other developers understand the program.
- Comments help us remember why we wrote something.
- Python ignores comments during execution.

PART 2: Single-Line Comments
- Start with #.
- Used for short explanations.
- Can be written before or beside a line of code.

PART 3: Common Uses of Comments
- Explain code purpose.
- Add information about the author and file.
- Temporarily prevent code from running.

PART 4: Docstrings
- Written using triple quotes:
    """ """ 
- Used to describe modules, functions, and classes.
- They are stored as documentation strings.
- They can be accessed by Python documentation tools.

Important Notes:
- Comments are ignored by Python.
- Docstrings are not the same as comments.
- Avoid writing unnecessary comments that explain obvious code.

Common Mistakes:
- Using comments instead of explaining unclear code.
- Thinking triple quotes are normal comments.
- Writing too many comments that make code harder to read.

"""


# ===========================================================
# PART 1: File Information Comment
# ===========================================================

# Comments can be used to describe file information.

# License:
# Information about how the code can be used.

# Created By:
# The person who wrote the file.

# Created Date:
# When the file was created.

# Purpose:
# Why this file was created.



# ===========================================================
# PART 2: Single-Line Comments
# ===========================================================

# This is a single-line comment.

print("Hello Python")


# Comment can be written beside code

print("Welcome to Python")  # This prints a welcome message



# ===========================================================
# PART 3: Prevent Code From Running
# ===========================================================

# We can comment a line to prevent Python from executing it.

# print("This line will not run")


print("This line will run")



# ===========================================================
# PART 4: Docstrings
# ===========================================================

"""
This is a docstring.

It is usually used to describe:
- Modules
- Functions
- Classes

Unlike comments, docstrings can be accessed
as documentation.
"""


print("Learning Documentation")



# ===========================================================
# Practice
# ===========================================================

# 1. Write a comment with your name.
# 2. Write a comment explaining what the program does.
# 3. Comment a line of code and observe that it does not run.