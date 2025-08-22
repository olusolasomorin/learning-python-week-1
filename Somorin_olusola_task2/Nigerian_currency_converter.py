# Ask for: 
# Amount in Naira (float)
# Exchange rate to us Dollars (float)
# Exchange rate to british pounds (float)
# Convert and print results with thousands separators and currency symbols, neatly aligned in a table-like format using escape sequences.
amount_naira = float(input("Enter amount in naira (₦): "))
rate_usd = float(input("Enter exchange rate to US Dollar ($): "))
rate_GBP = float(input("Enter exchange rate to Pounds (£): "))
amount_usd = amount_naira / rate_usd
amount_GBP = amount_naira / rate_GBP
print("\tCurrency Conversion Table\nCurrency\tAmount")
print(f"Naira (₦)\t₦{amount_naira:,.2f}")
print(f"US Dollar ($)\t${amount_usd:,.2f}")
print(f"Pounds (£)\t£{amount_GBP:,.2f}")