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
- Learn how to use break and continue with while loops.


Topics Covered:

PART 1: Basic While Loop
- while repeats code while a condition is True.
- The condition is checked before every iteration.

Syntax:

while condition:

    code


PART 2: Updating Counter
- The loop variable must change inside the loop.
- Otherwise, the loop may never stop.


PART 3: Infinite Loop
- Happens when the condition never becomes False.
- Always make sure the loop has a stopping condition.


PART 4: While Loop with User Input
- Useful when we don't know how many times
  the loop will run.


PART 5: break with While
- Stops the loop completely.


PART 6: continue with While
- Skips the current iteration.


PART 7: While Loop with a Counter
- We can use a counter to control the loop.


Important Notes:
- while depends on a condition.
- The condition must eventually become False.
- Indentation is required.
- Always update the loop variable when necessary.
"""


# ===========================================================
# PART 1: Basic While Loop
# ===========================================================


i = 0


while i < 10:

    print(i)

    i += 1


# Output:
#
# 0
# 1
# 2
# ...
# 9


# ===========================================================
# PART 2: Print Numbers from 1 to 10
# ===========================================================


i = 1


while i <= 10:

    print(i)

    i += 1


# Output:
#
# 1
# 2
# 3
# ...
# 10


# ===========================================================
# PART 3: Counting with a Step
# ===========================================================


number = 10


while number <= 100:

    print(number)

    number += 10


# Output:
#
# 10
# 20
# 30
# ...
# 100


# ===========================================================
# PART 4: Countdown
# ===========================================================


number = 10


while number >= 1:

    print(number)

    number -= 1


# Output:
#
# 10
# 9
# 8
# ...
# 1


# ===========================================================
# PART 5: Infinite Loop
# ===========================================================


"""
An infinite loop happens when the condition
never becomes False.

Example:

i = 0

while i < 10:

    print(i)

    # i is never updated


This code is intentionally commented out
because it will run forever.
"""


# ===========================================================
# PART 6: Common While Loop Mistake
# ===========================================================


"""
Wrong example:

i = 0

while i < 10:

    print(i)

    i + 1


Why is this wrong?

i + 1 only calculates a new value.
It does NOT update i.

Correct:

i += 1

"""


# ===========================================================
# PART 7: While Loop with User Input
# ===========================================================


password = ""


while password != "1234":

    password = input("Enter password: ")


print("Correct password")


# The loop continues until the user enters:
#
# 1234


# ===========================================================
# PART 8: While Loop with User Input
# ===========================================================


number = int(input("Enter a positive number: "))


while number <= 0:

    print("Invalid number.")

    number = int(input("Enter a positive number: "))


print("Valid number:", number)


# ===========================================================
# PART 9: break with While Loop
# ===========================================================


# break stops the loop completely.

i = 0


while i < 10:

    if i == 5:

        break

    print(i)

    i += 1


# Output:
#
# 0
# 1
# 2
# 3
# 4


# The loop stops when i becomes 5.


# ===========================================================
# PART 10: continue with While Loop
# ===========================================================


# continue skips the current iteration
# and moves to the next iteration.

i = 0


while i < 10:

    i += 1

    if i == 5:

        continue

    print(i)


# Output:
#
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10


# ===========================================================
# PART 11: While Loop with a Counter
# ===========================================================


counter = 1


while counter <= 5:

    print("Counter:", counter)

    counter += 1


# ===========================================================
# PART 12: Calculate a Sum
# ===========================================================


number = 1

total = 0


while number <= 100:

    total += number

    number += 1


print("Total:", total)


# ===========================================================
# PART 13: FOR vs WHILE
# ===========================================================


# FOR:
#
# We usually use for when we know
# the sequence or range we want to iterate over.

for i in range(5):

    print(i)


# WHILE:
#
# We use while when repetition depends
# on a condition.

i = 0


while i < 5:

    print(i)

    i += 1


# Both examples print:
#
# 0
# 1
# 2
# 3
# 4


# ===========================================================
# PART 14: Practice
# ===========================================================


# Exercise 1:
# Print numbers from 1 to 20 using while.


number = 1


while number <= 20:

    print(number)

    number += 1


# -----------------------------------------------------------
# Exercise 2:
# Print even numbers from 2 to 20.
# -----------------------------------------------------------


number = 2


while number <= 20:

    print(number)

    number += 2


# -----------------------------------------------------------
# Exercise 3:
# Print numbers from 10 to 1.
# -----------------------------------------------------------


number = 10


while number >= 1:

    print(number)

    number -= 1


# -----------------------------------------------------------
# Exercise 4:
# Calculate the sum from 1 to 50.
# -----------------------------------------------------------


number = 1

total = 0


while number <= 50:

    total += number

    number += 1


print(total)


# -----------------------------------------------------------
# Exercise 5:
# Ask the user to enter numbers.
# Stop when the user enters 0.
#
# Then print the total of all entered numbers.
# -----------------------------------------------------------


total = 0

number = int(input("Enter number (0 to stop): "))


while number != 0:

    total += number

    number = int(input("Enter number (0 to stop): "))


print("Total:", total)


# ===========================================================
# SUMMARY
# ===========================================================

# while
# -> repeats code while a condition is True.
#
# counter
# -> a variable used to control the loop.
#
# +=
# -> increases a variable.
#
# -=
# -> decreases a variable.
#
# break
# -> completely stops the loop.
#
# continue
# -> skips the current iteration.
#
# Infinite loop
# -> happens when the condition never becomes False.
#
# ===========================================================
# END OF WHILE LOOP
# ===========================================================