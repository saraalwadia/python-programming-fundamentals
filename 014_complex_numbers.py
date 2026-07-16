# ===========================================================
# Lesson: Complex Numbers in Python
# ===========================================================


"""
Teaching Notes:

Lesson Objectives:
- Understand what complex numbers are.
- Learn how to create complex numbers in Python.
- Access real and imaginary parts.
- Perform mathematical operations on complex numbers.


Prerequisites:
- Variables
- Data Types
- Arithmetic Operators


What are Complex Numbers?

Complex numbers are numbers that contain:

Real part + Imaginary part


Mathematical form:

a + bi


In Python:

a + bj


Important Note:

Python uses "j" instead of "i"
for the imaginary part.


Example:

z = 3 + 4j


Real part:
3

Imaginary part:
4j



Where are Complex Numbers Used?

- Engineering
- Physics
- Signal Processing
- Electrical circuits
- Mathematics
- Machine Learning algorithms


Python supports these basic numeric types:

1. int
   Example:
   10


2. float
   Example:
   10.5


3. complex
   Example:
   3 + 4j


"""



###########################################################
# Part 1: Creating Complex Numbers
###########################################################


# A complex number consists of:
# Real part + Imaginary part


# Syntax:
# real + imaginary j


z = 3 + 4j


print(z)


print(type(z))




###########################################################
# Part 2: Accessing Real and Imaginary Parts
###########################################################


# real:
# Returns the real part of the complex number


print("Real part:", z.real)



# imag:
# Returns the imaginary part


print("Imaginary part:", z.imag)




###########################################################
# Part 3: Creating Complex Numbers using complex()
###########################################################


# We can create complex numbers
# using the complex() function


# Syntax:

# complex(real, imaginary)


z1 = complex(2, 5)


print(z1)



# This means:

# Real part = 2
# Imaginary part = 5




###########################################################
# Part 4: Complex Number Operations
###########################################################


z1 = 2 + 3j

z2 = 1 + 4j



# Addition

print("Addition:", z1 + z2)



# Subtraction

print("Subtraction:", z1 - z2)



# Multiplication

print("Multiplication:", z1 * z2)



# Division

print("Division:", z1 / z2)




###########################################################
# Part 5: Using Complex Numbers in Expressions
###########################################################


z = 5 + 2j


result = z * 2


print(result)




###########################################################
# Part 6: Magnitude (Absolute Value)
###########################################################


# abs() returns the distance of the complex number
# from zero.


z = 3 + 4j


print(abs(z))



# Calculation:

# sqrt(real² + imaginary²)

# sqrt(3² + 4²)

# sqrt(9 + 16)

# = 5




###########################################################
# Part 7: Complex Conjugate
###########################################################


# conjugate() changes the sign
# of the imaginary part.


z = 3 + 4j


print(z.conjugate())



# Output:

# 3 - 4j




###########################################################
# Part 8: Complex Numbers as Coordinates
###########################################################


# Complex numbers can represent points
# in a 2D coordinate system.


# Real part represents X-axis

# Imaginary part represents Y-axis



point = 4 + 7j



x = point.real

y = point.imag



print("X =", x)

print("Y =", y)




###########################################################
# Part 9: Checking Complex Type
###########################################################


number = 10 + 5j



if isinstance(number, complex):

    print("This is a complex number")




###########################################################
# Practice
###########################################################


"""
Create two complex numbers:


z1 = 6 + 2j

z2 = 3 + 5j



Calculate:


1. Addition

2. Subtraction

3. Multiplication

4. Real part of z1

5. Imaginary part of z2

"""