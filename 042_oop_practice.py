###########################################################
# OOP Practice
###########################################################


"""
This file contains practical examples using:

- Classes and Objects
- __init__()
- Instance Attributes
- Class Attributes
- Instance Methods
- Class Methods
- Static Methods
- Inheritance
- Method Overriding
- super()
- Encapsulation
- Polymorphism
"""


# ===========================================================
# PART 1: Classes and Objects
# ===========================================================


class Person:

    def say_hello(self):

        print("Hello")


person1 = Person()

person1.say_hello()



# ===========================================================
# PART 2: Constructor and Instance Attributes
# ===========================================================


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


student1 = Student("Sara", 23)


print(student1.name)
print(student1.age)



# ===========================================================
# PART 3: Instance Method
# ===========================================================


class Student:

    def __init__(self, name):

        self.name = name


    def display_name(self):

        print("Student Name:", self.name)


student1 = Student("Joe")

student1.display_name()



# ===========================================================
# PART 4: Class Attributes
# ===========================================================


class Student:

    university = "University of Palestine"


    def __init__(self, name):

        self.name = name


student1 = Student("Sara")
student2 = Student("Joe")


print(student1.university)
print(student2.university)



# ===========================================================
# PART 5: Class Method
# ===========================================================


class Student:

    university = "University of Palestine"


    @classmethod
    def display_university(cls):

        print(cls.university)


Student.display_university()



# ===========================================================
# PART 6: Static Method
# ===========================================================


class Calculator:


    @staticmethod
    def add(number1, number2):

        return number1 + number2


result = Calculator.add(10, 5)

print(result)



# ===========================================================
# PART 7: Inheritance
# ===========================================================


class Person:

    def __init__(self, name):

        self.name = name


    def introduce(self):

        print("My name is", self.name)


class Student(Person):

    def study(self):

        print(self.name, "is studying")


student = Student("Sara")


student.introduce()
student.study()



# ===========================================================
# PART 8: Method Overriding
# ===========================================================


class Animal:

    def sound(self):

        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):

        print("Dog says Woof")


dog = Dog()

dog.sound()



# ===========================================================
# PART 9: super()
# ===========================================================


class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def __init__(self, name, major):

        super().__init__(name)

        self.major = major


student = Student(
    "Joe",
    "Computer Science"
)


print(student.name)
print(student.major)



# ===========================================================
# PART 10: Encapsulation
# ===========================================================


class BankAccount:

    def __init__(self, balance):

        self.__balance = balance


    def get_balance(self):

        return self.__balance


    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount

        else:

            print("Invalid amount")


account = BankAccount(100)


print(account.get_balance())


account.deposit(50)


print(account.get_balance())



# ===========================================================
# PART 11: Polymorphism
# ===========================================================


class Dog:

    def sound(self):

        print("Woof")


class Cat:

    def sound(self):

        print("Meow")


animals = [

    Dog(),
    Cat()

]


for animal in animals:

    animal.sound()



# ===========================================================
# PART 12: Mini Project - Student Management
# ===========================================================


class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age


    def display_info(self):

        print("Name:", self.name)
        print("Age:", self.age)



class Student(Person):

    university = "University of Palestine"


    def __init__(self, name, age, student_id, major):

        super().__init__(name, age)

        self.student_id = student_id
        self.major = major


    def display_student(self):

        self.display_info()

        print("Student ID:", self.student_id)
        print("Major:", self.major)
        print("University:", self.university)



student1 = Student(
    "Sara",
    23,
    101,
    "Information Technology"
)


student1.display_student()



# ===========================================================
# PART 13: Mini Project - Employee System
# ===========================================================


class Employee:

    company = "ABC Company"


    def __init__(self, name, salary):

        self.name = name
        self.__salary = salary


    def get_salary(self):

        return self.__salary


    def work(self):

        print(self.name, "is working")



class Manager(Employee):

    def work(self):

        print(self.name, "is managing the team")



class Developer(Employee):

    def work(self):

        print(self.name, "is writing code")



employees = [

    Manager("Sara", 3000),
    Developer("Joe", 2500)

]


for employee in employees:

    employee.work()

    print("Salary:", employee.get_salary())



# ===========================================================
# PART 14: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a class called:
#
# Car
#
# Add:
#
# brand
# model
#
# Create a method:
#
# display_info()
#
# Print the car information.


# -----------------------------------------------------------


# Exercise 2:
#
# Create a class called:
#
# Student
#
# Add a class attribute:
#
# school
#
# Add:
#
# name
# age
#
# Create two objects
# and print their information.


# -----------------------------------------------------------


# Exercise 3:
#
# Create a parent class:
#
# Animal
#
# Add:
#
# name
#
# Create child classes:
#
# Dog
# Cat
#
# Add different sound() methods.


# -----------------------------------------------------------


# Exercise 4:
#
# Create a class:
#
# BankAccount
#
# Add a private attribute:
#
# __balance
#
# Create methods:
#
# deposit(amount)
#
# withdraw(amount)
#
# get_balance()
#
# Do not allow withdrawing
# more than the available balance.


# -----------------------------------------------------------


# Exercise 5:
#
# Create a parent class:
#
# Employee
#
# Add:
#
# name
# salary
#
# Create child classes:
#
# Manager
# Developer
#
# Override:
#
# work()
#
# Store the objects in a list
# and use a loop to call work().


###########################################################
# END OF OOP PRACTICE
###########################################################