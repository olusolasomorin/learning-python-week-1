# Single quotes
name = 'Ada'
print(name)

# Double quotes
greeting = "Hello"
print(greeting)

# Triple quotes (for multi-line strings)
story = '''Once upon a time,
there was a coder named Ada.'''
print(story)

# String with numbers and symbols
password = "p@ssword123" 
print(password)

# string operation
# Indexing
word = "Python"
print(word[0]) # P
print(word[-1]) # n

# Slicing
word = "Python"
print(word[0:4])   # Pyth
print(word[2:])    # thon
print(word[:3])    # Pyt
print(word[::2])   # Pto
print(word[::-1])
print(word[::1])

# String Concatenation & Repetiton
# Concatenation
a = "Hello"
b = "World"
print(a + " " + b)

# Repetition
word = "Hi!"
print (word * 3)

# String Searching & Checking 
# Membership
text = "Python programming"
print("Python" in text)
print("Java" not in text)
print("Java" in text)

# find() / rfind()
text = "Hello World"
print(text.find("o"))
print(text.rfind("o"))
print(text.rfind("l"))

# index() / rindex()
# (Like find () but raises an error if not found)
text = "Hello World"
print(text.index("World"))

# startswith() / endswith()
filename = "data.cvs"
print(filename.startswith("data"))
print(filename.endswith(".cvs"))

# Upper()
# Converts all characters in the string to uppercase.
name = "Ada Balogun"
print(name.upper())

# Lower()
# Converts all characters in the string to lowercase.
sentence = "PYTHON IS AMAZING"
print(sentence.lower())
sentence = "PYTHON IS AMAZING"
print(sentence.title())

# strip()
# Removes whitespace (or specified characters) from both ends of the string.
text = " Abuja "
print(text.strip())

# replace()
# Replaces occurences of a substring with another substring.
message = "I love Java"
print(message.replace("Java", "Python"))

# swapcase()
# switches lowercase to uppercase and vice versa
text = "Hello ABEOKUTA"
print(text.swapcase())
text = "hello ABEOKUTA"
print(text.swapcase())

# lstrip()
# Removes whitespace (or specified characters) from the left side only.
text = " Nigeria"
print(text.lstrip())

# rstrip()
# Removes whitespace (or specified characters) from the right side only.
text = "Nigeria "
print(text.rstrip())

# split()
# Splits a string into a list using a separator (defult is space).
fruits = "mango orange banana"
print(fruits.split())

# rsplit()
# Splits a string into a list from the right side.
text = "one,two,there,four"
print(text.rsplit(",", 2))

# splitlines()
# Splits a string into a list at each newline (\n).
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())

# join()
# Joins a list of strings into one string with a specified separator.
words = ["I", "love", "Python"]
print(" ".join(words))

# center()
# Centers the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.center(20, "-"))

# ljust()
# Left-aligns the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.ljust(10, "*"))

# rjust
# Right-aligns the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.rjust(10, "*"))

# zfill()
# Pads a numeric string on the left with zeros until it reaches a given length.
num = "42"
print(num.zfill(5))

# isalpha()
# Checks if the string contains only letters.
print("Lagos".isalpha())
print("Lagos123".isalpha())

# isdigit()
# Checks if the string contains only digits.
print("12345".isdigit())
print("123a".isdigit())

# isalnum()
# Checks if the string contains only letters and digits.
print("Python3".isalnum())
print("Python 3".isalnum())
