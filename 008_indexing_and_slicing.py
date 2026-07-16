# ===========================================================
# String Indexing & Slicing
# ===========================================================


"""
Teaching Notes:

Lesson Objectives:
- Understand how strings are stored as sequences of characters.
- Learn how to access characters using indexing.
- Learn how to extract parts of strings using slicing.
- Understand positive and negative indexes.

Prerequisites:
- Variables
- Strings
- print()
- len()

Topics Covered:

PART 1: Strings as Sequences
- A string is a sequence of characters.
- Each character has a position called an index.
- Python indexing starts from 0.

Example:
Python

Index:
 P  y  t  h  o  n
 0  1  2  3  4  5


PART 2: Positive and Negative Indexing
- Positive indexing starts from the beginning.
- Negative indexing starts from the end.

Example:
Python

Positive:
0  1  2  3  4  5

Negative:
-6 -5 -4 -3 -2 -1


PART 3: String Length
- len() returns the number of characters.
- The last index is always:
    length - 1


PART 4: String Slicing
Syntax:

string[start:end]

Rules:
- start is included.
- end is excluded.


PART 5: Slicing with Step
Syntax:

string[start:end:step]

Examples:
- step = 2 → take every second character.
- step = -1 → reverse the string.


Important Notes:
- Indexing accesses one character.
- Slicing accesses multiple characters.
- Strings are immutable; slicing creates a new string.

Common Mistakes:
- Forgetting that indexing starts from 0.
- Including the end index when slicing.
- Using an index that does not exist.

"""


# ===========================================================
# PART 1: String Indexing
# ===========================================================


# Strings are sequences of characters.

myString = "Python"


# Access the first character

print(myString[0])


# Access the second character

print(myString[1])


# Access the last character using negative indexing

print(myString[-1])


# Access the second last character

print(myString[-2])



# ===========================================================
# PART 2: String Length
# ===========================================================


# len() returns the number of characters

print(len(myString))


# The last index is:
# length - 1


print(myString[len(myString)-1])



# ===========================================================
# PART 3: String Slicing
# ===========================================================


myString = "Hello Python"


# Syntax:
# string[start:end]


# Get characters from index 0 to index 4

print(myString[0:5])


# Get characters from index 6 until the end

print(myString[6:])


# Get characters from beginning until index 4

print(myString[:5])


# Copy the complete string

print(myString[:])



# ===========================================================
# PART 4: Slicing with Step
# ===========================================================


word = "Programming"


# Syntax:
# string[start:end:step]


# Take every second character

print(word[0::2])


# Take every third character

print(word[0::3])


# Reverse the string

print(word[::-1])



# ===========================================================
# PART 5: Practice
# ===========================================================


text = "Python Programming"


"""
Practice Tasks:

1. Print the first character.

2. Print the last character.

3. Print "Python".

4. Print "Programming".

5. Reverse the string.

6. Print every second character.

"""


# Write your solutions here: