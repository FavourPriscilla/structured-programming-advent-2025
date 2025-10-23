'''
Dictionary is a collection of key-value pairs.

Represented as {}

Each key is unique and its mapped to a specific value.

'''

student = {
    "name" : "Derrick",
    "age" : 24,
    'course' : "Information Technology",
}

print(student)

##access dictionary values
#1. keys
print(student["name"])

##2. get method
print(student.get("course"))

##adding values to the dictionary
student["university"] = "UCU" ##creating a new field
student["age"] = 22   ## update on an existing field
   ##updating an existing field