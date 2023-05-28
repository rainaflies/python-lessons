from openai_planets import *

def show_menu():
	print("Please pick a planet:")
	print("1. Mercury")
	print("2. Venus")
	print("3. 🌎")
	print("4. Mars")
	print("5. Jupiter")
	print("6. Saturn")
	print("7. Uranus")
	print("8. Neptune")
	print("9. Pluto")
	print("⎯"* 50)

def main():
	show_menu()	
	
	planet = int(input("Which planet do you want to learn about? "))
	
	if planet == 1:
		show_planet_info("Mercury")
		show_planet_picture("Mercury")
	elif planet == 2:
		show_planet_info("Venus")
		show_planet_picture("Venus")
	elif planet == 3:	
		show_planet_info("Earth")
		show_planet_picture("Earth")
	elif planet == 4:	
		show_planet_info("Mars")
		show_planet_picture("Mars")
	elif planet == 5:	
		show_planet_info("Jupiter")
		show_planet_picture("Jupiter")
	elif planet == 6:	
		show_planet_info("Saturn")
		show_planet_picture("Saturn")		
	elif planet == 7:	
		show_planet_info("Uranus")
		show_planet_picture("Uranus")		
	elif planet == 8:	
		show_planet_info("Neptune")
		show_planet_picture("Neptune")
	elif planet == 9:	
		show_planet_info("Pluto")
		show_planet_picture("Pluto")
	else:
		print("Unknown planet!")

if __name__ == "__main__":
	main()
