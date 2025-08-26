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


#3. yield
def count_up_to(n):
    i = 1
    while i <= n:
        yield i  # pause and return i
        i += 1

# Using the generator
for number in count_up_to(5):
    print(number)


# more on function arguments(Type of arguments)
#1. Positional Arguments
# These are the most common. The order matters: values are assigned to parameter in the same order as they appear.
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")

# function call
introduce("Ngozi", "AI Engineering")  # Correct order

# Change the arrangement and watch the output
introduce("AI Engineering", "Ngozi")  # Incorrect order, this will throw a semantic error.

#2. Keyword Arguments
# Here, you explicitly mention the parameter name when calling the function. Order doesn't matte, since python knows which value goes where.
def introduce(name, track):
    print("My name is", name)
    print("I am learning", track)

# Function call
introduce(name = "Ngozi", track = "AI Engineering")
# Change the arrangement and watch the output
introduce(track = "AI Engineering", name = "Ngozi")  # Here you notice that order does not matter.

#3. Default arguments 
# Here, you can give parameters a default value. Even if no value is provided when calling, the default is used.
def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print("I am learning", track)

# Function call
# Without specifying the default argument, but watch the output
introduce("paul")
# Specify the default argument, and watch the output
introduce("Tunji Paul", track = "AI Development")

#4. Varying length Argument
# Sometimes we don’t know how many arguments will be passed. Python provides two special symbols(that is the asterisk)
# single asterisk for non-keyword arguments or tuple(*args)
# Double asterisk for keyword arguments or dictionary(**kwargs)

#a. non-keyword(tuple)
# Collects extra positional arguments into a tuple.
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("sum:", total)

# function call
# take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30 ,40, 50)

#b. keyword argument(dictionary)
# Collects extra keyword arguments into a dictionary.
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Function call - Take note of the output
student_details(name = "Peter", track ="AI Engineering", interest = "Block Chain")

# Lets implement on full code

# Define student profile function
# Ensure to not the order of arrangement of the types of arguments used.
# This is how to arrange it of you are using everything or some of the together

def participant_profile(name, age, track = "AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    # Skills (from *args)
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"
    
    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"

    return profile 

# ------- LEts test -------
# Example1: Using only positional arguments
print(participant_profile("Peter", 24))

# Example2: Adding keyword/default argument
print(participant_profile("Ridwan", 29, track = "AI Engineering"))

# Example3: Adding variable-length positional arguments (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))

# Example4: Adding variable-length keyword arguments (*kwargs)
print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interest="Blockchain", city="Shagamu", phone="08123456789"
))