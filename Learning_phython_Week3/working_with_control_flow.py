# Control Flow in python
#A. Conditional statements
#1. if statement
# Executes a block only when a condition is true.
age = 20
if age >= 18:
    print("You are eligble to vote") # You are eligible to vote

#2. if-else statement
# Provides two alternative paths.
wallet = 400
price = 500

if wallet >= price:
    print("Purchase successful")
else:
    print('Insufficient balance')

#3. if-elif-else statement
# Used for multiple conditions.
score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")

#4. Nested if 
# Placing an if inside another if.
age = 19
citizen = True
if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")

#B. Loops
#1. for loop
# This is used for iterating over a sequence (strings, list, tuple, dictionary)

# Iterates through each element ina LIST.
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterates through each element in a TUPLE. This works like lists, but remember that tuples are immutable.
coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")

# Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.
student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

# Iterates through each element in a STRING. Remember that strings are sequences of characters.
word = "PYTHON"
for char in word:
    print(char)

#2. While loop
# A while loop is used to repeatedly execute a block of code as long as a given condition is true. unlike the for loop (which iterates over sequences like lists, tuples, etc.), the while loop is condition-based.
# The condition must evaluate to True for the loop to continue running.
# When the condition becomes False, the loop stops.
# Using while loop
## Documenting my thoughts ##
# Let the loop start with count = 1
# Let it keep printing until count is greater than 5
# Let the loop terminate when the condition is no longer true

## My code
count = 1
while count <= 5:
    print("Number:", count)
    count += 1

# Incrementing with 'while'
num =1
while num <= 10:
    print(num, end=" ")
    num += 1

# Decrementing with 'while'
timer = 10
while timer > 0:
    print("Countdown:", timer)
    timer -= 1

# While with user Input
## Keep asking until the user enters a correct password.
password = ""
while password != "python123":
    password = input("Enter the password: ")

print ("Access Granted!")

# Understanding while True
# The while True: loop is an infinite loop — it keeps running forever until you explicitly stop it with a break statement or by exiting the program.
# It is commonly used when:
# You don’t know in advance how many times you want the loop to run.
# You want to keep asking the user for input until a valid condition is met.
# You are building continuous programs like menus, login systems, or simulations.

# Keep asking the user for a name until they type "exit".
while True:
    name = input("Enter your name (type 'exit' to quit): ")
    if name.lower() == "exit":
        print("Goodbye!")
        break
    print(f"Hello, {name}")

# Loop Control Statements (`break`, `continue` and `pass`)
# These keywords help us control the behavior of loops (for and while). Instead of loops always running all iterations, we can skip steps, stop early, or do nothing intentionally.
#1. Break
# Stops loop immediately. It is used if a condition is met and there's no need to continue looping.
for num in range(1, 10):
    if num == 5:
        break
    print(num)

#The loop stops completely when num == 5.
# Stop searching when an item is found.
# Exit when user input matches a condition.
# Prevent unnecessary iterations.

#2. Continue
# Skips the current iteration and moves to the next one. It is used if you want to ignore some values but keep the loop running.
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

#3. Pass 
# Does nothing. A placeholder to avoid errors. It is used if you haven't written the code yet but want to keep the structure.
for num in range(1, 6):
    if num == 3:
        pass
    else:
        print(num)

# Lest try while True again
# Try and think through this 
while True:
    print('\nMenu:')
    print("1. Say Hello")
    print("2. Goodbye")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("Goodbye")
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")

# Try and use while True for validation

while True:
    age = input("Enter your age: ")
    if age.isdigit():
        print(f"Your age is {age}")
        break
    else:
        print("Invalid input. Please enter a number.")

# Lets make a guess

secret = "python"

while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong! Try again.")

# Do you remember this?

balance = 1000

while True:
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance is: {balance}")
    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")