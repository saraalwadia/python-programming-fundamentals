###########################################################
# If Statement in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:
- Understand how to make decisions in Python.
- Learn how to use if statement.
- Learn the difference between if, elif, and else.
- Use comparison and logical operators with conditions.

Topics Covered:

PART 1: If Statement
- if executes code only when the condition is True.
- The condition must return True or False.


PART 2: If - Else Statement
- if runs when the condition is True.
- else runs when the condition is False.


PART 3: Using Input with Conditions
- Get data from the user.
- Convert input to the correct data type.
- Use conditions based on user input.


PART 4: If - Elif - Else
- elif means another condition.
- Python checks conditions from top to bottom.
- else runs when no condition is True.


PART 5: Logical Operators
- and  --> Both conditions must be True.
- or   --> At least one condition must be True.


PART 6: Practice
- Check if a number is even or odd using modulus operator (%).

Important Notes:
- Colon : is required after the condition.
- Code inside if must be indented.
- Conditions use comparison operators:
    ==  equal
    !=  not equal
    >   greater than
    <   less than
    >=  greater or equal
    <=  less or equal

"""


# ===========================================================
# PART 1: Simple If Else
# ===========================================================


age = 23


# Check if age is less than 18

if age < 18:

    print("Child")


else:

    print("Adult")



# ===========================================================
# PART 2: Input with If
# ===========================================================


# Get age from user

my_age = int(input("Enter your age: "))


# Check the condition

if my_age > 0 and my_age <= 18:

    print("Child")


else:

    print("Adult")



# ===========================================================
# PART 3: If - Elif - Else
# ===========================================================


# elif is used when we have multiple conditions.


color = "Blue"


if color == "Blue":

    print("Blue")


elif color == "Red":

    print("Red")


else:

    print("None")



# ===========================================================
# PART 4: Practice
# ===========================================================


"""
Task:

Check if a number is:
- Even
- Odd

Hint:
Even numbers have remainder 0 when divided by 2.
"""


number = int(input("Enter Number: "))


if number % 2 == 0:

    print("Even")


else:

    print("Odd")