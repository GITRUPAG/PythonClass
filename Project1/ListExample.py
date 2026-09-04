# List - Collection of items
# Ordered - Its maintain Insertion order
# Mutable - can change
# Allows Duplicates
# Each item has index (position) starting from 0
# from dataTypesExamples import number

fruits = ["apple", "banana", "pineapple", "banana", "apple"]
numbers = [1, 12, 30, 41, 5]
floats = [1.20, 5.36, 8.20]
grades = ['a', 'b', 10, 20]

print("grapes" not in fruits)


print(fruits)
print(fruits[2])
print(fruits[0])

# Methods

# Adding an item
fruits.append("grapes")
numbers.append(10)
print(fruits)
print(numbers)

# Add multiple items
fruits.extend(["watermelon", "muskmelon", "sapota"])
print(fruits)

# Add at specific position
fruits.insert(1, "watermelon")
fruits.insert(0, "Dragon Fruit")
print(fruits)

# Remove value
fruits.remove("banana")
print(fruits)
fruits.remove("banana")
print(fruits)

# Remove by index
fruits.pop(1) # specific index
print(fruits)
fruits.pop() # last item deleted
print(fruits)

# find position
print(fruits.index("watermelon"))

# count occurrences
print(fruits.count("watermelon"))

# sort list
numbers.sort() # ascending
print(numbers)

numbers.sort(reverse=True) # descending
print(numbers)

# reverse list
primes = [2, 13, 15, 7, 9, 13]
primes.reverse()
print(primes)

# copy list
new_list = primes.copy()
print(new_list)

# list slicing
print(new_list[0:4])

print(len(new_list))

# Remove all items
fruits.clear()
print(fruits)


