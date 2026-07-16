###########################################################
# Lesson 01
# My First Python Program
###########################################################

"""
Teaching Notes:

Lesson Objectives:
- Understand how Python programs are executed.
- Learn the print() function.
- Understand the difference between text and numbers.
- Learn how Python evaluates simple expressions.
- Introduce comments.

Topics Covered:

PART 1: Running the First Python Program
- Every Python program starts by executing instructions line by line.
- Python reads code from top to bottom.

PART 2: print() Function
- print() is used to display output on the screen.
- It can display text, numbers, and results of calculations.

PART 3: Strings vs Numbers
- Text values are written inside quotes (" " or ' ').
- Numbers are written without quotes.
- Python treats "1" as text and 1 as a number.

PART 4: Expressions
- Python can calculate expressions before printing.
- Example: 1 + 2 is calculated first, then printed.


Important Notes:
- Explain that print() does not return a value; it only displays output.
- Show the difference between:
    print(1 + 2)
    print("1 + 2")
- Explain that quotes change the data type.

Common Mistakes:
- Forgetting quotation marks around text.
- Writing print(Hello) instead of print("Hello").
- Confusing displayed output with the code itself.

"""



###########################################################
# PART 1: First Python Output
###########################################################

# print() displays information on the screen

print("Welcome to Python Course")
print("My name is Sara")
print("I love programming")



###########################################################
# PART 2: Printing Numbers
###########################################################

# Numbers do not need quotation marks

print(1)


# Python evaluates mathematical expressions first

print(1 + 2)



###########################################################
# PART 3: String vs Expression
###########################################################

# Anything inside quotes is treated as a string

print("1 + 2")


# Compare:
# print(1 + 2)      -> calculates the result
# print("1 + 2")    -> prints the text exactly



###########################################################
# PART 4: Multiple print Statements
###########################################################

# Each print() statement creates a new line by default

print("Hello")
print("World")



###########################################################
# PART 5: Multiple Statements in One Line
###########################################################

# Python allows multiple statements in one line
# However, it is recommended to write one statement per line.
# using semicolon (;)

print("Hello"); print("World")


# Output:
# Hello
# World


###########################################################
# Practice:
###########################################################

# 1. Print your name.
# 2. Print your favorite programming language.
# 3. Print the result of:
#    5 + 10
# 4. Print "5 + 10" as text.