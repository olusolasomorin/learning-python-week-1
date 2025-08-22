# Ask for:
# Distance in km (float)
# Fare per km (float)
# Calculate and display the total fare with two decimal places using f"{value:.2f}"
distance = float(input("Distance in km: "))
fare = float(input("Fare per km: "))
result = distance * fare
print(f"Total fare: ${result:.2f}")