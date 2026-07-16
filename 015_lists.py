# ===========================================================
# Lesson: Lists - Basics & List Operations
# ===========================================================


"""
Teaching Notes:


Lesson Objectives:

- Understand what lists are in Python.
- Learn how to create and access lists.
- Understand indexing and slicing.
- Learn how to add, update, and delete list elements.



What is a List?

A list is a collection used to store multiple values
inside one variable.


Example:

numbers = [10, 20, 30]


Important Properties of Lists:

1. Ordered:
- Elements have a specific order.
- Each element has an index.


2. Mutable:
- We can change, add, or remove elements.


3. Allows Duplicate Values:

Example:

numbers = [1, 2, 2, 3]


4. Can Store Different Data Types:

Example:

data = [10, "Sara", True]


-----------------------------------------------------------

List Indexing:

- Index starts from 0.

Example:

list = [10, 20, 30]

Index:

0 --> 10
1 --> 20
2 --> 30


Negative Indexing:

- Starts from the end.

-1 --> Last element


-----------------------------------------------------------

List Slicing:

Used to get a part of a list.


Syntax:

list[start:end:step]


Important:

start --> included

end --> not included


-----------------------------------------------------------

List Modification:

Because lists are mutable:

We can:

1. Add elements:
- append()
- insert()


2. Update elements:
- Using index


3. Delete elements:
- del
- remove()
- clear()


"""



###########################################################
# Part 1: List Basics
###########################################################


# A list stores multiple values in one variable.
# Lists can contain multiple data types.
# Lists are ordered and mutable (can be changed).


numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]



###########################################################
# Display List
###########################################################


# Print the complete list


print(numbers)



###########################################################
# List Length
###########################################################


# len() returns the number of elements in the list


print(len(numbers))




###########################################################
# List Indexing
###########################################################


# Each element has an index.
# Index starts from 0.


# Access the second element


print(numbers[1])



# Access the last element using negative indexing


print(numbers[-1])




###########################################################
# List Slicing
###########################################################


# Slicing is used to get a part of a list.


# Syntax:

# list[start:end]


# Start from index 1 until the end


print(numbers[1:])



# From the beginning until index 4
# Index 4 is not included


print(numbers[:4])



# From index 1 to index 4
# Index 4 is not included


print(numbers[1:4])




###########################################################
# Slicing with Step
###########################################################


# Syntax:

# list[start:end:step]



# Start from index 1
# Take every second element


print(numbers[1::2])



# Start from index 0
# Take every third element


print(numbers[0::3])



# Start from index 0
# Take every fourth element


print(numbers[0::4])



# Start from index 1
# Take every sixth element


print(numbers[1::6])




###########################################################
# Part 2: Adding List Elements
###########################################################


# Create an empty list


letters = []




###########################################################
# Add Data using append()
###########################################################


# append()
# Adds an element at the end of the list.


letters.append("a")

letters.append("b")

letters.append("c")

letters.append("d")


print(letters)




###########################################################
# Add Data using insert()
###########################################################


# insert(index, value)
# Adds an element at a specific position.


letters.insert(0, "M")


print(letters)




###########################################################
# Part 3: Display Data
###########################################################


# Print the complete list


print(letters)



# Access an element using index


print(letters[1])




###########################################################
# Part 4: Update List Elements
###########################################################


# Lists are mutable.
# We can change the value of any element.


letters[3] = "D"


print(letters)




###########################################################
# Part 5: Delete List Elements
###########################################################


# Delete an element using its index


del letters[2]


print(letters)



# Remove an element using its value


letters.remove("a")


print(letters)



# Remove all elements from the list


letters.clear()


print(letters)



###########################################################
# Practice
###########################################################


"""
Practice Tasks:


1. Create a list:

fruits = ["Apple", "Banana", "Orange"]


Do the following:

- Print the list.
- Print the first element.
- Print the last element.
- Add "Mango" using append().
- Change "Banana" to "Strawberry".
- Remove "Apple".



2. Create a list of numbers:

numbers = [5,10,15,20,25]


Print:

- First three elements.
- Last two elements.
- Every second element.

"""