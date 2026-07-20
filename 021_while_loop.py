###########################################################
# While Loop in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:
- Understand how while loop works.
- Learn how to repeat code based on a condition.
- Learn how to update loop variables.
- Understand infinite loops.
- Use while loop with user input.


Topics Covered:


PART 1: While Loop
- while repeats code while a condition is True.
- The condition is checked before every iteration.


Syntax:

while condition:

    code



PART 2: Updating Counter
- The loop variable must change inside the loop.
- Otherwise, the loop will never stop.


PART 3: Infinite Loop
- Happens when the condition never becomes False.
- Always make sure the loop has a stopping condition.


PART 4: While with User Input
- Useful when we don't know how many times the loop will run.


Important Notes:
- while depends on a condition.
- The condition must eventually become False.
- Indentation is required.
"""


# ===========================================================
# PART 1: Basic While Loop
# ===========================================================


i = 0


while i < 10:

    print(i)

    i += 1



# ===========================================================
# PART 2: Print Numbers from 1 to 10
# ===========================================================


i = 1


while i <= 10:

    print(i)

    i += 1



# ===========================================================
# PART 3: Infinite Loop Example
# ===========================================================


"""
This loop will never stop:

while True:

    print("Hello")

"""


# ===========================================================
# PART 4: While Loop with User Input
# ===========================================================


password = ""


while password != "1234":

    password = input("Enter password: ")


print("Correct password")



# ===========================================================
# PART 5: Practice
# ===========================================================


# Print numbers from 10 to 1


number = 10


while number >= 1:

    print(number)

    number -= 1