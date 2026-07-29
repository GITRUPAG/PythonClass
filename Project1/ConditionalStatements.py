# Conditional Statements - allow a program to
#               make decisions based on conditions
# if, if else, if elif else, nested if

# if statements - used when you want to execute code only if a condition is true
age = 20
if age >= 18:
    print("Eligible to Vote")

name = "rupa"
if name == "Alice":
    print("Name Matched")
else:
    print("Name not matched!!!")

num = 100
if num < 10:
    print("num is lesser")
else:
    print("Greater!!")

marks = 15

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

age = 15
has_license = True

if age >= 18:
    if has_license:
        print("Can Drive!!!")
else:
    print("Cant Drive!!")

# Even and Odd numbers

# if number divided by 2 then it is even else it is odd

# Find th largest of two number

# Create a login system
 # username = "admin" and password = "1234"
# print success or failure

age = 150
location = "USA"

if age != 15 or location == "india":
    print("Eligible")
else:
    print("Not Eligible")

# is and is not are identity operators

a = 10
b = 10

print( a is b) # check memory location

list = [1, 2, 3]
list1 = [1,2,3]

print(list is list1)


