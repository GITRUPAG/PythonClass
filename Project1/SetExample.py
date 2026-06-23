# set - collection of items
# No duplicates
# Unordered
# Mutable

nums = {1, 2, 3}

# add one element
nums.add(3)
nums.add(2)
nums.add(4)

print(nums)

# adding multiple elements
nums.update((5, 6))
print(nums)

# remove element
nums.remove(2)

# safe remove
nums.discard(7)
print(nums)

# remove random element
nums.pop()

nums.clear()

print(nums)