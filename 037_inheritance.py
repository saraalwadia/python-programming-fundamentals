###########################################################
# Inheritance in Python
###########################################################


"""
Inheritance allows a class to use
attributes and methods from another class.

The class that gives the properties is called:

Parent Class
Base Class

The class that receives the properties is called:

Child Class
Derived Class
"""


# ===========================================================
# PART 1: Basic Inheritance
# ===========================================================


class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age


    def display_info(self):

        print("Name:", self.name)

        print("Age:", self.age)



class Student(Person):

    pass


# Student inherits from Person.


student1 = Student("Sara", 23)


print(student1.name)

print(student1.age)

student1.display_info()


# ===========================================================
# PART 2: Parent and Child Class
# ===========================================================


class Animal:

    def eat(self):

        print("Animal is eating")


class Dog(Animal):

    def bark(self):

        print("Dog is barking")


dog = Dog()


# Dog can use its own method.

dog.bark()


# Dog can also use the method
# inherited from Animal.

dog.eat()


# ===========================================================
# PART 3: Adding New Attributes to Child Class
# ===========================================================


class Person:

    def __init__(self, name):

        self.name = name


class Student(Person):

    def __init__(self, name, student_id):

        self.name = name

        self.student_id = student_id


student = Student("Joe", 101)


print(student.name)

print(student.student_id)


# Student has:
#
# name
# student_id



# ===========================================================
# PART 4: Using super()
# ===========================================================


"""
super() allows the child class
to call methods from the parent class.
"""


class Person:

    def __init__(self, name, age):

        self.name = name

        self.age = age


class Student(Person):

    def __init__(self, name, age, major):

        super().__init__(name, age)

        self.major = major


student = Student(
    "Sara",
    23,
    "Computer Science"
)


print(student.name)

print(student.age)

print(student.major)


# ===========================================================
# PART 5: Inherited Methods
# ===========================================================


class Person:

    def say_hello(self):

        print("Hello")


class Student(Person):

    def study(self):

        print("Student is studying")


student = Student()


student.say_hello()

student.study()


# ===========================================================
# PART 6: Parent and Child Methods
# ===========================================================


class Person:

    def walk(self):

        print("Person is walking")


class Student(Person):

    def study(self):

        print("Student is studying")


student = Student()


student.walk()

student.study()


# ===========================================================
# PART 7: Multiple Child Classes
# ===========================================================


class Animal:

    def eat(self):

        print("Animal is eating")


class Dog(Animal):

    def bark(self):

        print("Dog is barking")


class Cat(Animal):

    def meow(self):

        print("Cat is meowing")


dog = Dog()

cat = Cat()


dog.eat()

dog.bark()


cat.eat()

cat.meow()


# ===========================================================
# PART 8: Practical Example
# ===========================================================


class Employee:

    def __init__(self, name, salary):

        self.name = name

        self.salary = salary


    def display_info(self):

        print("Name:", self.name)

        print("Salary:", self.salary)


class Manager(Employee):

    def manage(self):

        print(self.name, "is managing the team")


manager = Manager(
    "Sara",
    2000
)


manager.display_info()

manager.manage()


# ===========================================================
# PART 9: Another Practical Example
# ===========================================================


class Vehicle:

    def __init__(self, brand):

        self.brand = brand


    def start(self):

        print("Vehicle is starting")


class Car(Vehicle):

    def drive(self):

        print(self.brand, "is driving")


car = Car("Toyota")


print(car.brand)

car.start()

car.drive()


# ===========================================================
# PART 10: Check Inheritance
# ===========================================================


"""
isinstance()

checks if an object belongs to
a specific class.
"""


class Person:

    pass


class Student(Person):

    pass


student = Student()


print(isinstance(student, Student))

print(isinstance(student, Person))


# Both return True because
# Student inherits from Person.


# ===========================================================
# PART 11: Check Class Relationship
# ===========================================================


"""
issubclass()

checks if a class is a child
of another class.
"""


print(issubclass(Student, Person))

print(issubclass(Person, Student))


# ===========================================================
# PART 12: Important Idea
# ===========================================================


"""
Inheritance represents an:

IS-A relationship.

Example:

Student IS-A Person

Dog IS-A Animal

Car IS-A Vehicle


The child class gets properties
and methods from the parent class.
"""


# ===========================================================
# PART 13: Simple Practice
# ===========================================================


# Exercise 1:
#
# Create a parent class called:
#
# Person
#
# Add:
#
# name
# age
#
# Create a child class called:
#
# Student
#
# Create a Student object
# and print its name and age.


# -----------------------------------------------------------


# Exercise 2:
#
# Create a parent class:
#
# Animal
#
# Add a method:
#
# eat()
#
# Create a child class:
#
# Dog
#
# Add a method:
#
# bark()
#
# Create a Dog object
# and call both methods.


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
# Use super() inside the child class.


# -----------------------------------------------------------


# Exercise 4:
#
# Create:
#
# Vehicle
#
# with:
#
# brand
#
# Create:
#
# Car
#
# and add:
#
# model
#
# Print both brand and model.


###########################################################
# END OF INHERITANCE
###########################################################