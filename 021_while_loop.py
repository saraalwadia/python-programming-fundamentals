###########################################################
# While Loop in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:
- Understand how while loop works.
- Learn how to repeat code based on a condition.
- Understand the importance of updating the loop variable.
- Practice creating simple while loops.


Topics Covered:


PART 1: While Loop
- while repeats a block of code as long as the condition is True.
- The condition is checked before every iteration.


Syntax:

while condition:

    code



PART 2: Updating Loop Variable
- The loop variable must be changed inside the loop.
- If the condition never becomes False, the loop will run forever.


Example:

i = 0

while i < 5:

    print(i)

    i += 1



PART 3: While Loop vs For Loop

For Loop:
- Used when the number of repetitions is known.
- Commonly used with range().


While Loop:
- Used when repetition depends on a condition.
- The number of repetitions may not be known.


Important Notes:
- The condition must return True or False.
- The code inside while must be indented.
- Always make sure the loop can stop.

"""



# ===========================================================
# PART 1: Basic While Loop
# ===========================================================


i = 0


# Repeat while i is less than 10

while i < 10:

    print(i)

    # Increase i by 1
    # Without this line, the loop will never stop

    i += 1



# ===========================================================
# PART 2: Practice
# ===========================================================


"""
Task:

Print numbers from 1 to 10.
"""


i = 1


while i <= 10:

    print(i)

    i += 1