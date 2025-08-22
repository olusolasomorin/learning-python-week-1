# How to create a list
# Creating a list with an empty 
# Method1: Using square brackets
empty_list = []
print(empty_list)

# Method2: Using the list() constructor
empty_list2 = list()
print(empty_list2)

# Creating a list with initial elements.
# List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)

# Creating a list from another sequence. you can convert strings, tuples, or other iterables into a list.
# From a string (each character becomes an element)
chars = list("hello")
print(chars)

# From a tuple
my_tuple = (10,20,30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# From a range
numbers_range = list(range(5))
print(numbers_range)

# Creating a list using list comprehnesion. List comprehensions are a concise way to create lists using a loop in one line.
# squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares)

# Even numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)

# creating a nested list. A list can contain other lists it is useful for matrices or grouped data.
# Matrix-like list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)

# Accessing elements in a nested list
print(matrix[1])
print(matrix[0][1])

# Characteristics of a list
#1. ordered collection
# The elements in a list maintain the order in which they are inserted.
# - The first element has index 0, the second has index 1, and so on.
fruits = ["mango", "orange", "banana"]
print(fruits)
print(fruits[0])
print(fruits[2])
print(fruits[0])

#2. Allows Duplicates
# Lists can store the same value multiple times.
items = ["rice", "beans", "yam", "rice"]
print(items)

#3. Mutable (Can Be changed)
# You canmodify a list after it's created-change elements, add new ones, or remove exisiting ones.
numbers = [1, 2, 3]
numbers[1] = 20
print(numbers)

#4. can contain different data types
# A list can hold integers, strings, floats, booleans, and even other lists.
mixed = [10, "Nigeria", 3.14, True]
print(mixed)

#5. Can be nested 
# A list can contain other lists (2D or multi-dimensional lists).
nested_list = [[1, 2], ["a","b"]]
print(nested_list)
print(nested_list[0][1])

#6. Dynamic size
# You don’t need to declare the size of a list beforehand; it can grow or shrink as needed.
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
print(names)