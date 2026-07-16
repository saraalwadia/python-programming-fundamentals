###########################################################
# Complex Numbers in Python
###########################################################

# Python supports different data types:
# int, float, string, boolean, complex


###########################################################
# 1. Creating Complex Numbers
###########################################################

# A complex number consists of:
# Real part + Imaginary part

# Syntax:
# a + bj

z = 3 + 4j

print(z)

print(type(z))



###########################################################
# 2. Real and Imaginary Parts
###########################################################

# real:
# Returns the real part of the complex number

print("Real part:", z.real)


# imag:
# Returns the imaginary part

print("Imaginary part:", z.imag)



###########################################################
# 3. Creating Complex Numbers using complex()
###########################################################

# We can create complex numbers using complex()

z1 = complex(2, 5)

print(z1)


# This means:
# Real part = 2
# Imaginary part = 5



###########################################################
# 4. Complex Number Operations
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
# 5. Using Complex Numbers in Expressions
###########################################################

z = 5 + 2j

result = z * 2

print(result)



###########################################################
# 6. Finding Magnitude (Absolute Value)
###########################################################

# abs() returns the distance from zero

z = 3 + 4j

print(abs(z))


# Result:
# sqrt(3² + 4²)
# = 5



###########################################################
# 7. Conjugate
###########################################################

# The conjugate changes the sign of imaginary part

z = 3 + 4j

print(z.conjugate())


# Output:
# 3 - 4j



###########################################################
# 8. Example: Representing a Point
###########################################################

# Complex numbers can represent points
# in a 2D coordinate system.

point = 4 + 7j


x = point.real
y = point.imag


print("X =", x)
print("Y =", y)



###########################################################
# 9. Checking Complex Type
###########################################################

number = 10 + 5j


if isinstance(number, complex):
    print("This is a complex number")



###########################################################
# Practice
###########################################################

# Create two complex numbers:

# z1 = 6 + 2j
# z2 = 3 + 5j


# Calculate:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Real part of z1
# 5. Imaginary part of z2