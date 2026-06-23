# variables - To store data

name = "alice"
value = 100
rupa = 36.0252
active = True




# Data Types
# Numeric
# Integer (int)
# x = 10
# # Float (decimal values)
# y = 10.50

# Arithmetic Operators
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)

# Boolean
isActive = True
isActive = False

print(isActive)

# Comparison operators - return True or false
# print(x > y) # x = 10, y = 10.50
# print(x < y)
# print(x == y) # equals
# print(x != y) # Not equals

# Logical operators
x = 10
y = 20
z = 30

# and, or, not Logical operators
print("AND ")
print(x > y and x > z)
print(x > y and x < z) # false
print(x > y or x < z) # true
print(x <= y )
print(x >=y)
print(x == y)
print(x != y)

print(x < y and x < z)

print(not True)

# Assignment operators - assign/update values
h = 20
h = h + 10 # h += 10
h = h - 30  # h -= 30
h = h * 4   # h *= 4 , h /= 2
print(h)

# membership operators - in, not in
primes = [2, 13, 15, 7, 9, 13]

print("Membership Operators")
print(15 in primes) # if present then it returns True else false

print(20 in primes) # false







# Dictionary key-value pairs   word -> meaning
# {
#     "name" : "Rupa",
#     "age" : 21
# }

student = {
    "name": "bob",
    "age": 25,
    "salary": 25000.500,
    "Details": {
        "marks": 50,
        "grade": 'P'
    }
    # "name":"rupa" ->Wrong
}
print(student["name"]) #bob
print(student["age"])
print(student["salary"])

# Adding new key-value pair into dictionary
student["city"] = "chennai"
print(student)

# Updating key-value pair
student["age"] = 22
student["city"] = "Hyderabad"
student["city"] = "Bangalore"
print(student)

# Removing key-value pair
student.pop("age")
print(student)

# Methods
print(student.keys()) # All keys
print(student.values()) # All values

# Rules
# Key must be unique
# key:value pair
# Its maintain insertion order
# Mutable
# No duplicates allowed


# Create a Dictionary Employee


user = {
    "name": "rupa",
    "age": 21,
    "skills": ["python", "react"]
}

user["skills"].append("java")

user

