###########################################################
# For Loop in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:
- Understand how loops work.
- Learn how to repeat code using for loop.
- Learn how to use range().
- Learn how to loop through lists and strings.
- Understand nested loops.
- Learn break and continue statements.


Topics Covered:


PART 1: For Loop
- for loop is used to repeat code.
- It works with sequences:
    - range()
    - lists
    - strings


PART 2: range() Function

Syntax:

range(end)

- Starts from 0.
- Stops before end.


range(start, end)

- Starts from start.
- Stops before end.


range(start, end, step)

- step controls the increment.



PART 3: Loop Through Lists
- We can loop directly through list values.
- We can also access elements using indexes.


PART 4: Loop Through Strings
- Strings are sequences of characters.
- Each character can be accessed using a loop.


PART 5: Nested For Loop
- A loop inside another loop.
- Used for working with multi-dimensional data.


PART 6: break
- Stops the loop completely.


PART 7: continue
- Skips the current iteration and moves to the next one.


Important Notes:
- The code inside the loop must be indented.
- range() does not include the ending value.
- Always check the loop condition and values.
"""


# ===========================================================
# PART 1: Basic For Loop with range()
# ===========================================================


# range(end)

for i in range(10):

    print(i)



# ===========================================================
# PART 2: range(start, end)
# ===========================================================


for i in range(1, 10):

    print(i)



# ===========================================================
# PART 3: range(start, end, step)
# ===========================================================


for i in range(0, 101, 10):

    print(i)



# ===========================================================
# PART 4: Practical Example - Multiplication Table
# ===========================================================


number = int(input("Enter number: "))


for i in range(0, 11):

    print(i * number)



# ===========================================================
# PART 5: Loop Through List
# ===========================================================


arr = ["a", "b", "c"]



# Access indexes

for i in range(len(arr)):

    print(i)



# Access values using index

for i in range(len(arr)):

    print(arr[i])



# Direct access to values

for value in arr:

    print(value)



# ===========================================================
# PART 6: Loop Through String
# ===========================================================


for letter in "Sara Mohammed":

    print(letter)



# ===========================================================
# PART 7: Nested For Loop
# ===========================================================


grid = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9],

    [0]

]


# Access rows

for row in grid:

    print(row)



# Access every element

for row in grid:

    for col in row:

        print(col)



# ===========================================================
# PART 8: break Statement
# ===========================================================


for i in range(10):

    if i == 5:

        break

    print(i)



# ===========================================================
# PART 9: continue Statement
# ===========================================================


for i in range(10):

    if i == 5:

        continue

    print(i)



# ===========================================================
# PART 10: Exercises
# ===========================================================



# Exercise 1:
# Print numbers multiplied by 2


for i in range(11):

    print(i * 2)



# Exercise 2:
# Calculate sum from 0 to 99


result = 0


for i in range(100):

    result += i


print(result)



# Exercise 3:
# Find numbers divisible by 7 and 5
# Between 1500 and 2700


numbers = []


for x in range(1500, 2701):

    if x % 7 == 0 and x % 5 == 0:

        numbers.append(str(x))


print(",".join(numbers))