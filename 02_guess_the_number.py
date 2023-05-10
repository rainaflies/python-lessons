from random import randrange

print("Welcome! Guess the number between 1-10.")
random_num = randrange(0, 10)

if random_num < 5:
	print("Hint: The number is less then 5.")
else:
	print("Hint: The number is 5 or greater.")
	
print("⎯"*79)

while True:		
	guess_num = input("Can you guess the number: ")

	if int(guess_num) == random_num:
		print("You are right.")
		break
	else:
		print("Sorry, please try again.")

	print("⎯"*79)