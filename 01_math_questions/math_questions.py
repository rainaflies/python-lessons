score = 0

name = input("Hello, what is your name? ")
print("Hello, " + name + ", I have a math game for you!")

answer1 = input("What is 2 + 2? ")
if answer1 == "4":
	print("✅ Yes! You are correct!")
	score = 1
else: 
	print("🚫 Sorry you are wrong.")

answer2 = input("What is 4 + 5? ")
if answer2 == "9":
	print("✅ Yes! You are correct!")
	score = score + 1
else: 
	print("🚫 Sorry you are wrong.")
	
answer3 = input("What is 2 + 4? ")
if answer3 == "6":
	print("✅ Yes! You are correct!")
	score = score + 1 
else: 
	print("🚫 Sorry you are wrong.")

answer4 = input("What is 7 + 0? ")
if answer4 == "7":
	print("✅ Yes! You are correct!")
	score = score + 1 
else: 
	print("🚫 Sorry you are wrong.")

answer5 = input("What is 6 + 4? ")
if answer5 == "10":
	print("✅ Yes! You are correct!")
	score = score + 1
else: 
	print("🚫 Sorry you are wrong.")

print("Your total score is ")
print(score)

print("Thank you. Come back tomorrow!")