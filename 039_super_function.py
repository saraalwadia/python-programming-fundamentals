###########################################################
# super() Function in Python
###########################################################


"""
super() is used to access methods
and attributes from the parent class.

It is commonly used with:

- __init__()
- Parent methods
"""


# ===========================================================
# PART 1: Basic super()
# ===========================================================


class Person:

    def say_hello(self):

        print("Hello from Person")


class Student(Person):

    def say_hello(self):

        super().say_hello()

        print("Hello from Student")


student = Student()

student.say_hello()


# ===========================================================
# PART 2: super() with __init__()
# ===========================================================


class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def __init__(self, name, student_id):

        super().__init__(name)

        self.student_id = student_id


student = Student("Sara", 101)


print(student.name)

print(student.student_id)


# super().__init__(name)
# calls the __init__() method
# from the parent class.



# ===========================================================
# PART 3: Parent and Child Attributes
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


print("Name:", student.name)

print("Major:", student.major)


# ===========================================================
# PART 4: Adding More Information
# ===========================================================


class Employee:

    def __init__(self, name):

        self.name = name


    def display(self):

        print("Employee:", self.name)


class Manager(Employee):

    def __init__(self, name, department):

        super().__init__(name)

        self.department = department


    def display(self):

        super().display()

        print("Department:", self.department)


manager = Manager(
    "Sara",
    "IT"
)


manager.display()


# ===========================================================
# PART 5: Calling Parent Method
# ===========================================================


class Animal:

    def sound(self):

        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):

        super().sound()

        print("Dog says Woof")


dog = Dog()

dog.sound()


# ===========================================================
# PART 6: Another Example
# ===========================================================


class Vehicle:

    def start(self):

        print("Vehicle is starting")


class Car(Vehicle):

    def start(self):

        super().start()

        print("Car is ready to drive")


car = Car()

car.start()


# ===========================================================
# PART 7: super() with Multiple Attributes
# ===========================================================


class Person:

    def __init__(self, name, age):

        self.name = name

        self.age = age


class Student(Person):

    def __init__(self, name, age, university):

        super().__init__(name, age)

        self.university = university


student = Student(
    "Joe",
    22,
    "University of Palestine"
)


print("Name:", student.name)

print("Age:", student.age)

print("University:", student.university)


# ===========================================================
# PART 8: Why Do We Use super()?
# ===========================================================


"""
Without super():

class Student(Person):

    def __init__(self, name, age, major):

        self.name = name

        self.age = age

        self.major = major


With super():

class Student(Person):

    def __init__(self, name, age, major):

        super().__init__(name, age)

        self.major = major


super() helps us reuse the code
from the parent class.
"""


# ===========================================================
# PART 9: Inheritance + Overriding + super()
# ===========================================================


class Person:

    def introduce(self):

        print("I am a person")


class Student(Person):

    def introduce(self):

        super().introduce()

        print("I am a student")


class Teacher(Person):

    def introduce(self):

        super().introduce()

        print("I am a teacher")


student = Student()

teacher = Teacher()


student.introduce()

teacher.introduce()


# ===========================================================
# PART 10: Important Notes
# ===========================================================


"""
super():

- Refers to the parent class.
- Helps us reuse parent code.
- Is commonly used with __init__().
- Can also call parent methods.


Example:

super().__init__()

Calls the parent constructor.


Example:

super().display()

Calls the parent display() method.
"""


# ===========================================================
# PART 11: Simple Practice
# ===========================================================


# Exercise 1:
#
# Create a parent class:
#
# Person
#
# Add __init__():
#
# name
#
# Create a child class:
#
# Student
#
# Add:
#
# student_id
#
# Use super() to initialize name.
# -----------------------------------------------------------


# Exercise 2:
#
# Create a parent class:
#
# Animal
#
# Add:
#
# sound()
#
# Create a child class:
#
# Dog
#
# Override sound().
#
# Use super() to call the parent sound()
# and then print:
#
# "Dog says Woof"
# -----------------------------------------------------------


# Exercise 3:
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
# Create a child class:
#
# Manager
#
# Add:
#
# department
#
# Use super() inside __init__().
# -----------------------------------------------------------


# Exercise 4:
#
# Create:
#
# Vehicle
#
# with:
#
# start()
#
# Create:
#
# Car
#
# Override start().
#
# Use super() and then print:
#
# "Car is ready"
# -----------------------------------------------------------


###########################################################
# END OF super()
###########################################################