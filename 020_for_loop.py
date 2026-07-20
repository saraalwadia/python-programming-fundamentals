###########################################################
# For Loop in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:
- Understand how loops work in Python.
- Learn how to repeat code using for loop.
- Learn how to use range().
- Learn how to loop through lists and strings.
- Practice using loops with conditions.

Topics Covered:


PART 1: For Loop
- for loop is used to repeat code multiple times.
- It works with sequences:
    - Lists
    - Strings
    - Range


PART 2: range() Function

Syntax:

range(start, end, step)

Rules:
- start is included.
- end is not included.
- step defines the increment.


Examples:

range(5)

Output:
0 1 2 3 4


range(1,5)

Output:
1 2 3 4



PART 3: Loop Through Lists
- We can access list elements using:
    - Index
    - Direct values


PART 4: Loop Through Strings
- Strings are sequences of characters.
- for loop can access each character separately.


PART 5: Using Conditions Inside Loops
- We can use if statements inside loops.
- Useful for filtering data.


Important Notes:
- The code inside the loop must be indented.
- The loop variable changes automatically.
- range() does not include the ending value.

"""


# ===========================================================
# PART 1: Using range()
# ===========================================================


# range(10) starts from 0 and stops before 10


for i in range(10):

    print(i)



# ===========================================================
# PART 2: range(start, end)
# ===========================================================


# Start from 0 and stop before 10


for i in range(0, 10):

    print(i)



# ===========================================================
# PART 3: Loop Through List
# ===========================================================


arr = ["a", "b", "c"]



# Access list indexes

for i in range(len(arr)):

    print(i)



# Access list values using index

for i in range(len(arr)):

    print(arr[i])



# ===========================================================
# PART 4: Loop Through String
# ===========================================================


# Access each character in the string


for letter in "Sara Mohammed":

    print(letter)



# ===========================================================
# PART 5: Practice Exercises
# ===========================================================



# Exercise 1:
# Print numbers multiplied by 2


for i in range(11):

    print(i * 2)



# Exercise 2:
# Calculate the sum of numbers from 0 to 99


total = 0


for i in range(100):

    total += i


print(total)



# Exercise 3:
# Find numbers between 1500 and 2700
# that are divisible by 7 and 5


numbers = []


for x in range(1500, 2701):

    if x % 7 == 0 and x % 5 == 0:

        numbers.append(str(x))


print(",".join(numbers))