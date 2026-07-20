###########################################################
# Advanced If Statement & Dictionary Practice
###########################################################


"""
Teaching Notes:

Lesson Objectives:
- Practice using dictionaries.
- Understand if, elif, else with different conditions.
- Learn how to combine conditions using and / or.
- Learn nested if statements.
- Solve real-world decision problems.


Topics Covered:


PART 1: Dictionary
- Store data using key-value pairs.
- Keys must be unique.
- If a key is repeated, the last value replaces the previous one.


PART 2: If - Elif - Else
- Used to make decisions.
- Python checks conditions from top to bottom.
- The first True condition will execute.


PART 3: Logical Operators

and:
- Both conditions must be True.

or:
- At least one condition must be True.


PART 4: Nested If
- An if statement inside another if statement.
- Used when we have dependent conditions.


PART 5: Modulus Operator %
- Used to find the remainder.
- Useful for checking even and odd numbers.


Important Notes:
- Order of conditions matters.
- Put the most specific conditions first.
- Avoid unreachable conditions.
"""


# ===========================================================
# PART 1: Dictionary
# ===========================================================


# Dictionary stores data as key : value


hobbies = {

    "sara": "football",

    "adam": "basketball",

    "Jo": "swimming",

    # Duplicate keys are not allowed.
    # The last value will replace the previous one.

    "Jo": "english"
}


print(hobbies)



people = {

    1: "Sara",

    2: "Mohammed"

}


print(people)



# ===========================================================
# PART 2: Positive, Negative or Zero
# ===========================================================


number = float(input("Enter the number: "))


if number > 0:

    print("Positive")


elif number < 0:

    print("Negative")


else:

    print("Zero")



# ===========================================================
# PART 3: Simple Menu
# ===========================================================


choice = int(input("Enter your choice: "))


if choice == 1:

    print("Coffee")


elif choice == 2:

    print("Tea")


elif choice == 3:

    print("Water")


else:

    print("Sorry, I don't know that")



# ===========================================================
# PART 4: Certificate Grade
# ===========================================================


av = float(input("Enter your average: "))


if av >= 90:

    print("Excellent")


elif av >= 80:

    print("Very good")


elif av >= 70:

    print("Good")


elif av >= 60:

    print("Fairly Good")


else:

    print("Not so good")



# ===========================================================
# PART 5: Logical Operators (and / or)
# ===========================================================


x = int(input("Enter integer number: "))


# or:
# At least one condition must be True


if x >= 0 or x <= 20:

    print(True)


else:

    print(False)



# ===========================================================
# PART 6: Even or Odd
# ===========================================================


y = int(input("Enter integer number: "))


# Even numbers have remainder 0 when divided by 2


if y % 2 == 0:

    print("Even")


else:

    print("Odd")



# ===========================================================
# PART 7: Nested If Statement
# ===========================================================


# if inside another if


gender = input("Enter gender: ")

age = int(input("Enter your age: "))



if gender == "boy":


    if age > 0 and age < 18:

        print("Boy and child")


    else:

        print("Boy and adult")



else:


    if age > 0 and age < 18:

        print("Girl and child")


    else:

        print("Girl and Adult")