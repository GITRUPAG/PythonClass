# tuple - collection of items
# ordered
# Immutable - cannot be changed
# allows duplicates

colors = ("red", "green", "orange", "red")
numbers = (1, 2, 3, 4, 5, 6)

print(colors)

colors[0] = "pink"

print(colors[0])

print(colors.count("red")) # count occurrences

print(colors.index("red")) # find position

