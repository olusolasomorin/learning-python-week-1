# Handling Errors in python
# Errors in python are classified into three main categories:
#1. Syntax errors 
#2. Runtime errors
#3. Semantic errors

#1. SYNTAX ERRORS
#a. Indentation error - Incorrect spacing
# for i in range(3):
# print(i)  # Wrong indentation

#b. Missing colon/parenthesis error
# if 5 > 3 # Missing colon
#     print('Hello')

#c. Invalid syntax - General grammar mistakes.
# print 'Hello'     # Missing parentheses in python 3

#2. RUNTIME ERRORS
#a. Zero Division Error - Dividing Errors
# x = 10 / 0 

#b. NameError - Using a variable before defining it.
# print(age)  # age not defined

#c. TypeError - Wrong data type in an operation.
# result = "10" + 5   # str + int not allowed 

#d. ValueError - Invalid value for a function.
# number = int("abc")   # cannot convert string to int

#e. IndexError - Accessing list index out of range.
# fruits = ['apple', 'banana']
# print(fruits[3])    # Index out of range

#f. KeyError - Accessing a dictionary with a missing key.
# data = {"name": "Ada"}
# print(data["age"])   # key not found

#g. FileNotFoundError - File does not exist.
# f = open("mising.txt")  # File not found

# Handling Runtime Errors
#1. The try Block
# It is used to wrap code that might raise an error
# If no error occurs python skips the except block.
# try:
#     x = 10 / 2
#     print("Result:", x)

#2. The except Block
# It defines what to do if an error occurs inside try.
# It can catch specific errors or all errors.
# This is a specific exception
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

# This is a case of multiple exception
try:
    number = int("abc")
    result = 10 / 0
except ValueError:
    print("Invalid conversion to integer.")
except ZeroDivisionError:
    print(" Cannot divide by zero.")

#3. The finally block
# Always runs, whether an error occurred or not.
# Useful for cleanup tasks (e.g., closing files, releasing resources).
try:
    f = open("sample.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file if it was opened.")

balance = 5000 # starting balance
print("Welcome to the ATM")
amount = input("Enter amount to withdraw: ")

try:
    amount = float(amount)   # Convert input to number

    if amount > balance:
        raise ValueError("Insufficient funds.")
    
    balance -= amount
    print("Withdrawal successful. New balance: ₦", balance)

except ValueError as e:
    print("Error:", e)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Transaction session closed.")

#3. Semantic Errors
# Wrong condition in logic
age = 18
if age > 18:     # Should be >=
    print("Eligible to vote")
else:
    print("Not eligible")

# Wrong Formula/Computation
length = 10
width = 5
area = length + width  # should be multiplication
print("Area:", area)

# Wrong variable usage
marks = [70, 80, 90]
total = marks[0] * marks[1] * marks[2]  # wrong, should be sum
print("Total:", total)

# To fix semantic errors carefully review logic, test with multiple cases, use debugging or print statements.