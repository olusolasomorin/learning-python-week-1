# Ask for:
# Customer's full name
# Units consumed (kWh) - integer
# Cost per unit - float
# Calculate the total bill and print it in a neatly formatted receipt using escape sequences for line breaks.
customer_name = input("Enter your Full name: ")
units_consumed = int(input("Enter units consumed(kWh): "))
cost_per_unit = float(input("Enter cost per units: "))
total_bills = units_consumed * cost_per_unit
print(f"\tELECTRICITY BILL RECEIPT\nCustomer name:\t{customer_name}\nUnits consumed:\t{units_consumed}\nCost per unit:\t${cost_per_unit}\nTotal Bills:\t${total_bills}")