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
	
def show_planet(planet):
	show_planet_info(planet)
	show_planet_picture(planet)

def main():
	show_menu()	
	
	planet = int(input("Which planet do you want to learn about? "))
	
	if planet == 1:
		show_planet("Mercury")
	elif planet == 2:
		show_planet("Venus")
	elif planet == 3:
		show_planet("Earth")
	elif planet == 4:
		show_planet("Mars")
	elif planet == 5:
		show_planet("Jupiter")
	elif planet == 6:
		show_planet("Saturn")
	elif planet == 7:
		show_planet("Uranus")
	elif planet == 8:	
		show_planet("Neptune")
	elif planet == 9:
		show_planet("Pluto")
	else:
		print("Unknown planet!")

if __name__ == "__main__":
	main()
