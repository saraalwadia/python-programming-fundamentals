###########################################################
# Encapsulation in Python
###########################################################


"""
Encapsulation means:

Keeping data and methods together inside a class.

It also helps us control how attributes
are accessed and changed.

Python uses naming conventions for attributes:

Public:
    name

Protected:
    _name

Private:
    __name
"""


# ===========================================================
# PART 1: Public Attributes
# ===========================================================


"""
Public attributes can be accessed
from anywhere.
"""


class Person:

    def __init__(self, name):

        self.name = name


person = Person("Sara")


print(person.name)


# We can change a public attribute.

person.name = "Joe"


print(person.name)



# ===========================================================
# PART 2: Protected Attributes
# ===========================================================


"""
A protected attribute starts with:

_

Example:

_name

It means that the attribute should
normally be used inside the class
or its child classes.

Python still allows direct access.
"""


class Person:

    def __init__(self, name):

        self._name = name


person = Person("Sara")


print(person._name)


# This works in Python,
# but protected attributes
# should be used carefully.



# ===========================================================
# PART 3: Private Attributes
# ===========================================================


"""
A private attribute starts with:

__

Example:

__name

It should not be accessed directly
from outside the class.
"""


class Person:

    def __init__(self, name):

        self.__name = name


person = Person("Sara")


# This will cause an error:

# print(person.__name)



# ===========================================================
# PART 4: Access Private Attribute
# ===========================================================


"""
We can access a private attribute
using a method.
"""


class Person:

    def __init__(self, name):

        self.__name = name


    def get_name(self):

        return self.__name


person = Person("Sara")


print(person.get_name())



# ===========================================================
# PART 5: Change Private Attribute
# ===========================================================


class Person:

    def __init__(self, name):

        self.__name = name


    def get_name(self):

        return self.__name


    def set_name(self, name):

        self.__name = name


person = Person("Sara")


print(person.get_name())


person.set_name("Joe")


print(person.get_name())



# ===========================================================
# PART 6: Getter and Setter
# ===========================================================


"""
Getter:

Used to get a value.

Setter:

Used to change a value.
"""


class Student:

    def __init__(self, name, age):

        self.__name = name

        self.__age = age


    def get_name(self):

        return self.__name


    def get_age(self):

        return self.__age


    def set_name(self, name):

        self.__name = name


    def set_age(self, age):

        self.__age = age


student = Student("Sara", 23)


print(student.get_name())

print(student.get_age())


student.set_name("Joe")

student.set_age(25)


print(student.get_name())

print(student.get_age())



# ===========================================================
# PART 7: Validation Using Setter
# ===========================================================


"""
One important benefit of encapsulation
is validating data before changing it.
"""


class Student:

    def __init__(self, name, mark):

        self.name = name

        self.__mark = mark


    def get_mark(self):

        return self.__mark


    def set_mark(self, mark):

        if 0 <= mark <= 100:

            self.__mark = mark

        else:

            print("Invalid mark")


student = Student("Sara", 90)


print(student.get_mark())


student.set_mark(95)


print(student.get_mark())


student.set_mark(150)



# ===========================================================
# PART 8: Practical Example - Bank Account
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


account.deposit(-20)



# ===========================================================
# PART 9: Another Practical Example
# ===========================================================


class User:

    def __init__(self, username, password):

        self.username = username

        self.__password = password


    def check_password(self, password):

        if password == self.__password:

            print("Correct password")

        else:

            print("Wrong password")


user = User("sara", "1234")


print(user.username)


user.check_password("1234")

user.check_password("0000")



# ===========================================================
# PART 10: Public vs Protected vs Private
# ===========================================================


"""
Public:

self.name

Can be accessed anywhere.


Protected:

self._name

Should normally be used inside
the class or child classes.


Private:

self.__name

Cannot be accessed directly
using the normal attribute name.

Usually accessed using methods.
"""


# ===========================================================
# PART 11: Why Use Encapsulation?
# ===========================================================


"""
Encapsulation helps us:

- Protect data.
- Control access to attributes.
- Validate data before changing it.
- Keep code organized.
"""


# ===========================================================
# PART 12: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Create a class called:
#
# Person
#
# Add a private attribute:
#
# __name
#
# Create a method:
#
# get_name()
#
# Return the name.
# -----------------------------------------------------------


# Exercise 2:
#
# Create a class called:
#
# Student
#
# Add a private attribute:
#
# __mark
#
# Create:
#
# get_mark()
#
# set_mark(mark)
#
# Only allow marks between:
#
# 0 and 100.
# -----------------------------------------------------------


# Exercise 3:
#
# Create a class called:
#
# BankAccount
#
# Add a private attribute:
#
# __balance
#
# Create methods:
#
# get_balance()
#
# deposit(amount)
#
# Only allow positive amounts.
# -----------------------------------------------------------


# Exercise 4:
#
# Create a class called:
#
# User
#
# Add:
#
# username
#
# __password
#
# Create a method:
#
# check_password(password)
#
# Check if the password is correct.
# -----------------------------------------------------------


###########################################################
# END OF ENCAPSULATION
###########################################################