num = -10

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Invalid Number")

# Even or odd
# 1,2,3,4,5,6
value = 25

if value % 2 == 0:
    print("EVEN")
else:
    print("ODD")

# USing logical Operators
age = 28
present = False

if age >= 18 and present == True:
    print("Access granted!!")
else:
    print("No Access")

if age >= 18 or present == True:
    print("Access granted!!")
else:
    print("No Access")

is_blocked = False

if not is_blocked == True:
    print("Login Allowed")
else:
    print("Blocked!!")


# ATM Withdrawal System
# Balance = 5000 and Withdraw_amount = 3000

# If withdrawal amount is
# less than or equal to balance , print "Transactional Successful"
# OtherWise print "Insufficient balance"

balance = 5000

withdraw = 6000

if withdraw <= balance:
    print("Transactional Successful")
else:
    print("Insufficient Balance!!")





