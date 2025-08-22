# A tuple is an ordered, immutable(unchangeable) collection of items in python
# Creatin tuples
#1. Using parentheses()
fruits = ("apple", "banana", "cherry")
print(fruits)

#2. Without parentheses (tuple packing)
numbers = 1, 2, 3
print(numbers)

#3. Single-item tuple (must include a comma)
single_item = ("apple",)
print(single_item)
print(type(single_item))

#4. Using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# Characteristics of tuples
#1. Ordered 
colors = ("red", "green", "blue")
print(colors[0])

# Immutable ( uncomment and run. This will cause an error)
#colors[1] = "yellow"

# Allow duplicates
numbers = (1, 2, 2, 3)
print(numbers)

# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)

# Nested tuples
nested = (("a", "b"), (1, 2))
print(nested)

# tuples operations
#1. indexing
fruits = ("apple","banana","cherry")
print(fruits[1])
print(fruits[-1])

#2. Slicing
print(fruits[0:2])
print(fruits[::-1])

#3. Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)

#4. Repetition
nums = (1, 2)
print(nums * 3)

#5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" not in fruits)

#6. Iteration
for fruit in fruits:
    print(fruit)

# Unpacking Tuples
person = ("john", 25, "Nigeria")
name, age, country, = person
print(name)
print(age)
print(country)

# Tuple methods
# don't count() and dot index()
numbers = (1, 2, 2, 3, 4)
print(numbers.count(2)) #(counts occurrences of 2)
print(numbers.index(3)) #(position of first occurrence of 3)

# Converting between list and tuple
# tuple to list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)

# list back to tuple
t = tuple(lst)
print(t)

# built-in functions with tuples
nums = (4, 1, 7, 3)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))