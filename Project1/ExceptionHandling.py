# Exception Handling - prevents the program from crashing and allows it to handle errors

# Exception - Error that occurs  while program is running

num1 = 10
num2 = 0

#print(num1 / num2) # cant divided by zero

# a = int(input("Enter Number 1 :"))
# b = int(input("Enter Number 2 : "))

# print("Result : ", a/b) # causing ZeroDivisionError
#
# print("HEllo ")

# try and except
try:
    a = int(input("Enter Number 1 :"))
    b = int(input("Enter Number 2 : "))

    print("Result : ", a / b)  # causing ZeroDivisionError
except ZeroDivisionError:  # Handle error
    print("Cannot divide by ZERO")

print("Hello World!!!")

try:
    age = int(input("Enter ur AGE : "))
    print(age)
except ValueError:
    print("Please, Enter Valid number!!!!")
finally:   # you can use else
    print("Successfully Handle Exception")

# ZeroDivisionError - Divide by zero
# ValueError  - Invalid data type
# TypeError - Wrong data type
# IndexError - Invalid list index
# keyError - Dictionary key not found
# FileNotFoundError - File does not exist


try:
    list = [1, 2, 3, 4, 5]

    print(list[10])
except IndexError:
    print("Out of Bound Index")



