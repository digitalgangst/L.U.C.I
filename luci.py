#!/usr/bin/env python
# coding: utf-8

import time, sys, pyttsx, os
import speech_recognition as sr
from subprocess import call
from gtts import gTTS


pynotify.init(sys.argv[0]) # Reminder

reload(sys)
call(["clear"])                    
sys.setdefaultencoding('utf8')

# speech config
speech_engine = pyttsx.init()
speech_engine.setProperty('rate', 150) # noise config
recognizer = sr.Recognizer()



def listen():
		with sr.Microphone() as source:
				recognizer.adjust_for_ambient_noise(source)
				audio = recognizer.listen(source)

		try:
				return recognizer.recognize_google(audio)
		except sr.UnknownValueError:
				print("Could not understand audio")
		except sr.RequestError as e:
				print("Recog Error; {0}".format(e))

		return ""


while True:
		time.sleep(1)
		print('[+] Listening...')
		a = listen()
		print a

		# Find location example

		if "where is" in a:
			data = a.split(" ")
			location = data[2]
			
			# Text to speech generator exemple
			beep = call(["mpg321", "start.mp3"])
			tts = gTTS(text="Hold on sir, i will show you where"+location+" is.", lang='en') # The language can be change 
			tts.save('where.mp3') # TTS saves the audio file and play with mpg321
			call(["mpg321", "where.mp3"])
			
			os.system("firefox https://www.google.com/maps/place/{0}/&amp;".format(location))
		# End

