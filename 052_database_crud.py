###########################################################
# SQLite Database in Python
###########################################################


"""
SQLite is a simple database system included with Python.

A database is used to store data in an organized way.

In this lesson we will learn how to:

- Create a database
- Create a table
- Insert data
- Read data
- Search data
- Update data
- Delete data
- Work with multiple records

Before using SQLite, we need to import sqlite3.
"""


# ===========================================================
# PART 1: Import sqlite3
# ===========================================================


"""
sqlite3 is a built-in Python module.

It allows us to work with SQLite databases.

No additional installation is required.
"""


import sqlite3


# ===========================================================
# PART 2: Connect to a Database
# ===========================================================


"""
connect() is used to connect to a database.

If the database does not exist,
SQLite will create it automatically.
"""


connection = sqlite3.connect("school.db")


print("Database connected successfully!")


# ===========================================================
# PART 3: Create a Cursor
# ===========================================================


"""
A cursor is used to execute SQL commands.

We use the cursor to:

- Create tables
- Insert data
- Read data
- Update data
- Delete data
"""


cursor = connection.cursor()


# ===========================================================
# PART 4: Create a Table
# ===========================================================


"""
A table stores data in rows and columns.

Our students table will contain:

id
name
age
major
gpa
"""


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    major TEXT,
    gpa REAL
)
""")


connection.commit()


print("Students table created!")


# ===========================================================
# PART 5: Insert Data
# ===========================================================


"""
INSERT INTO is used to add data to a table.

The ? symbols are placeholders.

Using placeholders is safer than building SQL
queries directly with user input.
"""


cursor.execute("""
INSERT INTO students
(name, age, major, gpa)
VALUES (?, ?, ?, ?)
""", (
    "Sara",
    22,
    "Information Technology",
    93.5
))


connection.commit()


print("Student added successfully!")


# ===========================================================
# PART 6: Insert Multiple Records
# ===========================================================


"""
executemany() allows us to insert
multiple records at once.
"""


students = [
    ("Ahmad", 21, "Computer Science", 88.5),
    ("Lina", 23, "Information Technology", 91.2),
    ("Omar", 20, "Software Engineering", 85.7)
]


cursor.executemany("""
INSERT INTO students
(name, age, major, gpa)
VALUES (?, ?, ?, ?)
""", students)


connection.commit()


print("Multiple students added!")


# ===========================================================
# PART 7: SELECT - Read Data
# ===========================================================


"""
SELECT is used to read data from a table.

SELECT * means:

Select all columns.
"""


cursor.execute("""
SELECT * FROM students
""")


students = cursor.fetchall()


print("\nAll Students:")


for student in students:

    print(student)


# ===========================================================
# PART 8: Select Specific Columns
# ===========================================================


"""
We do not always need all columns.

We can select only the columns we need.
"""


cursor.execute("""
SELECT name, major, gpa
FROM students
""")


students = cursor.fetchall()


print("\nStudent Information:")


for student in students:

    print(
        "Name:",
        student[0],
        "| Major:",
        student[1],
        "| GPA:",
        student[2]
    )


# ===========================================================
# PART 9: WHERE
# ===========================================================


"""
WHERE is used to filter records.

Example:

Find students whose GPA is greater than 90.
"""


cursor.execute("""
SELECT *
FROM students
WHERE gpa > ?
""", (90,))


students = cursor.fetchall()


print("\nStudents with GPA greater than 90:")


for student in students:

    print(student)


# ===========================================================
# PART 10: Search by Name
# ===========================================================


"""
We can use WHERE to search for
a specific student.
"""


name = "Sara"


cursor.execute("""
SELECT *
FROM students
WHERE name = ?
""", (name,))


student = cursor.fetchone()


print("\nSearch Result:")


print(student)


# ===========================================================
# PART 11: fetchone()
# ===========================================================


"""
fetchone() returns one record.

It is useful when we expect
one result.
"""


cursor.execute("""
SELECT *
FROM students
WHERE name = ?
""", ("Lina",))


student = cursor.fetchone()


print("\nOne Student:")


print(student)


# ===========================================================
# PART 12: fetchall()
# ===========================================================


"""
fetchall() returns all records
returned by the query.
"""


cursor.execute("""
SELECT *
FROM students
""")


students = cursor.fetchall()


print("\nAll Records:")


for student in students:

    print(student)


# ===========================================================
# PART 13: UPDATE Data
# ===========================================================


"""
UPDATE is used to change existing data.

Here we will change Sara's GPA.
"""


cursor.execute("""
UPDATE students
SET gpa = ?
WHERE name = ?
""", (
    95.0,
    "Sara"
))


connection.commit()


print("\nStudent updated successfully!")


# Check the updated student


cursor.execute("""
SELECT *
FROM students
WHERE name = ?
""", ("Sara",))


student = cursor.fetchone()


print(student)


# ===========================================================
# PART 14: DELETE Data
# ===========================================================


"""
DELETE is used to remove records.

Here we will delete Omar.
"""


cursor.execute("""
DELETE FROM students
WHERE name = ?
""", ("Omar",))


connection.commit()


print("\nStudent deleted successfully!")


# ===========================================================
# PART 15: Count Records
# ===========================================================


"""
COUNT() is used to count records.

It can be useful for statistics
and dashboards.
"""


cursor.execute("""
SELECT COUNT(*)
FROM students
""")


total_students = cursor.fetchone()[0]


print(
    "\nTotal Students:",
    total_students
)


# ===========================================================
# PART 16: Sorting Data
# ===========================================================


"""
ORDER BY is used to sort data.

ASC  = Ascending
DESC = Descending
"""


cursor.execute("""
SELECT name, gpa
FROM students
ORDER BY gpa DESC
""")


students = cursor.fetchall()


print("\nStudents Sorted by GPA:")


for student in students:

    print(
        "Name:",
        student[0],
        "| GPA:",
        student[1]
    )


# ===========================================================
# PART 17: Working with User Input
# ===========================================================


"""
We can combine Python input()
with a database.

The user can enter information,
and we can store it in the database.
"""


name = input("\nEnter student name: ")

age = int(
    input("Enter student age: ")
)

major = input(
    "Enter student major: "
)

gpa = float(
    input("Enter student GPA: ")
)


cursor.execute("""
INSERT INTO students
(name, age, major, gpa)
VALUES (?, ?, ?, ?)
""", (
    name,
    age,
    major,
    gpa
))


connection.commit()


print(
    "New student added successfully!"
)


# ===========================================================
# PART 18: Display Final Data
# ===========================================================


"""
Let's display all students
after the previous operations.
"""


cursor.execute("""
SELECT *
FROM students
""")


students = cursor.fetchall()


print("\nFinal Students List:")


for student in students:

    print(student)


# ===========================================================
# PART 19: Close the Database
# ===========================================================


"""
When we finish working with the database,
we should close the connection.
"""


connection.close()


print("\nDatabase connection closed.")


# ===========================================================
# PART 20: Important Database Commands
# ===========================================================


"""
sqlite3.connect()
Used to connect to a database.


cursor()
Creates a cursor for executing SQL commands.


execute()
Executes an SQL command.


executemany()
Executes a command multiple times.


commit()
Saves changes to the database.


fetchone()
Returns one record.


fetchall()
Returns all records.


close()
Closes the database connection.


Common SQL commands:

CREATE TABLE
Creates a table.


INSERT INTO
Adds data.


SELECT
Reads data.


WHERE
Filters data.


UPDATE
Changes existing data.


DELETE
Removes data.


ORDER BY
Sorts data.


COUNT()
Counts records.
"""


# ===========================================================
# PART 21: Database Structure
# ===========================================================


"""
A database contains tables.

A table contains:

Columns
Rows

Example:

students

+----+-------+-----+----------------------+------+
| id | name  | age | major                | gpa  |
+----+-------+-----+----------------------+------+
| 1  | Sara  | 22  | Information Tech.   | 95.0 |
| 2  | Ahmad | 21  | Computer Science    | 88.5 |
+----+-------+-----+----------------------+------+

Each row represents one record.

Each column represents one piece of information.
"""


# ===========================================================
# PART 22: Important Data Types
# ===========================================================


"""
Common SQLite data types:

INTEGER
Used for whole numbers.

Example:
age = 22


REAL
Used for decimal numbers.

Example:
gpa = 93.5


TEXT
Used for strings.

Example:
name = "Sara"


NULL
Represents a missing value.
"""


# ===========================================================
# PART 23: Primary Key
# ===========================================================


"""
A Primary Key uniquely identifies
each record in a table.

In our students table:

id INTEGER PRIMARY KEY AUTOINCREMENT

This means:

- Each student has a unique ID.
- The ID is automatically generated.
"""


# ===========================================================
# PART 24: CRUD Operations
# ===========================================================


"""
CRUD is a common term used in database applications.

C = Create
R = Read
U = Update
D = Delete


Create:
INSERT


Read:
SELECT


Update:
UPDATE


Delete:
DELETE


These four operations are very important
when building real-world applications.
"""


# ===========================================================
# PART 25: Practical Example - Search Student
# ===========================================================


"""
Ask the user for a student name
and search for that student.
"""


search_name = input(
    "\nEnter a name to search: "
)


connection = sqlite3.connect(
    "school.db"
)

cursor = connection.cursor()


cursor.execute("""
SELECT *
FROM students
WHERE name = ?
""", (search_name,))


student = cursor.fetchone()


if student:

    print(
        "Student found:"
    )

    print(student)

else:

    print(
        "Student not found."
    )


connection.close()


# ===========================================================
# PART 26: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a database called:
#
# shop.db
#
# Create a table called:
#
# products
#
# The table should contain:
#
# id
# name
# price
# quantity
#
# -----------------------------------------------------------


# Exercise 2:
#
# Add at least 5 products
# to the products table.
#
# -----------------------------------------------------------


# Exercise 3:
#
# Display all products.
#
# -----------------------------------------------------------


# Exercise 4:
#
# Ask the user to enter
# a product name.
#
# Search for that product
# in the database.
#
# -----------------------------------------------------------


# Exercise 5:
#
# Update the price of a product.
#
# -----------------------------------------------------------


# Exercise 6:
#
# Delete a product
# from the database.
#
# -----------------------------------------------------------


# Exercise 7:
#
# Count the total number
# of products.
#
# -----------------------------------------------------------


# Exercise 8:
#
# Display products sorted
# by price from highest
# to lowest.
#
# -----------------------------------------------------------


# Exercise 9:
#
# Create a simple
# Product Management program
# that allows the user to:
#
# 1. Add Product
# 2. View Products
# 3. Search Product
# 4. Update Product
# 5. Delete Product
# 6. Exit
#
# Use SQLite to store the data.


###########################################################
# END OF SQLITE DATABASE
###########################################################