# Task1
#1. Write a program to take a string input from the user and display it in uppercase.
name = input("Enter your name: ")
print(name.upper())

#2. Given the string "python", print its first and last characters.
word = "python"
print(word[0])
print(word[-1])

#3. Ask the user for their name and print "Hello !" where is the user's input.
user_name = input("Enter your name: ")
print(f"Hello {user_name}!")

#4. Write a program to count the number of characters in a string without using len()
string = "Hello world"
print(string.rindex(string[-1]) + 1)

#5. Given "Hello World", replace "World" with "Python"
message = "Hello World"
print(message.replace("World", "Python"))

# Task2
#6. Check if a given string contains the substring "python" (case-insensitive).
string = "Am i coding python"
print("python" in string)

#7. write a program to reverse a string without using slicing ([::-1]).
string = 'olusola'
print(''.join(reversed(string)))

#8. Given a string with extra spaces, remove the leading and trailing spaces.
string = ' olusola '
print(string.strip())

#9. Ask the user to enter a sentence and print the number of vowels in it.
sentence = input("Enter a sentence: ")
print(sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u"))

#10. Convert a string "1234" to an integer and multiply it by 2.
string = '1234'
print(int(string) * 2)

# Task3: Pattern Matching & Splitting
#11. Given "apple,banana,orange", split into a list of fruits.
fruit = "apple,banana,orange"
print(f"List of fruits\n{fruit.split(",",)}")

#12. Ask the user for a sentence and print each word on a new line.
sentence = input("Enter a sentence: ")
print("\n".join(sentence.split()))

#13. Replace all spaces in a string with underscores(_).
string = 'Olusola Edward'
print(string.replace(' ', '_'))

#14. count how many times the letter "a" appears in "Banana".
letter = 'Banana'
print(letter.count('a'))

#15. check if a given string starts with "https://".
website = 'www.python.com'
print(website.startswith('https://'))