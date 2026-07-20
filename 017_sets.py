# ===========================================================
# Sets in Python
# ===========================================================


# A set is a collection used to store multiple values.
# Sets are:
# - Unordered (no index)
# - Mutable (can be changed)
# - Do not allow duplicate values
# - Written using {}


# ===========================================================
# Part 1: Creating Sets
# ===========================================================


numbers = {10, 20, 30, 40}

print(numbers)


# Check type

print(type(numbers))



# ===========================================================
# Part 2: Duplicate Values
# ===========================================================


# Duplicate values are removed automatically

numbers = {10, 20, 20, 30, 30, 40}

print(numbers)



# ===========================================================
# Part 3: Adding Data
# ===========================================================


numbers = {10, 20, 30}


# add()
# Adds one element to the set

numbers.add(40)

print(numbers)



# update()
# Adds multiple elements

numbers.update([50, 60, 70])

print(numbers)



# ===========================================================
# Part 4: Removing Data
# ===========================================================


numbers = {10, 20, 30, 40}


# remove()
# Removes a specific value
# Gives error if value does not exist

numbers.remove(20)

print(numbers)



# discard()
# Removes a value without error

numbers.discard(100)

print(numbers)



# clear()
# Removes all elements

numbers.clear()

print(numbers)



# ===========================================================
# Part 5: Accessing Set Elements
# ===========================================================


# Sets do not support indexing

numbers = {10, 20, 30}


# This will cause an error:
# print(numbers[0])


# We use loops to access values

for number in numbers:
    print(number)



# ===========================================================
# Part 6: Set Operations
# ===========================================================


set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}



# Union
# Combine two sets

print(set1 | set2)



# Intersection
# Common elements

print(set1 & set2)



# Difference
# Elements in set1 but not set2

print(set1 - set2)



# ===========================================================
# Part 7: Useful Set Methods
# ===========================================================


numbers = {10, 20, 30, 40}


# len()
# Number of elements

print(len(numbers))



# in
# Check if value exists

print(20 in numbers)

print(100 in numbers)



# ===========================================================
# Part 8: Convert List to Set
# ===========================================================


# Remove duplicates from a list

numbers = [10, 20, 20, 30, 30, 40]


unique_numbers = set(numbers)


print(unique_numbers)



# ===========================================================
# Practice
# ===========================================================


# Create a set called:
# favorite_languages

# Add:
# Python
# Java
# C++

# Remove one language

# Check if Python exists

# Convert this list to set:
# [1,2,2,3,3,4]