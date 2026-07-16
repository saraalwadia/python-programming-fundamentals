# ===========================================================
# Lesson: Tuples in Python
# ===========================================================


"""
Teaching Notes:


Lesson Objectives:

- Understand what tuples are.
- Learn how to create tuples.
- Access tuple elements using indexing.
- Understand slicing.
- Learn why tuples are immutable.
- Compare tuples and lists.



What is a Tuple?

A tuple is a collection used to store multiple values
inside one variable.


Example:

colors = ("Red", "Green", "Blue")



Tuple vs List:

List:
- Uses []
- Mutable (can be changed)
- Has many methods


Tuple:
- Uses ()
- Immutable (cannot be changed)
- Has fewer methods



Why use Tuples?

- Store data that should not change.
- Protect fixed values from modification.
- Usually faster than lists for fixed data.


Examples:

- Days of week
- Coordinates
- Configuration values



-----------------------------------------------------------

Creating Tuples:

Multiple values:

colors = ("Red", "Green", "Blue")


Single value tuple:

number = (5,)


Important:

The comma is required.

(5) --> Integer

(5,) --> Tuple



-----------------------------------------------------------

Tuple Indexing:

Tuples are ordered.

Index starts from 0.


Example:

tuple = ("A", "B", "C")


0 --> A

1 --> B

2 --> C



Negative indexing:

-1 --> Last element



-----------------------------------------------------------

Tuple Immutability:

Tuples cannot be modified after creation.


This is not allowed:

tuple[0] = value


Because tuples are immutable.


-----------------------------------------------------------

Tuple Methods:

Because tuples cannot change,
they only have two methods:


1. count()

Counts occurrences.


2. index()

Returns the position of a value.



-----------------------------------------------------------

Tuple Packing:

Putting multiple values into one tuple.


Example:

student = "Sara", 23, "IT"



Tuple Unpacking:

Extracting values from tuple into variables.


Example:

name, age, major = student



"""



###########################################################
# Part 1: Creating Tuples
###########################################################


# Create a tuple with multiple values


colors = ("Red", "Green", "Blue")


print(colors)



# Check the type


print(type(colors))




###########################################################
# Part 2: Accessing Tuple Elements
###########################################################


# Tuples use indexing like lists.
# Index starts from 0.



print(colors[0])


print(colors[1])


print(colors[-1])




###########################################################
# Part 3: Tuple Length
###########################################################


# len() returns the number of elements


print(len(colors))




###########################################################
# Part 4: Tuple Slicing
###########################################################


# Slicing works the same way as lists.


numbers = (10, 20, 30, 40, 50)



print(numbers[1:])


print(numbers[:3])


print(numbers[1:4])


print(numbers[::2])




###########################################################
# Part 5: Tuple is Immutable
###########################################################


# Tuples cannot be modified after creation.



numbers = (10, 20, 30)



# This will cause an error:

# numbers[0] = 100



print(numbers)




###########################################################
# Part 6: Creating a Single Element Tuple
###########################################################


# A comma is required when creating
# a tuple with one element.



single_tuple = (5,)



print(single_tuple)


print(type(single_tuple))



# Without comma, Python considers it an integer



not_tuple = (5)



print(not_tuple)


print(type(not_tuple))




###########################################################
# Part 7: Tuple Methods
###########################################################


# Tuples have only two methods:

# count()
# index()



numbers = (10, 20, 30, 20, 40)



# count()
# Returns how many times a value appears


print(numbers.count(20))



# index()
# Returns position of first occurrence


print(numbers.index(30))




###########################################################
# Part 8: Tuple Packing
###########################################################


# Packing:
# Storing multiple values into one tuple.



student = "Sara", 23, "IT"



print(student)




###########################################################
# Part 9: Tuple Unpacking
###########################################################


# Unpacking:
# Extracting tuple values into variables.



name, age, major = student



print(name)


print(age)


print(major)




###########################################################
# Part 10: Tuple vs List
###########################################################


# List:
# - Mutable
# - Uses []
# - More methods



my_list = [1, 2, 3]



# Tuple:
# - Immutable
# - Uses ()
# - Fewer methods



my_tuple = (1, 2, 3)



print(my_list)


print(my_tuple)




###########################################################
# Practice
###########################################################


"""
Practice Tasks:


1. Create a tuple:

favorite_movies


Add three movie names.


2. Print:

- Complete tuple.
- First movie.
- Number of movies.


3. Try to change one movie.

Observe the error and explain why it happens.


4. Create:

student = ("Sara", 23, "IT")


Unpack the tuple into:

name

age

major

"""
