# ===========================================================
# Dictionaries in Python
# ===========================================================


# A dictionary stores data as key-value pairs.
# Dictionary is:
# - Mutable (can be changed)
# - Ordered (keeps insertion order)
# - Accessed using keys, not indexes
# - Written using {}


# ===========================================================
# Part 1: Creating Dictionaries
# ===========================================================


# Create a dictionary

person = {
    "name": "Sara",
    "age": 23,
    "major": "IT"
}


print(person)


# Check type

print(type(person))



# ===========================================================
# Part 2: Accessing Dictionary Data
# ===========================================================


# Access value using key

print(person["name"])

print(person["age"])



# Using get()
# Returns the value of a key

print(person.get("major"))



# get() returns None if key does not exist

print(person.get("country"))



# ===========================================================
# Part 3: Adding Data
# ===========================================================


# Add a new key-value pair

person["country"] = "Palestine"


print(person)



# ===========================================================
# Part 4: Updating Data
# ===========================================================


# Change the value of an existing key

person["age"] = 24


print(person)



# update()
# Add or update multiple values

person.update({
    "age": 25,
    "city": "Gaza"
})


print(person)



# ===========================================================
# Part 5: Deleting Data
# ===========================================================


person = {
    "name": "Sara",
    "age": 23,
    "major": "IT"
}



# pop()
# Removes a key and returns its value

removed_value = person.pop("age")


print(person)

print(removed_value)



# del
# Removes a key

del person["major"]


print(person)



# clear()
# Removes all data

person.clear()


print(person)



# ===========================================================
# Part 6: Dictionary Methods
# ===========================================================


student = {
    "name": "Sara",
    "age": 23,
    "major": "IT"
}



# keys()
# Returns all keys

print(student.keys())



# values()
# Returns all values

print(student.values())



# items()
# Returns key-value pairs

print(student.items())



# ===========================================================
# Part 7: Loop Through Dictionary
# ===========================================================


# Loop through keys

for key in student:
    print(key)



# Loop through values

for value in student.values():
    print(value)



# Loop through keys and values

for key, value in student.items():
    print(key, ":", value)



# ===========================================================
# Part 8: Nested Dictionary
# ===========================================================


# Dictionary can contain another dictionary


students = {

    "student1": {
        "name": "Sara",
        "age": 23
    },

    "student2": {
        "name": "Adam",
        "age": 22
    }

}



print(students)



# Access nested values

print(students["student1"]["name"])

print(students["student2"]["age"])



# ===========================================================
# Part 9: Dictionary with Lists
# ===========================================================


student = {

    "name": "Sara",

    "skills": [
        "Python",
        "SQL",
        "Machine Learning"
    ]

}


print(student)


# Access list inside dictionary

print(student["skills"][0])



# ===========================================================
# Part 10: Dictionary vs List
# ===========================================================


# List:
# - Access data using index
# - Uses []
# - Ordered collection


numbers = [10, 20, 30]


print(numbers[0])



# Dictionary:
# - Access data using key
# - Uses key:value
# - Useful for structured data


person = {
    "name": "Sara",
    "age": 23
}


print(person["name"])



# ===========================================================
# Practice
# ===========================================================


# Create a dictionary called:

# employee


# Add:

# name
# age
# department
# salary


# Print employee information.


# Update salary.


# Add a new key:
# country


# Delete one key.


# Print all keys and values.