# Ask for:
# School name
# Tution fee (float)
# Hostel fee (float)
# Feeding fee (float)
# Calculate the total and print it in receipt format with each fee on a new line.
school_name = input("Enter the name of your school: ")
tution_fee = float(input("Tution fee: "))
hostel_fee = float(input("Hostel fee: "))
feeding_fee = float(input("Feeding fee: "))
total = tution_fee + hostel_fee + feeding_fee
print(f"\t{school_name}\n\tReceipt\nTution:\t\t${tution_fee}\nHostel:\t\t${hostel_fee}\nfeeding:\t${feeding_fee}\nTotal:\t\t${total}")