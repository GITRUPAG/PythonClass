
# Assignment Operators

s = 10  # 1011
s= 20 # 0111

a = 5 # 101
b = 3 # 011

# &
print(5 & 3)  # 1  001 - return 1  both bits  are 1

print(5 | 3) # at least one bit is 1

print(5 ^ 3) # returns when both bits are different

print(~5)

s = s + 10

s += 10

s -= 5

s *= 5

s /= 10

print(s)

# Membership Operators - check if value is present or not

nums = [1, 2, 6, 8, 10, 23, 56, 89]

print(24 in nums)

print(24 not in nums)

# Identity Operators - check memory identity
a = [1, 2]
b = a

c = 1000

print(a is b)

print( a is c)

print(a is not c)

# Bitwise Operators





