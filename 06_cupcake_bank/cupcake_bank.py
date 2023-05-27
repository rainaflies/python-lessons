balance = 0

def check_password():
	print("Welcome to Cupcake Bank")	

	password = input("Please enter your password: ")
	if password == "9999":
		print("✅ Welcome!")
	else:
		print("⛔️ Wrong password. Goodbye!")
		quit()
	 
def deposit():
	global balance
	
	amount = input("How much do you want to deposit? ")
	balance = balance + int(amount)	
	print(f"✅ OK, you deposited ${amount} into your account.")	
	
def withdraw():	
	global balance
	
	if balance == 0:		
		print("Sorry, you have no money in your account. Please deposit some money.")		
	else:
		withdraw_amount = int(input("How much do you want to withdraw? "))
		
		if withdraw_amount > balance:
			print("Sorry you don't have that much money in your account.")
		else:				
			balance = balance - withdraw_amount
			print(f"✅ OK, you withdrew ${withdraw_amount} from your account.")
	
def check_balance():
	global balance	
	
	if balance == 0:
		print("You have no money. Please go do some work.")
	else:
		print(f"Your balance is ${balance}.")
	
def buy_cupcake():
	global balance
	if balance < 3:		
		print("⛔️ You don't have enough money to buy a cupcake. Please work harder.")
	else:
		balance = balance - 3		
		print("✅ Here's your cupcake for $3: 🧁")		
	
def show_menu():
	print("⎯" * 60)
	print("Main Menu")
	print("1. Deposit")
	print("2. Withdraw")
	print("3. Check Balance")
	print("4. Buy a cupcake ($3)")
	print("5. Goodbye")
	print("⎯" * 60)
	
	choice = input("Please choose an option: ")
	
	if choice == "1":
		deposit()
	elif choice == "2":
		withdraw()
	elif choice == "3":
		check_balance()
	elif choice == "4":
		buy_cupcake()
	else:		
		print("Thank you and come again to Cupcake Bank!")
		quit()
		
check_password()

while True:
	show_menu()