from scamp import *

s = Session(tempo=120)

harmony_inst = input("What should the harmony instrument be? ")
melody_inst = input("What should the melody instrument be? ")

harmony = s.new_part(harmony_inst)
melody = s.new_part(melody_inst)

for n in range(3):
	harmony.play_chord([57, 61, 64], 1, 2, blocking=False)
	melody.play_note(57, 1, 2)
	
	harmony.play_chord([57, 61, 64], 1, 2, blocking=False)
	melody.play_note(59, 1, 2)
	
	harmony.play_chord([57, 61, 64], 1, 2, blocking=False)
	melody.play_note(61, 1, 2)
	
	harmony.play_chord([57, 61, 64], 1, 2, blocking=False)
	melody.play_note(62, 1, 2)
	
	harmony.play_chord([57, 61, 64], 1, 2, blocking=False)
	melody.play_note(64, 1, 2)
	
	harmony.play_chord([57, 61, 64], 1, 2, blocking=False)
	melody.play_note(66, 1, 2)
	
	harmony.play_chord([57, 61, 64], 1, 2, blocking=False)
	melody.play_note(68, 1, 2)
	
	harmony.play_chord([57, 61, 64], 1, 2, blocking=False)
	melody.play_note(69, 1, 2)
