# Ask user to input:
# Market name
# Number of traders
# Daily revenue in naira
# Display the result using f-string formatting with commas for thousands seperator.
market_name = input("Market name: ")
no_of_traders = input("Number of Traders: ")
revenue = float(input("Daily revenue: "))
print(f"Your details are: ", market_name, no_of_traders, revenue)