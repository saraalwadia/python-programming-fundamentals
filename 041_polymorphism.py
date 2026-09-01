###########################################################
# Polymorphism in Python
###########################################################


"""
Polymorphism means:

Different objects can use the same method name,
but each object can perform the method differently.

Example:

Dog.sound()

Cat.sound()

Both use sound(),
but each one produces a different result.

Polymorphism is commonly used with:

- Inheritance
- Method Overriding
"""


# ===========================================================
# PART 1: Basic Polymorphism
# ===========================================================


class Dog:

    def sound(self):

        print("Woof")


class Cat:

    def sound(self):

        print("Meow")


dog = Dog()
cat = Cat()


dog.sound()
cat.sound()


# Both classes have the same method name:
#
# sound()
#
# But each class has different behavior.



# ===========================================================
# PART 2: Polymorphism Using a Loop
# ===========================================================


class Dog:

    def sound(self):

        print("Woof")


class Cat:

    def sound(self):

        print("Meow")


class Cow:

    def sound(self):

        print("Moo")


animals = [

    Dog(),
    Cat(),
    Cow()

]


for animal in animals:

    animal.sound()


# The same method is called:
#
# sound()
#
# But the result depends on the object.



# ===========================================================
# PART 3: Polymorphism with Inheritance
# ===========================================================


class Animal:

    def sound(self):

        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):

        print("Dog says Woof")


class Cat(Animal):

    def sound(self):

        print("Cat says Meow")


dog = Dog()
cat = Cat()


dog.sound()
cat.sound()


# Dog and Cat inherit from Animal.
#
# Each child class provides its own
# version of the sound() method.



# ===========================================================
# PART 4: Polymorphism with Multiple Child Classes
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


class Designer(Employee):

    def work(self):

        print("Designer is creating designs")


employees = [

    Manager(),
    Developer(),
    Designer()

]


for employee in employees:

    employee.work()


# All objects use:
#
# work()
#
# But each object performs
# a different action.



# ===========================================================
# PART 5: Practical Example - Vehicles
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


class Bus(Vehicle):

    def start(self):

        print("Bus is starting")


vehicles = [

    Car(),
    Motorcycle(),
    Bus()

]


for vehicle in vehicles:

    vehicle.start()



# ===========================================================
# PART 6: Same Method - Different Behavior
# ===========================================================


class Circle:

    def draw(self):

        print("Drawing a circle")


class Square:

    def draw(self):

        print("Drawing a square")


class Triangle:

    def draw(self):

        print("Drawing a triangle")


shapes = [

    Circle(),
    Square(),
    Triangle()

]


for shape in shapes:

    shape.draw()


# All classes use:
#
# draw()
#
# But each object has
# different behavior.



# ===========================================================
# PART 7: Polymorphism with Functions
# ===========================================================


def make_sound(animal):

    animal.sound()


class Dog:

    def sound(self):

        print("Woof")


class Cat:

    def sound(self):

        print("Meow")


dog = Dog()
cat = Cat()


make_sound(dog)
make_sound(cat)


# The function does not need to know
# the exact type of object.
#
# It only expects the object
# to have a sound() method.



# ===========================================================
# PART 8: Real-World Example - Payment
# ===========================================================


class Payment:

    def pay(self):

        print("Processing payment")


class CreditCard(Payment):

    def pay(self):

        print("Payment using Credit Card")


class PayPal(Payment):

    def pay(self):

        print("Payment using PayPal")


class Cash(Payment):

    def pay(self):

        print("Payment using Cash")


payments = [

    CreditCard(),
    PayPal(),
    Cash()

]


for payment in payments:

    payment.pay()



# ===========================================================
# PART 9: Another Example
# ===========================================================


class Person:

    def introduce(self):

        print("I am a person")


class Student(Person):

    def introduce(self):

        print("I am a student")


class Teacher(Person):

    def introduce(self):

        print("I am a teacher")


class Doctor(Person):

    def introduce(self):

        print("I am a doctor")


people = [

    Student(),
    Teacher(),
    Doctor()

]


for person in people:

    person.introduce()



# ===========================================================
# PART 10: Built-in Polymorphism
# ===========================================================


"""
Python also has built-in polymorphism.

For example:

len()

The same function works with
different data types.
"""


text = "Hello"

numbers = [1, 2, 3, 4, 5]

data = {

    "name": "Sara",
    "age": 23

}


print(len(text))
print(len(numbers))
print(len(data))


# len() works with:
#
# String
# List
# Dictionary



# ===========================================================
# PART 11: Polymorphism + Inheritance
# ===========================================================


class Animal:

    def move(self):

        print("Animal is moving")


class Bird(Animal):

    def move(self):

        print("Bird is flying")


class Fish(Animal):

    def move(self):

        print("Fish is swimming")


class Snake(Animal):

    def move(self):

        print("Snake is crawling")


animals = [

    Bird(),
    Fish(),
    Snake()

]


for animal in animals:

    animal.move()



# ===========================================================
# PART 12: Important Notes
# ===========================================================


"""
Polymorphism means:

One method name.

Different behaviors.


Example:

Dog.sound()

Cat.sound()

Cow.sound()


All use:

sound()

But each object produces
a different result.


Benefits:

- Makes code more flexible.
- Makes code easier to extend.
- Works well with inheritance.
- Reduces the need for many conditions.
"""


# ===========================================================
# PART 13: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create three classes:
#
# Dog
# Cat
# Cow
#
# Add a method called:
#
# sound()
#
# Each class should print
# a different sound.
#
# Store the objects in a list
# and use a loop to call sound().


# -----------------------------------------------------------


# Exercise 2:
#
# Create a parent class:
#
# Vehicle
#
# Add a method:
#
# move()
#
# Create child classes:
#
# Car
# Plane
# Boat
#
# Override move() in each class.
#
# Store the objects in a list
# and use a loop.


# -----------------------------------------------------------


# Exercise 3:
#
# Create a parent class:
#
# Employee
#
# Add:
#
# work()
#
# Create:
#
# Manager
# Developer
# Designer
#
# Override work() in each class.
#
# Use a loop to call work().


# -----------------------------------------------------------


# Exercise 4:
#
# Create a function called:
#
# display_sound()
#
# The function receives an object
# and calls:
#
# sound()
#
# Test it with different objects.


###########################################################
# END OF POLYMORPHISM
###########################################################