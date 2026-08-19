###########################################################
# Classes and Objects in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand Object-Oriented Programming (OOP).
- Understand what a class is.
- Understand what an object is.
- Learn how to create a class.
- Learn how to create objects from a class.
- Learn how to create and access attributes.
- Learn how to change attribute values.
- Learn how multiple objects can be created from one class.
- Understand basic methods.


Topics Covered:

PART 1:
What is OOP?

PART 2:
What is a Class?

PART 3:
Creating a Class

PART 4:
Creating an Object

PART 5:
Class Attributes

PART 6:
Creating Multiple Objects

PART 7:
Changing Attributes

PART 8:
Methods

PART 9:
Practical Examples

PART 10:
Practice Exercises
"""


# ===========================================================
# PART 1: What is OOP?
# ===========================================================


"""
OOP stands for:

Object-Oriented Programming


OOP is a programming style based on:

- Classes
- Objects


A class can be thought of as a blueprint.

An object is an actual instance created
from that blueprint.


Example:

Class:
    Car

Objects:
    Toyota
    BMW
    Tesla


Another example:

Class:
    Student

Objects:
    Sara
    Joe
    Ali
"""


# ===========================================================
# PART 2: What is a Class?
# ===========================================================


"""
A class is created using the keyword:

class


Syntax:

class ClassName:

    code
"""


class Student:

    pass


# "pass" means:
# Do nothing for now.


# ===========================================================
# PART 3: Creating an Object
# ===========================================================


"""
An object is created by calling the class.

Syntax:

object_name = ClassName()
"""


student1 = Student()


print(student1)


# student1 is an object of the Student class.



# ===========================================================
# PART 4: Creating Multiple Objects
# ===========================================================


student1 = Student()
student2 = Student()
student3 = Student()


print(student1)
print(student2)
print(student3)


# Each object is a separate object.



# ===========================================================
# PART 5: Class Attributes
# ===========================================================


"""
An attribute is a value/data
that belongs to an object.
"""


class Person:

    name = "Sara"
    age = 23


# Create an object


person1 = Person()


# Access attributes


print(person1.name)
print(person1.age)


# ===========================================================
# PART 6: Creating More Objects
# ===========================================================


person1 = Person()
person2 = Person()


print(person1.name)
print(person2.name)


# Both objects currently have
# the same class attributes.



# ===========================================================
# PART 7: Changing an Attribute
# ===========================================================


person1.name = "Joe"


print(person1.name)
print(person2.name)


# person1 changed,
# but person2 still has the original value.



# ===========================================================
# PART 8: Adding an Attribute to an Object
# ===========================================================


person1.city = "Gaza"


print(person1.city)


# ===========================================================
# PART 9: Different Objects Can Have Different Values
# ===========================================================


class Car:

    brand = "Toyota"
    color = "Black"


car1 = Car()
car2 = Car()


car1.color = "Red"
car2.color = "Blue"


print(car1.color)
print(car2.color)


# ===========================================================
# PART 10: Simple Class Example
# ===========================================================


class Animal:

    name = "Cat"
    age = 2


cat = Animal()


print(cat.name)
print(cat.age)


# ===========================================================
# PART 11: Another Class Example
# ===========================================================


class Book:

    title = "Python Basics"
    pages = 200


book1 = Book()


print(book1.title)
print(book1.pages)


# ===========================================================
# PART 12: Methods
# ===========================================================


"""
A method is a function that belongs
to a class.

Methods are used to define behavior
for objects.
"""


class Dog:

    def bark(self):

        print("Woof!")


dog1 = Dog()


dog1.bark()


# ===========================================================
# PART 13: Method with More Than One Action
# ===========================================================


class Robot:

    def start(self):

        print("Robot started.")

    def stop(self):

        print("Robot stopped.")


robot1 = Robot()


robot1.start()
robot1.stop()


# ===========================================================
# PART 14: Method with an Argument
# ===========================================================


class Greeting:

    def say_hello(self, name):

        print("Hello", name)


greeting1 = Greeting()


greeting1.say_hello("Sara")
greeting1.say_hello("Joe")


# ===========================================================
# PART 15: Class with Attributes and Methods
# ===========================================================


class StudentInfo:

    name = "Sara"
    age = 23

    def display(self):

        print("Name:", self.name)
        print("Age:", self.age)


student = StudentInfo()


student.display()


# ===========================================================
# PART 16: Understanding self
# ===========================================================


"""
self refers to the current object.

For example:

student.display()


Inside the method:

self

refers to:

student
"""


class PersonInfo:

    name = "Sara"

    def display_name(self):

        print(self.name)


person = PersonInfo()


person.display_name()


# ===========================================================
# PART 17: Changing Object Attributes
# ===========================================================


class StudentData:

    name = "Sara"
    mark = 90


student = StudentData()


print(student.name)
print(student.mark)


student.name = "Joe"
student.mark = 80


print(student.name)
print(student.mark)


# ===========================================================
# PART 18: Multiple Objects with Different Data
# ===========================================================


class StudentRecord:

    name = ""
    mark = 0


student1 = StudentRecord()
student2 = StudentRecord()


student1.name = "Sara"
student1.mark = 95


student2.name = "Joe"
student2.mark = 80


print(student1.name, student1.mark)
print(student2.name, student2.mark)


# ===========================================================
# PART 19: Practical Example - Bank Account
# ===========================================================


class BankAccount:

    balance = 0

    def show_balance(self):

        print("Balance:", self.balance)


account1 = BankAccount()


account1.balance = 1000


account1.show_balance()


# ===========================================================
# PART 20: Practical Example - Calculator
# ===========================================================


class Calculator:

    def add(self, number1, number2):

        print(number1 + number2)

    def subtract(self, number1, number2):

        print(number1 - number2)

    def multiply(self, number1, number2):

        print(number1 * number2)

    def divide(self, number1, number2):

        print(number1 / number2)


calculator = Calculator()


calculator.add(10, 5)
calculator.subtract(10, 5)
calculator.multiply(10, 5)
calculator.divide(10, 5)


# ===========================================================
# PART 21: Practical Example - Student
# ===========================================================


class StudentResult:

    name = ""
    mark = 0

    def show_result(self):

        if self.mark >= 50:

            print(self.name, "Passed")

        else:

            print(self.name, "Failed")


student1 = StudentResult()
student2 = StudentResult()


student1.name = "Sara"
student1.mark = 95


student2.name = "Joe"
student2.mark = 40


student1.show_result()
student2.show_result()


# ===========================================================
# PART 22: Practical Example - Person
# ===========================================================


class PersonData:

    name = ""
    age = 0

    def display_info(self):

        print("Name:", self.name)
        print("Age:", self.age)


person1 = PersonData()


person1.name = "Sara"
person1.age = 23


person1.display_info()


# ===========================================================
# PART 23: Important Difference
# ===========================================================


"""
Class:

    Blueprint / template


Object:

    An actual instance of a class


Example:


class Car:

    pass


car1 = Car()
car2 = Car()


Car
    |
    +---- car1
    |
    +---- car2


The class is the blueprint.

The objects are created from the blueprint.
"""


# ===========================================================
# PART 24: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a class called:
#
# Student
#
# Create an object from the class.
# -----------------------------------------------------------


# Exercise 2:
#
# Create a class called:
#
# Car
#
# Add the following attributes:
#
# brand
# color
# year
#
# Create an object and print
# all attributes.
# -----------------------------------------------------------


# Exercise 3:
#
# Create a class called:
#
# Person
#
# Add:
#
# name
# age
#
# Create two objects with different
# names and ages.
# -----------------------------------------------------------


# Exercise 4:
#
# Create a class called:
#
# Calculator
#
# Add methods for:
#
# add
# subtract
# multiply
# divide
#
# Test all methods.
# -----------------------------------------------------------


# Exercise 5:
#
# Create a class called:
#
# Student
#
# Add:
#
# name
# mark
#
# Create a method called:
#
# result()
#
# If mark >= 50:
#
# print("Pass")
#
# Otherwise:
#
# print("Fail")
# -----------------------------------------------------------


# Exercise 6:
#
# Create a class called:
#
# Dog
#
# Add:
#
# name
# age
#
# Create a method:
#
# bark()
#
# It should print:
#
# "Woof!"
# -----------------------------------------------------------


# Exercise 7:
#
# Create a class called:
#
# BankAccount
#
# Add:
#
# balance
#
# Create methods:
#
# deposit()
# withdraw()
# show_balance()
#
# Test the methods.
# -----------------------------------------------------------


# ===========================================================
# SUMMARY
# ===========================================================


"""
OOP Summary:


Class:

A blueprint used to create objects.


Object:

An instance of a class.


Attribute:

Data that belongs to an object.


Method:

A function that belongs to a class.


Example:


class Student:

    name = "Sara"

    def display(self):

        print(self.name)


student = Student()


student.name
student.display()


Important:

class
    ->
Creates a class.


object = ClassName()
    ->
Creates an object.


self
    ->
Refers to the current object.


Next Lesson:

Constructors and __init__

We will learn how to give
each object its own data
when the object is created.
"""


###########################################################
# END OF CLASSES AND OBJECTS
###########################################################