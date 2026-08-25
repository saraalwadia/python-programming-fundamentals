###########################################################
# Constructors and __init__ in Python
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Understand what a constructor is.
- Learn what __init__() does.
- Understand when __init__() is executed.
- Learn how to pass data when creating an object.
- Understand self inside __init__().
- Create multiple objects with different data.
- Combine attributes, constructors, and methods.


Topics Covered:

PART 1:
What is a Constructor?

PART 2:
The __init__() Method

PART 3:
Using self

PART 4:
Passing Arguments

PART 5:
Creating Multiple Objects

PART 6:
Default Values

PART 7:
Constructors with Methods

PART 8:
Updating Object Data

PART 9:
Practical Examples

PART 10:
Practice Exercises
"""


# ===========================================================
# PART 1: What is a Constructor?
# ===========================================================


"""
A constructor is a special method
that runs automatically when an object is created.

In Python, the constructor is:

__init__()


Example:

class Student:

    def __init__(self):

        print("Object created")


student1 = Student()


When student1 is created,
__init__() runs automatically.
"""


# ===========================================================
# PART 2: Basic __init__()
# ===========================================================


class Student:

    def __init__(self):

        print("Student object created.")


student1 = Student()


# __init__() runs automatically
# when the object is created.



# ===========================================================
# PART 3: __init__() with Attributes
# ===========================================================


class Person:

    def __init__(self):

        self.name = "Sara"
        self.age = 23


person1 = Person()


print(person1.name)
print(person1.age)



# ===========================================================
# PART 4: Understanding self
# ===========================================================


"""
self refers to the current object.

Example:

person1 = Person()


Inside the class:

self

refers to:

person1
"""


class PersonInfo:

    def __init__(self):

        self.name = "Sara"


person = PersonInfo()


print(person.name)



# ===========================================================
# PART 5: Passing Data to __init__()
# ===========================================================


"""
We can pass values when creating an object.

Example:

student1 = Student("Sara", 23)


The values are received by:

name
age
"""


class StudentData:

    def __init__(self, name, age):

        self.name = name
        self.age = age


student1 = StudentData("Sara", 23)


print(student1.name)
print(student1.age)



# ===========================================================
# PART 6: Creating Multiple Objects
# ===========================================================


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


student1 = Student("Sara", 23)

student2 = Student("Joe", 20)

student3 = Student("Ali", 25)


print(student1.name, student1.age)

print(student2.name, student2.age)

print(student3.name, student3.age)


"""
Each object has its own data.

student1:

Sara
23


student2:

Joe
20


student3:

Ali
25
"""



# ===========================================================
# PART 7: Constructor with More Attributes
# ===========================================================


class Car:

    def __init__(self, brand, color, year):

        self.brand = brand
        self.color = color
        self.year = year


car1 = Car("Toyota", "Black", 2020)

car2 = Car("BMW", "Red", 2024)


print(car1.brand)
print(car1.color)
print(car1.year)


print(car2.brand)
print(car2.color)
print(car2.year)



# ===========================================================
# PART 8: Updating Object Attributes
# ===========================================================


class User:

    def __init__(self, name, age):

        self.name = name
        self.age = age


user1 = User("Sara", 23)


print(user1.name)
print(user1.age)


# Change object data

user1.name = "Joe"

user1.age = 25


print(user1.name)
print(user1.age)



# ===========================================================
# PART 9: Constructor with Default Values
# ===========================================================


"""
We can give parameters default values.

If no value is provided,
the default value will be used.
"""


class Product:

    def __init__(self, name, price=0):

        self.name = name
        self.price = price


product1 = Product("Laptop", 1000)

product2 = Product("Mouse")


print(product1.name, product1.price)

print(product2.name, product2.price)



# ===========================================================
# PART 10: Constructor with Methods
# ===========================================================


class StudentInfo:

    def __init__(self, name, age):

        self.name = name
        self.age = age


    def display(self):

        print("Name:", self.name)

        print("Age:", self.age)


student1 = StudentInfo("Sara", 23)


student1.display()



# ===========================================================
# PART 11: Method That Changes Object Data
# ===========================================================


class Person:

    def __init__(self, name):

        self.name = name


    def change_name(self, new_name):

        self.name = new_name


person1 = Person("Sara")


print(person1.name)


person1.change_name("Joe")


print(person1.name)



# ===========================================================
# PART 12: Practical Example - Student Result
# ===========================================================


class StudentResult:

    def __init__(self, name, mark):

        self.name = name
        self.mark = mark


    def show_result(self):

        print("Name:", self.name)

        print("Mark:", self.mark)


        if self.mark >= 50:

            print("Result: Pass")

        else:

            print("Result: Fail")


student1 = StudentResult("Sara", 95)

student2 = StudentResult("Joe", 40)


student1.show_result()

print()

student2.show_result()



# ===========================================================
# PART 13: Practical Example - Bank Account
# ===========================================================


class BankAccount:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance


    def show_balance(self):

        print(self.name)

        print("Balance:", self.balance)


account1 = BankAccount("Sara", 1000)


account1.show_balance()



# ===========================================================
# PART 14: Practical Example - Calculator
# ===========================================================


class Calculator:

    def __init__(self, number1, number2):

        self.number1 = number1
        self.number2 = number2


    def add(self):

        print(self.number1 + self.number2)


    def subtract(self):

        print(self.number1 - self.number2)


    def multiply(self):

        print(self.number1 * self.number2)


    def divide(self):

        if self.number2 != 0:

            print(self.number1 / self.number2)

        else:

            print("Cannot divide by zero")


calculator = Calculator(10, 5)


calculator.add()

calculator.subtract()

calculator.multiply()

calculator.divide()



# ===========================================================
# PART 15: Practical Example - Product
# ===========================================================


class Product:

    def __init__(self, name, price):

        self.name = name
        self.price = price


    def display(self):

        print("Product:", self.name)

        print("Price:", self.price)


product1 = Product("Laptop", 1000)

product2 = Product("Mouse", 50)


product1.display()

print()

product2.display()



# ===========================================================
# PART 16: Important Concept
# ===========================================================


"""
Without __init__():

student1 = Student()

student1.name = "Sara"

student1.age = 23


With __init__():

student1 = Student("Sara", 23)


Using __init__() makes it easier
to create objects with their data.
"""



# ===========================================================
# PART 17: Class Blueprint
# ===========================================================


"""
Class:

Student


Constructor:

__init__(self, name, age)


Objects:


student1 = Student("Sara", 23)

student2 = Student("Joe", 20)


            Student
               |
               |
        __init__()
               |
        ----------------
        |              |
        |              |
    student1       student2
    Sara           Joe
    23             20


The class is the blueprint.

The constructor initializes
each object with its own data.
"""



# ===========================================================
# PART 18: Practice Exercises
# ===========================================================


"""
Exercise 1:

Create a class called:

Person


Create __init__() with:

name
age


Create an object and print
the name and age.


-----------------------------------------------------------


Exercise 2:

Create a class called:

Car


Create __init__() with:

brand
color
year


Create two different objects.


Print their information.


-----------------------------------------------------------


Exercise 3:

Create a class called:

Student


Create __init__() with:

name
mark


Create a method:

result()


If mark >= 50:

    Print "Pass"

Otherwise:

    Print "Fail"


-----------------------------------------------------------


Exercise 4:

Create a class called:

BankAccount


Create __init__() with:

name
balance


Create methods:

deposit(amount)

withdraw(amount)

show_balance()


-----------------------------------------------------------


Exercise 5:

Create a class called:

Rectangle


Create __init__() with:

length
width


Create a method:

area()


Calculate and print:

length * width


-----------------------------------------------------------


Exercise 6:

Create a class called:

Employee


Create __init__() with:

name
salary


Create a method:

display()


Print:

Name
Salary


-----------------------------------------------------------


Exercise 7:

Create a class called:

Calculator


Create __init__() with:

number1
number2


Create methods:

add()

subtract()

multiply()

divide()


Test all methods.
"""


# ===========================================================
# SUMMARY
# ===========================================================


"""
Constructor Summary:


__init__():

A special method that runs automatically
when an object is created.


self:

Refers to the current object.


Example:


class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age


student1 = Student("Sara", 23)


student1.name
student1.age


Important:


class Student
    |
    |
    +-- __init__()
    |
    +-- Attributes
    |
    +-- Methods


Next Lesson:

Class Attributes vs Instance Attributes

We will learn the difference between:

Class data:

    shared by all objects


Instance data:

    unique for each object
"""


###########################################################
# END OF CONSTRUCTORS AND __init__
###########################################################