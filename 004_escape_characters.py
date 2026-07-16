# ===========================================================
# Lesson 04
# Escape Characters in Python
# ===========================================================


"""
Teaching Notes:

Lesson Objectives:
- Understand what escape characters are.
- Learn how to use special characters inside strings.
- Understand how Python handles line breaks and formatting.

Topics Covered:

PART 1: What are Escape Characters?
- Escape characters are special characters used inside strings.
- They start with a backslash (\).
- They allow us to add special formatting to text.

PART 2: Common Escape Characters:
- \n  -> New line
- \t  -> Tab space
- \\  -> Backslash character
- \"  -> Double quote inside a string
- \'  -> Single quote inside a string
- \r  -> Carriage return

PART 3: Using Quotes Inside Strings
- We can use escape characters when the quote type
  is the same as the string quote.

PART 4: Carriage Return (\r)
- Moves the cursor back to the beginning of the line.
- The next characters overwrite existing characters.

Important Notes:
- Escape characters only work inside strings.
- The backslash tells Python that the next character
  has a special meaning.

Common Mistakes:
- Forgetting the backslash.
- Confusing \n with normal text.
- Expecting \r to create a new line.

"""


# ===========================================================
# PART 1: New Line (\n)
# ===========================================================


# \n moves the text to a new line

print("Hello\nWorld")


# Output:
# Hello
# World



# ===========================================================
# PART 2: Tab Space (\t)
# ===========================================================


# \t adds a tab space

print("Name:\tSara")

print("Age:\t23")



# Example: Creating formatted text

print("Name\tAge")

print("Sara\t23")



# ===========================================================
# PART 3: Backslash (\\)
# ===========================================================


# \\ is used to print a backslash character

print("C:\\Users\\Sara\\Python")



# ===========================================================
# PART 4: Double Quotes Inside Strings (\")
# ===========================================================


# When the string uses double quotes,
# we need escape character for inner quotes.

print("He said \"Hello Python\"")



# Another solution:
# Use single quotes outside

print('He said "Hello Python"')



# ===========================================================
# PART 5: Single Quotes Inside Strings (\')
# ===========================================================


# When the string uses single quotes,
# we need escape character for inner single quotes.

print('It\'s Python')



# Another solution:
# Use double quotes outside

print("It's Python")



# ===========================================================
# PART 6: Carriage Return (\r)
# ===========================================================


# \r returns the cursor to the beginning of the line.

print("Hello\rPython")


# Explanation:
# 1. Python prints Hello
# 2. Cursor returns to the beginning
# 3. Python overwrites characters with Python



# Another example:

print("123456\rABC")


# Output behavior:
# ABC456



# ===========================================================
# PART 7: Combining Escape Characters
# ===========================================================


student_card = "Name:\tSara\nAge:\t23\nMajor:\tIT"


print(student_card)



# ===========================================================
# Practice
# ===========================================================


# 1. Print your name and age on separate lines using \n.


# 2. Create a formatted student card using:
#    \t and \n


# 3. Print this sentence:
#    Sara said "I love Python"


# 4. Print a Windows path:
#    C:\Python\Projects


# 5. Try different examples using \r
#    and observe the output.