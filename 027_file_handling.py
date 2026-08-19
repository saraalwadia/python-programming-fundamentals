###########################################################
# File Handling in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand what file handling is.
- Learn how to open files.
- Learn how to read files.
- Learn how to write to files.
- Learn how to append data to files.
- Understand file modes.
- Learn read(), readline(), and readlines().
- Learn how to use with open().
- Learn how to loop through a file.
- Handle file-related exceptions.
- Combine file handling with loops and functions.


Topics Covered:

PART 1:
What is File Handling?

PART 2:
Opening a File

PART 3:
File Modes

PART 4:
Reading a File

PART 5:
read()

PART 6:
readline()

PART 7:
readlines()

PART 8:
Loop Through a File

PART 9:
Writing to a File

PART 10:
Appending to a File

PART 11:
Using with open()

PART 12:
Checking if a File Exists

PART 13:
Exception Handling with Files

PART 14:
Functions with File Handling

PART 15:
Mini Project - Student Records

PART 16:
Practice Exercises
"""


# ===========================================================
# PART 1: What is File Handling?
# ===========================================================


"""
File handling means working with files using Python.

Python can:

- Create files.
- Read files.
- Write data to files.
- Add data to files.
- Modify file content.

Common file types:

.txt
.csv
.json
"""


# ===========================================================
# PART 2: Opening a File
# ===========================================================


"""
The open() function is used to open a file.

Syntax:

open(filename, mode)

Example:

file = open("data.txt", "r")

The file should exist when using "r".
"""


# -----------------------------------------------------------
# Example:
# This example is commented because the file may not exist.
# -----------------------------------------------------------


# file = open("data.txt", "r")
#
# print(file.read())
#
# file.close()


# ===========================================================
# PART 3: File Modes
# ===========================================================


"""
Common file modes:

"r" -> Read
"w" -> Write
"a" -> Append
"x" -> Create a new file


r:
- Opens the file for reading.
- The file must already exist.


w:
- Opens the file for writing.
- Creates the file if it does not exist.
- Deletes the old content if the file already exists.


a:
- Opens the file for adding new content.
- New content is added at the end.


x:
- Creates a new file.
- Causes an error if the file already exists.
"""


# ===========================================================
# PART 4: Creating and Writing a File
# ===========================================================


"""
Using "w" allows us to write data to a file.

If the file does not exist,
Python will create it.
"""


file = open("example.txt", "w")

file.write("Hello Python!")

file.close()


# ===========================================================
# PART 5: Writing Multiple Lines
# ===========================================================


file = open("students.txt", "w")

file.write("Sara\n")

file.write("Joe\n")

file.write("Ali\n")

file.write("Mohammed\n")

file.close()


# \n means a new line.


# ===========================================================
# PART 6: Reading a File
# ===========================================================


file = open("students.txt", "r")

content = file.read()

print(content)

file.close()


# ===========================================================
# PART 7: read()
# ===========================================================


"""
read() reads the entire file.
"""


file = open("students.txt", "r")

content = file.read()

print(content)

file.close()


# ===========================================================
# PART 8: readline()
# ===========================================================


"""
readline() reads one line at a time.
"""


file = open("students.txt", "r")

line1 = file.readline()

line2 = file.readline()

print(line1)

print(line2)

file.close()


# ===========================================================
# PART 9: readlines()
# ===========================================================


"""
readlines() reads all lines
and returns them as a list.
"""


file = open("students.txt", "r")

lines = file.readlines()

print(lines)

file.close()


# ===========================================================
# PART 10: Loop Through a File
# ===========================================================


"""
A file can be treated as a sequence of lines.

We can use a for loop to read
each line separately.
"""


file = open("students.txt", "r")


for line in file:

    print(line)


file.close()


# ===========================================================
# PART 11: Remove Extra New Lines
# ===========================================================


"""
Each line read from a text file
usually contains \n at the end.

strip() can remove extra spaces
and newline characters.
"""


file = open("students.txt", "r")


for line in file:

    print(line.strip())


file.close()


# ===========================================================
# PART 12: Append Data to a File
# ===========================================================


"""
"a" means append.

New data is added to the end
of the existing file.

The old content is not deleted.
"""


file = open("students.txt", "a")

file.write("John\n")

file.close()


# Check the updated file.


file = open("students.txt", "r")

print(file.read())

file.close()


# ===========================================================
# PART 13: Using with open()
# ===========================================================


"""
The recommended way to work with files
is to use:

with open()

Python automatically closes the file
after the block finishes.
"""


with open("students.txt", "r") as file:

    content = file.read()

    print(content)


# No need to use:
#
# file.close()


# ===========================================================
# PART 14: Write Using with open()
# ===========================================================


with open("message.txt", "w") as file:

    file.write("Hello from Python!")


# ===========================================================
# PART 15: Append Using with open()
# ===========================================================


with open("message.txt", "a") as file:

    file.write("\nWelcome to Python.")


# ===========================================================
# PART 16: Read Using with open()
# ===========================================================


with open("message.txt", "r") as file:

    content = file.read()

    print(content)


# ===========================================================
# PART 17: File Not Found
# ===========================================================


"""
When we try to read a file that does not exist,
Python raises FileNotFoundError.

The following example is commented
because the file may not exist.
"""


# with open("unknown_file.txt", "r") as file:
#
#     content = file.read()
#
#     print(content)


# ===========================================================
# PART 18: Exception Handling with Files
# ===========================================================


"""
We can use try / except
to handle file errors.
"""


try:

    with open("unknown_file.txt", "r") as file:

        content = file.read()

        print(content)


except FileNotFoundError:

    print("The file was not found.")


# ===========================================================
# PART 19: Check if File Exists
# ===========================================================


"""
We can use the os module
to check whether a file exists.
"""


import os


if os.path.exists("students.txt"):

    print("The file exists.")


else:

    print("The file does not exist.")


# ===========================================================
# PART 20: Delete a File
# ===========================================================


"""
The os.remove() function can be used
to delete a file.

The example below is commented
to avoid accidentally deleting a file.
"""


# if os.path.exists("example.txt"):
#
#     os.remove("example.txt")
#
#     print("File deleted.")


# ===========================================================
# PART 21: Write a List to a File
# ===========================================================


students = [
    "Sara",
    "Joe",
    "Ali",
    "Mohammed"
]


with open("students_list.txt", "w") as file:

    for student in students:

        file.write(student + "\n")


# ===========================================================
# PART 22: Read a File into a List
# ===========================================================


students = []


with open("students_list.txt", "r") as file:

    for line in file:

        students.append(line.strip())


print(students)


# ===========================================================
# PART 23: Functions with File Handling
# ===========================================================


"""
We can create functions
to make file operations reusable.
"""


def write_to_file(filename, text):

    with open(filename, "w") as file:

        file.write(text)


def read_from_file(filename):

    with open(filename, "r") as file:

        return file.read()


write_to_file(
    "function_example.txt",
    "Hello from a function!"
)


content = read_from_file("function_example.txt")


print(content)


# ===========================================================
# PART 24: Count Lines in a File
# ===========================================================


def count_lines(filename):

    count = 0

    with open(filename, "r") as file:

        for line in file:

            count += 1

    return count


print(
    "Number of lines:",
    count_lines("students.txt")
)


# ===========================================================
# PART 25: Search for a Name in a File
# ===========================================================


def search_name(filename, name):

    with open(filename, "r") as file:

        for line in file:

            if line.strip() == name:

                return True

    return False


print(
    search_name("students.txt", "Sara")
)


print(
    search_name("students.txt", "Unknown")
)


# ===========================================================
# PART 26: Mini Project - Student Records
# ===========================================================


"""
Mini Project:

Create a simple student records program.

The program should:

1. Ask the user for a student name.
2. Ask for the student's mark.
3. Save the information to a file.
4. Read the file.
5. Display the saved information.

We will use:

- input()
- functions
- with open()
- append mode
- read mode
"""


def add_student():

    name = input("Enter student name: ")

    mark = float(input("Enter student mark: "))


    with open("student_records.txt", "a") as file:

        file.write(
            f"{name},{mark}\n"
        )


def show_students():

    try:

        with open("student_records.txt", "r") as file:

            for line in file:

                print(line.strip())


    except FileNotFoundError:

        print("No student records found.")


try:

    add_student()

    print("\nStudent Records:")

    show_students()


except ValueError:

    print("Mark must be a number.")


# ===========================================================
# PART 27: Mini Project - Simple Notes App
# ===========================================================


"""
Simple Notes Application:

The user can enter a note.

The note will be saved to a file.
"""


def add_note():

    note = input("Enter your note: ")

    with open("notes.txt", "a") as file:

        file.write(note + "\n")


def show_notes():

    try:

        with open("notes.txt", "r") as file:

            for note in file:

                print("-", note.strip())


    except FileNotFoundError:

        print("No notes found.")


# Add a note.


add_note()


# Display all notes.


print("\nYour Notes:")

show_notes()


# ===========================================================
# PART 28: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a file called "hello.txt".
#
# Write:
#
# Hello Python
#
# into the file.
# -----------------------------------------------------------


# Exercise 2:
#
# Create a file called "names.txt".
#
# Write the following names:
#
# Sara
# Joe
# Ali
# Mohammed
#
# Each name should be on a separate line.
# -----------------------------------------------------------


# Exercise 3:
#
# Read "names.txt"
# and print all names.
# -----------------------------------------------------------


# Exercise 4:
#
# Add a new name to "names.txt"
# without deleting the existing names.
#
# Use append mode.
# -----------------------------------------------------------


# Exercise 5:
#
# Count how many lines exist
# in "names.txt".
# -----------------------------------------------------------


# Exercise 6:
#
# Ask the user for a name.
#
# Search for the name in "names.txt".
#
# Print:
#
# "Found"
#
# or:
#
# "Not Found"
# -----------------------------------------------------------


# Exercise 7:
#
# Create a function called:
#
# save_names(names)
#
# The function should receive
# a list of names and save them to a file.
# -----------------------------------------------------------


# Exercise 8:
#
# Create a function called:
#
# read_names()
#
# The function should read the file
# and return the names as a list.
# -----------------------------------------------------------


# Exercise 9:
#
# Create a program that asks the user
# for a sentence and saves it to a file.
#
# Then read the sentence from the file
# and print it.
# -----------------------------------------------------------


# Exercise 10:
#
# Create a simple To-Do List application.
#
# The program should:
#
# 1. Ask the user for a task.
# 2. Save the task to a file.
# 3. Display all saved tasks.
#
# Use functions.
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


"""
File Handling Summary:

We learned:

- open()
- "r" -> read
- "w" -> write
- "a" -> append
- "x" -> create
- read()
- readline()
- readlines()
- write()
- with open()
- strip()
- for loop with files
- os.path.exists()
- os.remove()
- FileNotFoundError
- File handling with functions
- Saving lists to files
- Reading files into lists
- Building simple file-based applications


Important:

Always prefer:

with open("file.txt", "r") as file:

    ...

because Python automatically closes
the file after the block finishes.
"""


###########################################################
# END OF FILE HANDLING
###########################################################