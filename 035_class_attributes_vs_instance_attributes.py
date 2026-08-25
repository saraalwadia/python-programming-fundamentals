###########################################################
# Class Attributes vs Instance Attributes in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand what an attribute is.
- Learn the difference between class attributes
  and instance attributes.
- Understand shared data between objects.
- Understand unique data for each object.
- Learn how class attributes can be changed.
- Learn how instance attributes can be changed.
- Understand the difference between changing
  a class attribute and an instance attribute.


Topics Covered:

PART 1:
What is an Attribute?

PART 2:
Class Attributes

PART 3:
Instance Attributes

PART 4:
Class Attributes vs Instance Attributes

PART 5:
Changing Class Attributes

PART 6:
Changing Instance Attributes

PART 7:
Using Both Types Together

PART 8:
Practical Examples

PART 9:
Practice Exercises
"""


# ===========================================================
# PART 1: What is an Attribute?
# ===========================================================


"""
An attribute is data that belongs
to a class or an object.

Example:

name
age
color
price
"""


class Person:

    name = "Sara"
    age = 23


person1 = Person()


print(person1.name)
print(person1.age)



# ===========================================================
# PART 2: Class Attributes
# ===========================================================


"""
A class attribute belongs to the class.

It is shared by all objects
created from that class.
"""


class Student:

    university = "University of Palestine"


student1 = Student()
student2 = Student()


print(student1.university)
print(student2.university)


"""
Both objects use the same value:

University of Palestine
"""



# ===========================================================
# PART 3: Instance Attributes
# ===========================================================


"""
An instance attribute belongs
to a specific object.

Instance attributes are usually
created inside __init__().
"""


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


student1 = Student("Sara", 23)
student2 = Student("Joe", 20)


print(student1.name)
print(student1.age)


print(student2.name)
print(student2.age)


"""
Each object has different data.

student1:

Sara
23


student2:

Joe
20
"""



# ===========================================================
# PART 4: Class Attribute and Instance Attribute Together
# ===========================================================


class Student:

    # Class Attribute

    university = "University of Palestine"


    def __init__(self, name, age):

        # Instance Attributes

        self.name = name
        self.age = age


student1 = Student("Sara", 23)
student2 = Student("Joe", 20)


print(student1.university)
print(student1.name)
print(student1.age)


print()


print(student2.university)
print(student2.name)
print(student2.age)



# ===========================================================
# PART 5: Understanding the Difference
# ===========================================================


"""
Class Attribute:

Shared by all objects.


Example:

university = "University of Palestine"



Instance Attribute:

Different for each object.


Example:

self.name = name
self.age = age
"""


class Car:

    # Shared by all cars

    wheels = 4


    def __init__(self, brand, color):

        # Different for each car

        self.brand = brand
        self.color = color


car1 = Car("Toyota", "Black")
car2 = Car("BMW", "Red")


print(car1.wheels)
print(car2.wheels)


print(car1.brand)
print(car1.color)


print(car2.brand)
print(car2.color)



# ===========================================================
# PART 6: Changing an Instance Attribute
# ===========================================================


class Person:

    def __init__(self, name):

        self.name = name


person1 = Person("Sara")
person2 = Person("Joe")


print(person1.name)
print(person2.name)


# Change person1 only

person1.name = "Adam"


print(person1.name)
print(person2.name)


"""
Changing an instance attribute
affects only that object.
"""



# ===========================================================
# PART 7: Changing a Class Attribute
# ===========================================================


class Student:

    university = "University of Palestine"


student1 = Student()
student2 = Student()


print(student1.university)
print(student2.university)


# Change the class attribute

Student.university = "New University"


print(student1.university)
print(student2.university)


"""
The class attribute changed.

Both objects now use:

New University
"""



# ===========================================================
# PART 8: Changing a Class Attribute Using an Object
# ===========================================================


class Car:

    wheels = 4


car1 = Car()
car2 = Car()


print(car1.wheels)
print(car2.wheels)


# Create an instance attribute for car1

car1.wheels = 6


print(car1.wheels)
print(car2.wheels)


"""
car1 now has its own wheels attribute.

car1:

6


car2:

4
"""


# ===========================================================
# PART 9: Accessing Class Attributes
# ===========================================================


class School:

    name = "University of Palestine"


# Access using the class

print(School.name)


# Access using an object

school1 = School()

print(school1.name)



# ===========================================================
# PART 10: Practical Example - Students
# ===========================================================


class Student:

    university = "University of Palestine"


    def __init__(self, name, major):

        self.name = name
        self.major = major


student1 = Student("Sara", "IT")
student2 = Student("Joe", "Computer Science")


print("Student 1")

print("Name:", student1.name)
print("Major:", student1.major)
print("University:", student1.university)


print()


print("Student 2")

print("Name:", student2.name)
print("Major:", student2.major)
print("University:", student2.university)



# ===========================================================
# PART 11: Practical Example - Employees
# ===========================================================


class Employee:

    company = "Google"


    def __init__(self, name, salary):

        self.name = name
        self.salary = salary


employee1 = Employee("Sara", 5000)
employee2 = Employee("Joe", 4000)


print(employee1.name)
print(employee1.salary)
print(employee1.company)


print()


print(employee2.name)
print(employee2.salary)
print(employee2.company)



# ===========================================================
# PART 12: Practical Example - Bank Account
# ===========================================================


class BankAccount:

    bank_name = "ABC Bank"


    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance


account1 = BankAccount("Sara", 1000)
account2 = BankAccount("Joe", 2000)


print(account1.owner)
print(account1.balance)
print(account1.bank_name)


print()


print(account2.owner)
print(account2.balance)
print(account2.bank_name)



# ===========================================================
# PART 13: Class Attribute with a Method
# ===========================================================


class Product:

    store = "Tech Store"


    def __init__(self, name, price):

        self.name = name
        self.price = price


    def display(self):

        print("Store:", self.store)
        print("Product:", self.name)
        print("Price:", self.price)


product1 = Product("Laptop", 1000)
product2 = Product("Mouse", 50)


product1.display()

print()

product2.display()



# ===========================================================
# PART 14: Important Example
# ===========================================================


class Student:

    university = "University A"


    def __init__(self, name):

        self.name = name


student1 = Student("Sara")
student2 = Student("Joe")


print(student1.university)
print(student2.university)


# Change the class attribute

Student.university = "University B"


print(student1.university)
print(student2.university)



# ===========================================================
# PART 15: Instance Attribute Overrides Class Attribute
# ===========================================================


class Car:

    color = "Black"


car1 = Car()
car2 = Car()


print(car1.color)
print(car2.color)


# Create an instance attribute

car1.color = "Red"


print(car1.color)
print(car2.color)


"""
The class attribute is:

Black


car1 created its own attribute:

Red


car2 still uses:

Black
"""



# ===========================================================
# PART 16: Comparison
# ===========================================================


"""
Class Attribute:

class Student:

    university = "University"


Shared by:

student1
student2
student3



Instance Attribute:

def __init__(self, name):

    self.name = name


Different for each object:

student1.name = "Sara"

student2.name = "Joe"

student3.name = "Ali"
"""



# ===========================================================
# PART 17: Visual Example
# ===========================================================


"""
                    Student
                       |
          -------------------------
          |                       |
     Class Attribute        Instance Attributes
          |                       |
     university              name
                             age


Objects:


student1                 student2

name: Sara               name: Joe
age: 23                  age: 20

university               university

University               University
(shared)                 (shared)
"""



# ===========================================================
# PART 18: Practical Example - Online Course
# ===========================================================


class Course:

    platform = "Online Learning"


    def __init__(self, name, hours):

        self.name = name
        self.hours = hours


course1 = Course("Python", 50)
course2 = Course("Machine Learning", 85)


print("Course:", course1.name)
print("Hours:", course1.hours)
print("Platform:", course1.platform)


print()


print("Course:", course2.name)
print("Hours:", course2.hours)
print("Platform:", course2.platform)



# ===========================================================
# PART 19: Practice Exercises
# ===========================================================


"""
Exercise 1:

Create a class called:

Student


Add a class attribute:

school


Create __init__() with:

name
age


Create two objects.

Print all information.


-----------------------------------------------------------


Exercise 2:

Create a class called:

Car


Add a class attribute:

wheels = 4


Create __init__() with:

brand
color


Create two cars.

Print their information.


-----------------------------------------------------------


Exercise 3:

Create a class called:

Employee


Add a class attribute:

company


Create __init__() with:

name
salary


Create two employees.

Print their information.


-----------------------------------------------------------


Exercise 4:

Create a class called:

Product


Add a class attribute:

store


Create __init__() with:

name
price


Create a method:

display()


Print:

Store
Product Name
Price


-----------------------------------------------------------


Exercise 5:

Create a class called:

University


Add a class attribute:

country


Create __init__() with:

name
students


Create two objects.

Print their information.


-----------------------------------------------------------


Exercise 6:

Create a class called:

Book


Add a class attribute:

language = "English"


Create __init__() with:

title
author


Create two books.

Print all information.


-----------------------------------------------------------


Exercise 7:

Create a class called:

BankAccount


Add a class attribute:

bank_name


Create __init__() with:

owner
balance


Create two accounts.

Print their information.
"""


# ===========================================================
# SUMMARY
# ===========================================================


"""
Class Attribute:

Belongs to the class.

Shared by all objects.


Example:

class Student:

    university = "University"



Instance Attribute:

Belongs to an object.

Each object can have different data.


Example:

class Student:

    def __init__(self, name):

        self.name = name



Example:


class Student:

    university = "University"


    def __init__(self, name):

        self.name = name


student1 = Student("Sara")
student2 = Student("Joe")


student1.name

Sara


student2.name

Joe


student1.university

University


student2.university

University


Important:

Class Attribute
    ->
Shared between objects.


Instance Attribute
    ->
Unique for each object.


Next Lesson:

Methods and Return in Classes

We will learn how methods can:

- Receive data.
- Process data.
- Change object data.
- Return values.
"""


###########################################################
# END OF CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
###########################################################