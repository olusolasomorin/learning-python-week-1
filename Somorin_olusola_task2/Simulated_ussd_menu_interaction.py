# You are to design a mock USSD interface for a mobile service.
# Requirements:
#    1. When the user runs the program, display a welcome screen with a Nigerian context greeting.
#    2. Ask the user to "dial" a USSD code (e.g., *123#) and store it in a variable.
#    3. Print a menu with at least 3 options (e.g., "Check Balance", "Buy Airtime", "Buy Data") using newline escape sequences `(\n)` for formatting.
#    4. Ask the user to choose an option (1, 2, or 3) and store their choice in a variable.
#    5. Use f-strings and/or concatenation to display a confirmation message showing the selected option.
#    6. Ask for an amount (if applicable) and store it as a number using type casting.
#    7. Display a final message summarizing the transaction.
print("\tWelcome to MTN, your number one service provider.\n\tDial *312# to view our service option")
ussd = input("")
print("1.\tCheck Balance\n2.\tBuy Airtime\n3.\tBuy Data")
option = input("Choose an option (1, 2, or 3 ): ")
print(f"You selected an option {option}.")
option == ("1:")
print("Your account balance is #1,500.00.\nThank you for using MTN.")
option == ("2:")
amount = float(input("Enter airtime amount to purchase (#): "))
print(f"You have successfully purchased {amount:.2f}airtime. Thank you!")
option == ("3:")
amount = float(input("Enter data amount MB: "))
print(f"You have successfully purchased {amount}MB of data. Keep browsing!")