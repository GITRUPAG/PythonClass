# While Loop
# executes when a block of code as long as condition is true

# syntax while condition:
             # statements

# print 1 to 5

num = 1 # 2 3

while num <= 15:
    print(num)
    num= num + 1 # num += 1

# even Numbers
n = 2
while n <= 10:
    print(n)
    n = n + 2
# 1, 2, 3, 4, 5
num = 1
sum = 0

while num <= 5:
    sum = sum + num
    num += 1

print("Sum : ",sum)

# break statement - stop the loop immediately
print("Break Statement")
count = 1

while count <= 10:
    if count == 5:
        break
    print(count)
    count +=1

print("ODD Numbers")
# continue statement - skips the iteration

count = 0

while count <= 10:
    count += 1
    if count == 6:
        continue
    print(count)


name = "Rupa"

print("Name : ", name)
