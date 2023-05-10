while True:	
	print("Welcome to the job tool store.")
	print("⎯"*79)
	print("1. Firefighter 🚒")
	print("2. Apple engineer 💻")
	print("3. PG&E manager 💻")
	print("4. Librarian 👩🏾‍🏫")
	print("5. Doctor 🏩")
	
	job = int(input("What is your job? "))
	
	if job == 1:
		print("🚒 👩🏼‍🚒 🪓")
		
	elif job == 2: 
		print("💻 ⎯ ⌨️")
		
	elif job == 3:
		print("💻 🚚 ☎️")
		
	elif job == 4:
		print("📚 📅 ✐")
		
	elif job == 5:
		print("🩻 🩹 🩺")
		
	else:
		show_image("Thief")
	
	print("⎯"*79)
	