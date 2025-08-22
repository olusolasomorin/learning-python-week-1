# Creating sets
#1. Using curly braces
fruits = {"apple", "banana", "mango"}
print(fruits)

#2. Using the set() constructor
numbers = set([1, 2, 3, 4])
print(numbers)

#3. Creating an empty set (must use set(), not{})
empty_set = set()
print(empty_set)

#4. from a string (duplicates removed automatically)
letters = set("mississippi")
print(letters)

# Set Operations
#1. Adding elements
colors = {"red", "blue"}
colors.add("green")
print(colors)

#2. Removing elements
colors.remove("blue")
colors.discard("yellow")
print(colors)

#3. Pop an element
colors = {"red", "blue", "green"}
removed = colors.pop()
print("Removed:", removed)
print("Remaining:", colors)

#4. Clear a set
colors.clear()
print(colors)

# Mathematical set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

#1. Union
print(set1 | set2)
print(set.union(set2))

#2. Intersection
print(set1 & set2)
print(set.intersection(set2))

#3. Difference
print(set1 - set2)
print(set1.difference(set2))

#4. symmetric difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# Working with sets
# collecting unique visitors to an event
visitors = set()

# Adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu")
print("Visitors:", visitors)

# Checking if a visitor attended
name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")    