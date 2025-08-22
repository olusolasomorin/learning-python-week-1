#1. dot append() method
# Adds an element to the end of the list.
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)

#2. dot insert() method
# inserts an element at a specific position
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)

#3. dot extend() method
# Adds elements from another list (or iterable) to the end.
fruits = ["apple", "banana"]
tropical =["mango", "pineapple"]
fruits.extend(tropical)
print(fruits)

#4. dot remove() method
# Removes the first occurrence of a specified value.
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)

#5. dot pop() method
# Removes and returns the element at a given index(default: last).
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()
print(last_fruit)
print(fruits)

#6. dot clear() method
# Removes all elements from the list.
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

#7. dot index() method
# Returns the index of the first occurence of a value.
fruits = ["apple", "banana","cherry"]
position = fruits.index("banana")
print(position)

#8. dot count() method
# Counts how many times a value appears.
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))

#9. dot sort() method
# Sorts the list in ascending order (default).
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)
# descending order
numbers.sort(reverse=True)
print(numbers)

#10. dot reverse() method
# Reverses the order of the list.
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)

#11. dot copy()
# returns a shallow copy of the list (This should be familiar already)
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)