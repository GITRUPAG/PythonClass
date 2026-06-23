#Function - Reusable Block of code to perform
# a specific task

# BENEFITS
# Reuse of code
# Reduce Repetition
# Easy to maintain
# makes program organized

# 100
# print("Good Morning!!!!")
#
# print("Good Afternoon!!!!")
#
# print("Good Night!!!!")


def greet():
    print("Welcome!!!")
    print("Good Morning!!!!")
    print(10 + 10)

def greetAfternoon():
    print("Welcome!!!")
    print("Good Afternoon!!!!")

# greet()

greet()

time = 20
if(time <=12):
    greet()

if(time >= 12):
    greetAfternoon()

#Function With Parameters
# sending data to a function
def greetWithName(name):
    print("Hello", name)

greetWithName("Rupa")

def add(a, b):
    print(a + b)

add(10.2022, 10)


def is_adult(age):
    return age >= 18

if is_adult(15):
    print("ADULT")
else:
    print("NOT AN ADULT!!!")

def sub(a, b):
    return a-b

print(sub(20,10))


def check_pass(marks):
    if marks >= 35:
        return True
    else:
        return False

print(check_pass(10))

def login(username, password):
    return username == "admin" and password=="1234"

print(login("admin", 1234))

