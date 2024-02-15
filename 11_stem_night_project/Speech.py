#!/usr/bin/env python3

from playsound import playsound
from gtts import gTTS
import os

def speak(text):	
	return
	tts = gTTS(text)
	tts.save("Speech.mp3")
	playsound("Speech.mp3")
	os.remove("Speech.mp3")
