for age in range(1, 101):
	if age == 1:
		print("Raina is 1 year old.")
	else:				
		print(f"Raina is {age} years old.")
		
	if age > 12 and age < 20:
		print("She's a teenager.")		
		
	if age > 20 and age < 60:
		print("She's an adult.")
		
	if age > 60 and age < 100:
		print("She's retired!")
		
	if age == 100:
		print("R.I.P")
		
	print("-" * 20)
