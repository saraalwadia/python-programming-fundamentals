# ===========================================================
# Lesson: String Methods
# ===========================================================


"""
Teaching Notes:

Lesson Objectives:
- Understand built-in string methods in Python.
- Learn how to modify and analyze strings.
- Practice methods used for:
    - Changing string format
    - Searching inside strings
    - Checking string content
    - Removing spaces
    - Splitting and joining strings

Important Notes:
- String methods are functions that belong to string objects.
- Methods are called using the dot operator (.)

Example:

string.method()

Example:

name.upper()


Important Concept:
- Strings are immutable.
- String methods do not modify the original string.
- They return a new string.

Example:

text = "hello"

text.upper()

The original text is still:
hello


Categories of String Methods:

1. Changing Case:
- capitalize()
- upper()
- lower()
- title()
- swapcase()


2. Searching:
- find()
- index()
- count()
- startswith()


3. Checking Content:
- isupper()
- islower()
- istitle()
- isspace()
- isalpha()
- isnumeric()


4. Modifying Strings:
- replace()
- strip()
- lstrip()
- rstrip()


5. Splitting and Joining:
- split()
- join()


6. Formatting:
- zfill()


"""



###########################################################
# String Methods
###########################################################

# capitalize()
# upper()
# lower()
# len()
# find()
# index()
# isupper()
# islower()
# replace()
# title()
# istitle()
# isspace()
# strip()
# lstrip()
# rstrip()
# split()
# join()
# zfill()
# swapcase()
# count()
# startswith()
# isalpha()
# isnumeric()
# isalnum()


###########################################################
# Part 1: Creating String
###########################################################

# Strings have built-in methods that allow us
# to modify and analyze text.

myString = "Hello World From PYTHON"



###########################################################
# Part 2: Changing String Case
###########################################################


# capitalize():
# Makes the first character uppercase
# and the rest lowercase

print(myString.capitalize())



# upper():
# Converts all characters to uppercase

print(myString.upper())



# lower():
# Converts all characters to lowercase

print(myString.lower())



# title():
# Makes the first letter of each word uppercase

print(myString.title())



# swapcase():
# Converts uppercase characters to lowercase
# and lowercase characters to uppercase

swapcase_string = "Hello World"

print(swapcase_string.swapcase())




###########################################################
# Part 3: String Length
###########################################################


# len():
# Returns the number of characters in the string

print(len(myString))




###########################################################
# Part 4: Searching Inside Strings
###########################################################


# find():
# Searches for a word and returns its position
# Returns -1 if the word is not found

print(myString.find("World"))



# index():
# Similar to find()
# Gives an error if the word does not exist

print(myString.index("World"))



# count():
# Counts how many times a substring appears

count_string = "Hello World, Hello Python"

print(count_string.count("Hello"))



# startswith():
# Checks if the string starts with a specific value

print(count_string.startswith("Hello"))




###########################################################
# Part 5: Checking String Content
###########################################################


# isupper():
# Checks if all characters are uppercase

print(myString.isupper())



# islower():
# Checks if all characters are lowercase

print(myString.islower())



# istitle():
# Checks if the string follows title format

print(myString.istitle())



# isspace():
# Checks if the string contains only spaces

sp = "   "

print(sp.isspace())



# isalpha():
# Checks if all characters are letters

alpha_string = "HelloWorld"

print(alpha_string.isalpha())


alpha_string2 = "Hello World"

print(alpha_string2.isalpha())



# isnumeric():
# Checks if all characters are numbers

numeric_string = "12345"

print(numeric_string.isnumeric())


numeric_string2 = "12345abc"

print(numeric_string2.isnumeric())




###########################################################
# Part 6: Replacing Text
###########################################################


# replace():
# Replaces part of a string with another value

print(myString.replace("PYTHON", "Java"))


# The original string does not change
# because strings are immutable

print(myString)




###########################################################
# Part 7: Removing Spaces
###########################################################


# strip():
# Removes whitespace from beginning and end

strped_string = "   Hello World   "

print(strped_string.strip())



# lstrip():
# Removes whitespace from the beginning

print(strped_string.lstrip())



# rstrip():
# Removes whitespace from the end

print(strped_string.rstrip())



# strip("#"):
# Removes the specified character

strped_string2 = "###Hello World###"

print(strped_string2.strip("#"))




###########################################################
# Part 8: Split and Join
###########################################################


# split():
# Converts string into a list
# based on a separator

sentence = "Hello World From Python"

print(sentence.split(" "))



# split() with different delimiter

sentence2 = "apple,banana,orange,grape"

print(sentence2.split(","))



# join():
# Combines list elements into one string

joined_string = " ".join(
    ["Hello", "World", "From", "Python"]
)

print(joined_string)



joined_string2 = "-".join(
    ["apple", "banana", "orange", "grape"]
)

print(joined_string2)




###########################################################
# Part 9: zfill()
###########################################################


# zfill():
# Adds zeros to the left side
# until reaching the required length


number = "42"

print(number.zfill(5))

# Output:
# 00042




###########################################################
# Practice
###########################################################


"""
Practice Tasks:

1. Create a variable:

text = "python programming"


Apply:
- upper()
- title()
- replace()


2. Create:

sentence = "I love Python Python"


Find:
- Number of times Python appears.


3. Create:

name = "   Sara   "

Remove extra spaces.


4. Convert:

"Python,Java,C++"

into a list using split().

"""