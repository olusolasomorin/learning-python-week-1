# # Modularizing codes
# # Examples
# # range()
# for i in range(3):
#     print(i)

# # zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)

# # map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)

# # filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)

# # Student performance & feedback system

# # Step1: Input student data
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# #step2: store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # step3: Display data
# print("\nStudent Data:")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# # Step4: Summary using built - ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score", lowest)

# # Step5: Ranking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# # Step6: Check data types
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# # Step7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores:", passing)

# # Step8: Map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_names)

# # Step9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)


# USER DEFINED FUNCTION
# In Python, we use the `def` keyword to define a function.Then we call the function whenever we want to use it.
# Lets see the function structure
# def function_name(takes in input):
#     process block
#     output block

# More explanantion
# def funtion_name(input - here, you will insert an item or list of what the function will need to work):

#     "process block -here will contain the logic or what you want the function to do"

#     " output - Then here will contain what you want the function to output. You can either use the 'return' keyword or'print()' or 'yield'"

# Defining a function
def greet():
    print("Hello, welcome to AI Fellowship")

# When you want to use a function, this is how to call it.
# And you can call it as many times as possible.
greet()
greet()
greet()

# Function with an argument - the placeholder
def greet(name):
    print("Hello", name, "welcome to Python learning!")

# Calling with parameters - the actual name
greet("Class rep")
greet("RIdwan")

# When to Use return, print(), and yield keywords inside a function
#1. print()
#  You can use it if you are just interested in displaying your output (Not Storing). It does not give back a value you can use later.

#  Think of it like shouting information out loud, but not recording it for reference purpose.

#  So you use it when you just want to show results to the user.  Example: printing menus, reports, or logs.

def greet(name):
    print("Hello", name)

# Funtion call
result = greet("Esther")

# You will notice that it did not store the name
print("Result:", result)


#2. return
# You can use it if you want to give back a value.
# return sends a value back to the function caller.
# The function ends immediately once it hits return.
# Think of it like filling a form and handing it back, the caller now owns the result and can reuse it.
# So you can use `return` when you need the result for further computation or storage.For example, math calculations, data processing, formatting text.

def add(a, b):
    return a + b
# Function call
result = add(4, 6)
print("The sum is:", result)  # Note the output and compare it with that of print()
