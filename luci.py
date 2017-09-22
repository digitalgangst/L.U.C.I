#!/usr/bin/env python
# coding: utf-8

import time, sys, pyttsx, os
import speech_recognition as luci
from subprocess import call
from gtts import gTTS
from time import gmtime, strftime

reload(sys)
call(["clear"])                    
sys.setdefaultencoding('utf8')

# speech config
speech_engine = pyttsx.init()
speech_engine.setProperty('rate', 150) # noise config
recognizer = luci.Recognizer()



def listen():
		with luci.Microphone() as source:
				recognizer.adjust_for_ambient_noise(source)
				audio = recognizer.listen(source)

		try:
				return recognizer.recognize_google(audio)
		except luci.UnknownValueError:
				print("Could not understand audio")
		except luci.RequestError as e:
				print("Recog Error; {0}".format(e))

		return ""


while True:
		
		time.sleep(1)
		print('[+] Listening...')
		a = listen()
		print(a)
		call(["clear"])
		print("""


 __         __  __     ______     __    
/\ \       /\ \/\ \   /\  ___\   /\ \   
\ \ \____  \ \ \_\ \  \ \ \____  \ \ \  
 \ \_____\  \ \_____\  \ \_____\  \ \_\ 
  \/_____/   \/_____/   \/_____/   \/_/ 
                                        



""")

		# Find location example
		if "lucy" in a or "Lucy" in a:
			beep = call(["mpg321", "start.mp3"])
			call(["clear"])

			if "open" in a:
				if "Terminal" in a or "Console" in a:

					tts = gTTS(text="Ok sir, i will open the terminal.", lang='en')
					tts.save("terminal.mp3")
					call(["mpg321", "terminal.mp3"])
					call(["clear"])
					call(["mate-terminal"])

			elif "check my calendar" in a:
				
				tts = gTTS(text="Hold on, sir. Checking your calendar.", lang ='en')
				tts.save("checkcalendar.mp3")
				call(["mpg321", "checkcalendar.mp3", "&>/dev/null"])
				call(["clear"])


				run_reminder = os.system("python reminder.py > events.csv")

				beep = call(["mpg321", "start.mp3", "&>/dev/null"])
				call(["clear"])

				event_log = open("events.csv", "r")
				y = event_log.read()
				print(y)

				if "No upcoming events found." in event_log:

					tts = gTTS(text="Sir, You dont have any upcoming event.")
					tts.save("noevents.mp3")
					call(["mpg321", "noevents.mp3", "&>/dev/null"])
					call(["clear"])
				else:
					tts = gTTS(text="Sir, you next event is: {0}. I will show you.".format(y))
					tts.save("nextevent.mp3")
					call(["mpg321", "nextevent.mp3", "&>/dev/null"])
					call(["clear"])
					os.system("gedit events.csv")

			elif "what time is it" in a:
				current_time = strftime("%H:%M:%S", gmtime())
				
				tts = gTTS(text="Its {0}".format(current_time))
				tts.save("currenttime.mp3")
				call(["mpg321", "currenttime.mp3"])
				call(["clear"])

			elif "close" in a:
				data = a.split(" ")
				process = data[2]

				tts = gTTS(text="Ok.", lang='en')
				tts.save('ok.mp3')
				call(["mpg321", "ok.mp3"])
				os.system("killall "+process)
				call(["clear"])

			elif "where is" in a:
				
				data = a.split(" ")
				location = data[3]
			
				# Text to speech generator exemple
				tts = gTTS(text="Hold on sir, i will show you where"+location+" is.", lang='en') # The language can be change 
				tts.save('where.mp3') # TTS saves the audio file and play with mpg321
				call(["mpg321", "where.mp3", "&>/dev/null"])
				call(["clear"])
				
				os.system("firefox https://www.google.com/maps/place/{0}/&amp;".format(location))
		# End

