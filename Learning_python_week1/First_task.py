# step1 welcome message and request for customer name
# step2 welcome message with the customers name 
# step 3 take customer order
# step 4 Reply customer to be patient with their order
# step 5 Notify customers about their order

# name = input("Enter your full name: ")
# print("welcome,", name)
# university = input("Enter the name of your univeristy of study: ")
# course = input("Course of study: ")
# nationality = input("Natinality: ")
# print(f"Great\nConfirm your details: \n{name}\n{university}\n{course}\n{nationality}.")
# confirm = input("Are your informations correct?: ")
# print("Thank you\nThat's all for now")

# Recharge 500 naira airtime and buy data
# step 1 load your recharge card
# step 2 use ussd code to buy data
# step 3 choose your data plan
# step 4 buy your data
welcome = input(" welcome to Spie Bank\nWhat would you like to do today?\n\t1.\tSend money\n\t2.\tBuy Airtime\n\t3.\tBuy a Data plan\n")
account_number = input("\tEnter account number:\n")
print("\tChoose bank:\n\t1.\topay\n\t2.\tPalmpay"),
bank = input("")
verify_name = input("\tEnter account name:\n")
amount = input("\tEnter amount:\n")
print(f"\tyour have successfully sent {amount} to {verify_name}. ")
