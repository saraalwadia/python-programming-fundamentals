###########################################################
# String Methods
#capitalize()
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
# islower()
# isupper()
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
# isalnumeric()
###########################################################

# Strings have built-in methods that allow us
# to modify and analyze text.

myString = "Hello World From PYTHON"


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


# len():
# Returns the number of characters in the string

print(len(myString))


# find():
# Searches for a word and returns its position
# Returns -1 if the word is not found

print(myString.find("World"))


# index():
# Similar to find(), but gives an error
# if the word does not exist

print(myString.index("World"))


# isupper():
# Checks if all characters are uppercase

print(myString.isupper())


# islower():
# Checks if all characters are lowercase

print(myString.islower())


# replace():
# Replaces part of a string with another value

print(myString.replace("PYTHON", "Java"))

# The original string does not change
# because strings are immutable

print(myString)


# title():
# Makes the first letter of each word uppercase

print(myString.title())


# istitle():
# Checks if the string is written in title format

print(myString.istitle())


# isspace():
# Checks if the string contains only spaces

sp = "   "

print(sp.isspace())

# islower():
# Checks if all characters are lowercase
islower_string = "hello world"
print(islower_string.islower())  # Output: True

islower_string2 = "Hello World"
print(islower_string2.islower())  # Output: False

# isupper():
# Checks if all characters are uppercase
isupper_string = "HELLO WORLD"
print(isupper_string.isupper())  # Output: True

isupper_string2 = "Hello World"
print(isupper_string2.isupper())  # Output: False


# strip():
# Removes whitespace from the beginning and end of a string
strped_string = "   Hello World   "
print(strped_string.strip())

# lstrip():
# Removes whitespace from the beginning of a string
print(strped_string.lstrip())

# rstrip():
# Removes whitespace from the end of a string
print(strped_string.rstrip())

# strip("#"):
# Removes the specified character from the beginning and end of a string
strped_string2 = "###Hello World###"    
print(strped_string2.strip("#"))

# split():
# Splits a string into a list of substrings based on a specified delimiter
sentence = "Hello World From Python"
print(sentence.split(" "))

# split() with a different delimiter
sentence2 = "apple,banana,orange,grape"
print(sentence2.split(","))

# join():
# Joins a list of strings into a single string with a specified delimiter
joined_string = " ".join(["Hello", "World", "From", "Python"])
print(joined_string)

joined_string2 = "-".join(["apple", "banana", "orange", "grape"])
print(joined_string2)


# zfill():
# Pads a string with zeros on the left until it reaches a specified length
number = "42"
print(number.zfill(5))  # Output: 00042

# swapcase():
# Swaps the case of each character in the string
swapcase_string = "Hello World"
print(swapcase_string.swapcase())  # Output: hELLO wORLD

# count():
# Counts the number of occurrences of a substring in the string
count_string = "Hello World, Hello Python"
print(count_string.count("Hello"))  # Output: 2

# startswith():
# Checks if the string starts with a specified substring
print(count_string.startswith("Hello"))  # Output: True

# isalpha():
# Checks if all characters in the string are alphabetic
alpha_string = "HelloWorld"
print(alpha_string.isalpha())  # Output: True

alpha_string2 = "Hello World"
print(alpha_string2.isalpha())  # Output: False

# isnumeric():
# Checks if all characters in the string are numeric
numeric_string = "12345"
print(numeric_string.isnumeric())  # Output: True

numeric_string2 = "12345abc"
print(numeric_string2.isnumeric())  # Output: False