###########################################################
# Method Overriding in Python
###########################################################


"""
Method Overriding:

A child class can provide its own version
of a method that already exists
in the parent class.

The child method replaces the behavior
of the parent method when we use
the child object.
"""


# ===========================================================
# PART 1: Basic Method Overriding
# ===========================================================


class Animal:

    def sound(self):

        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):

        print("Dog says Woof")


animal = Animal()

dog = Dog()


animal.sound()

dog.sound()


# Dog overrides the sound() method
# from Animal.



# ===========================================================
# PART 2: Another Example
# ===========================================================


class Person:

    def introduce(self):

        print("I am a person")


class Student(Person):

    def introduce(self):

        print("I am a student")


person = Person()

student = Student()


person.introduce()

student.introduce()


# ===========================================================
# PART 3: Overriding with Attributes
# ===========================================================


class Animal:

    def __init__(self, name):

        self.name = name


    def display(self):

        print("Animal:", self.name)


class Dog(Animal):

    def display(self):

        print("Dog:", self.name)


animal = Animal("Animal")

dog = Dog("Buddy")


animal.display()

dog.display()


# ===========================================================
# PART 4: Method Overriding with Parameters
# ===========================================================


class Calculator:

    def calculate(self, a, b):

        print(a + b)


class AdvancedCalculator(Calculator):

    def calculate(self, a, b):

        print(a * b)


calculator = Calculator()

advanced_calculator = AdvancedCalculator()


calculator.calculate(10, 5)

advanced_calculator.calculate(10, 5)


# ===========================================================
# PART 5: Overriding with super()
# ===========================================================


"""
Sometimes we want to use the parent method
and then add something new.

We can use:

super()
"""


class Person:

    def introduce(self):

        print("I am a person")


class Student(Person):

    def introduce(self):

        super().introduce()

        print("I am also a student")


student = Student()


student.introduce()


# Output:
#
# I am a person
# I am also a student



# ===========================================================
# PART 6: Practical Example - Employee
# ===========================================================


class Employee:

    def work(self):

        print("Employee is working")


class Manager(Employee):

    def work(self):

        print("Manager is managing the team")


class Developer(Employee):

    def work(self):

        print("Developer is writing code")


employee = Employee()

manager = Manager()

developer = Developer()


employee.work()

manager.work()

developer.work()


# Each child class has its own
# version of the work() method.



# ===========================================================
# PART 7: Practical Example - Animals
# ===========================================================


class Animal:

    def sound(self):

        print("Some animal sound")


class Dog(Animal):

    def sound(self):

        print("Woof")


class Cat(Animal):

    def sound(self):

        print("Meow")


class Cow(Animal):

    def sound(self):

        print("Moo")


dog = Dog()

cat = Cat()

cow = Cow()


dog.sound()

cat.sound()

cow.sound()


# ===========================================================
# PART 8: Method Overriding with __init__()
# ===========================================================


"""
__init__() can also be overridden.

The child class can have
its own __init__() method.
"""


class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def __init__(self, name, major):

        self.name = name

        self.major = major


student = Student(
    "Sara",
    "Computer Science"
)


print(student.name)

print(student.major)


# ===========================================================
# PART 9: Using super() with __init__()
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
    "Information Technology"
)


print(student.name)

print(student.major)


# super().__init__()
# calls the parent __init__() method.



# ===========================================================
# PART 10: Method Overriding vs Inheritance
# ===========================================================


"""
Inheritance:

The child class gets methods
from the parent class.


Example:

class Dog(Animal):
    pass


Method Overriding:

The child class creates its own
version of a parent method.


Example:

class Dog(Animal):

    def sound(self):

        print("Woof")
"""


# ===========================================================
# PART 11: Simple Example
# ===========================================================


class Vehicle:

    def start(self):

        print("Vehicle is starting")


class Car(Vehicle):

    def start(self):

        print("Car is starting")


class Motorcycle(Vehicle):

    def start(self):

        print("Motorcycle is starting")


vehicle = Vehicle()

car = Car()

motorcycle = Motorcycle()


vehicle.start()

car.start()

motorcycle.start()


# ===========================================================
# PART 12: Important Notes
# ===========================================================


"""
Important:

1. Method overriding happens between
   a parent class and a child class.


2. The method should have the same name.


3. The child class provides
   a different implementation.


4. super() can be used when we want
   to call the parent method.


Example:

class Parent:

    def show(self):

        print("Parent")


class Child(Parent):

    def show(self):

        super().show()

        print("Child")
"""


# ===========================================================
# PART 13: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a parent class:
#
# Animal
#
# Add a method:
#
# sound()
#
# Print:
#
# "Animal makes a sound"
#
# Create a child class:
#
# Dog
#
# Override sound()
#
# Print:
#
# "Dog says Woof"
# -----------------------------------------------------------


# Exercise 2:
#
# Create a parent class:
#
# Person
#
# Add:
#
# introduce()
#
# Create a child class:
#
# Student
#
# Override introduce()
#
# Print:
#
# "I am a student"
# -----------------------------------------------------------


# Exercise 3:
#
# Create:
#
# Employee
#
# with:
#
# work()
#
# Create:
#
# Manager
# Developer
#
# Override work() in both classes.
#
# Each class should print
# a different message.
# -----------------------------------------------------------


# Exercise 4:
#
# Create a parent class:
#
# Vehicle
#
# Add:
#
# start()
#
# Create:
#
# Car
# Motorcycle
#
# Override start()
# in both classes.
# -----------------------------------------------------------


# Exercise 5:
#
# Create a parent class:
#
# Person
#
# with __init__():
#
# name
#
# Create a child class:
#
# Student
#
# with:
#
# name
# major
#
# Use super()
# to call the parent __init__().
# -----------------------------------------------------------


###########################################################
# END OF METHOD OVERRIDING
###########################################################