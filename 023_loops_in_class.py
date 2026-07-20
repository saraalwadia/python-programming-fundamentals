###########################################################
# Practice Exercises - If, Dictionary & Loops
###########################################################


"""
Teaching Notes:

Lesson Objectives:

- Practice using if statements.
- Practice using dictionaries.
- Practice using for loops.
- Apply modulus operator % in real problems.
- Solve simple programming problems.


Topics Covered:

PART 1:
Leap Year Check

- Use % operator to check divisibility.
- If year is divisible by 4, it is considered leap.


PART 2:
Months Dictionary

- Store data using key-value pairs.
- Use user input to access dictionary values.
- Use loop and break to search for data.


PART 3:
Numbers with Conditions

- Use for loop with if condition.
- Filter numbers based on specific rules.

"""



# ===========================================================
# PART 1: Leap Year or Normal Year
# ===========================================================


year = int(input("Enter year: "))


# A year is leap if it is divisible by 4

if year % 4 == 0:

    print("Leap Year")


else:

    print("Normal Year")



# ===========================================================
# PART 2: Find Month Name Using Dictionary
# ===========================================================


months = {

    1: "Jan",

    2: "Feb",

    3: "Mar",

    4: "Apr",

    5: "May",

    6: "Jun",

    7: "Jul",

    8: "Aug",

    9: "Sep",

    10: "Oct",

    11: "Nov",

    12: "Dec"

}



number = int(input("Enter Month Number: "))



# Search for month number

for n in range(len(months) + 1):


    if n == number:

        print(months[n])

        break



# break:
# Stops the loop after finding the required value



# ===========================================================
# PART 3: Numbers Divisible by 7 and 5
# ===========================================================


numbers = []


# Check numbers between 1500 and 2700

for x in range(1500, 2701):


    if x % 7 == 0 and x % 5 == 0:

        numbers.append(str(x))



print(",".join(numbers))