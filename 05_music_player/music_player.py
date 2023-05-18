from playsound import playsound

def play_sound(filename):
	playsound("./sounds/" + filename + ".mp3")

def show_menu():
	print("1. 🎻")
	print("2. 🎸")
	print("3. 🥁")
	print("4. 🎷")
	print("5. 🎹")

def play_volin():
	print("🎻"*50)
	play_sound("Violin")
	
def play_guitar():
	print("🎸"*50)
	play_sound("Guitar")
	
def play_drum():
	print("🥁"*50)
	play_sound("Drum")
	
def play_sax():
	print("🎷"*50)
	play_sound("Sax")
	
def play_piano():
	print("🎹"*50)
	play_sound("Piano")
	
while True:	
	show_menu()
	choice = int(input("What do you you want to listen to? "))
	
	if choice == 1:
		play_volin()
	elif choice == 2:
		play_guitar()
	elif choice == 3:	
		play_drum()
	elif choice == 4:	
		play_sax()
	elif choice == 5:
		play_piano()
	else:
		speak("That's not an option!")