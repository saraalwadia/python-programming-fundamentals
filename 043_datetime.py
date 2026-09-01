###########################################################
# Date and Time in Python
###########################################################


"""
The datetime module is used to work with:

- Dates
- Time
- Date and time together

Before using datetime, we need to import it.
"""


# ===========================================================
# PART 1: Import datetime
# ===========================================================


import datetime


print(datetime.datetime.now())



# ===========================================================
# PART 2: Current Date and Time
# ===========================================================


now = datetime.datetime.now()


print("Current Date and Time:", now)



# ===========================================================
# PART 3: Current Date
# ===========================================================


today = datetime.date.today()


print("Today's Date:", today)



# ===========================================================
# PART 4: Current Time
# ===========================================================


current_time = datetime.datetime.now().time()


print("Current Time:", current_time)



# ===========================================================
# PART 5: Access Date Information
# ===========================================================


now = datetime.datetime.now()


print("Year:", now.year)

print("Month:", now.month)

print("Day:", now.day)

print("Hour:", now.hour)

print("Minute:", now.minute)

print("Second:", now.second)



# ===========================================================
# PART 6: Create a Specific Date
# ===========================================================


birthday = datetime.date(2000, 5, 10)


print("Birthday:", birthday)



# ===========================================================
# PART 7: Create a Specific Date and Time
# ===========================================================


meeting = datetime.datetime(
    2026,
    9,
    1,
    10,
    30,
    0
)


print("Meeting:", meeting)



# ===========================================================
# PART 8: strftime()
# ===========================================================


"""
strftime() is used to convert
a date or time into a formatted string.
"""


now = datetime.datetime.now()


print(now.strftime("%Y"))

print(now.strftime("%m"))

print(now.strftime("%d"))


print(now.strftime("%Y-%m-%d"))


print(now.strftime("%d/%m/%Y"))


print(now.strftime("%H:%M:%S"))


print(now.strftime("%A"))


print(now.strftime("%B"))



# ===========================================================
# PART 9: Common Format Codes
# ===========================================================


"""
%Y = Year

%m = Month number

%d = Day

%H = Hour

%M = Minute

%S = Second

%A = Day name

%B = Month name
"""


# ===========================================================
# PART 10: strptime()
# ===========================================================


"""
strptime() converts a string
into a datetime object.
"""


date_text = "2026-09-01"


date_object = datetime.datetime.strptime(
    date_text,
    "%Y-%m-%d"
)


print(date_object)



# ===========================================================
# PART 11: Date Difference
# ===========================================================


date1 = datetime.date(2026, 1, 1)

date2 = datetime.date(2026, 12, 31)


difference = date2 - date1


print("Days Difference:", difference.days)



# ===========================================================
# PART 12: timedelta()
# ===========================================================


"""
timedelta is used to add or subtract
days, weeks, or other time periods.
"""


today = datetime.date.today()


future_date = today + datetime.timedelta(days=7)


print("Date After 7 Days:", future_date)



# Subtract days


previous_date = today - datetime.timedelta(days=7)


print("Date Before 7 Days:", previous_date)



# ===========================================================
# PART 13: Add Weeks
# ===========================================================


today = datetime.date.today()


next_week = today + datetime.timedelta(weeks=1)


print("Next Week:", next_week)



# ===========================================================
# PART 14: Practical Example - Calculate Age
# ===========================================================


birth_year = int(input("Enter your birth year: "))


current_year = datetime.date.today().year


age = current_year - birth_year


print("Your age is:", age)



# ===========================================================
# PART 15: Practical Example - Days Until Event
# ===========================================================


event_date = datetime.date(2026, 12, 31)


today = datetime.date.today()


remaining_days = event_date - today


print("Days remaining:", remaining_days.days)



# ===========================================================
# PART 16: Important Notes
# ===========================================================


"""
datetime.datetime

Used for:

Date + Time


datetime.date

Used for:

Date only


datetime.time

Used for:

Time only


datetime.timedelta

Used for:

Adding or subtracting time.
"""


# ===========================================================
# PART 17: Practice Exercises
# ===========================================================


# Exercise 1:
#
# Print the current:
#
# Year
# Month
# Day
# Hour
# Minute


# -----------------------------------------------------------


# Exercise 2:
#
# Ask the user to enter:
#
# Birth year
#
# Calculate and print their age.


# -----------------------------------------------------------


# Exercise 3:
#
# Create a date representing:
#
# Your birthday
#
# Print it in this format:
#
# Day/Month/Year


# -----------------------------------------------------------


# Exercise 4:
#
# Create a future date.
#
# Calculate how many days
# remain until that date.


# -----------------------------------------------------------


# Exercise 5:
#
# Get today's date.
#
# Print:
#
# Yesterday
#
# Today
#
# Tomorrow
#
# Use timedelta().


###########################################################
# END OF DATE AND TIME
###########################################################
