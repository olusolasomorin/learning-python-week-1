# Ask the user for:
# Your age (integer)
# Your height in meters (float)
# Your name (string)
# Print a sentence using f-string showing all details in one line, making sure you type-cast where necessary.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height(m): "))
print(f"\tUser Details\nFull name:\t{name}\nAge:\t{age} years\nHeight:\t{height} m")