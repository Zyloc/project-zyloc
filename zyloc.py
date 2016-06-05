from os import sys, path
from subprocess import call

import pyttsx


"""
class Engine(object):
	def speak(self,*args,**kwargs):
		self.speaker.say()
		self.speaker.runAndWait()

	def __init__(self):
		self.speaker = pyttsx.init()
		
	def __del__(self):
		self.speaker.stop()
		self.speaker.setProperty('rate',150)	
"""
def speak(*args,**kwargs):
	speaker = pyttsx.init()
	speaker.setProperty('rate',150)
	speaker.say(inp)
	speaker.runAndWait()

if __name__ == '__main__' and __package__ is None:
	sys.path.append(path.abspath(__file__))
	while 1:
		inp = raw_input()
		if 'stop' in inp:
			break
		else:
			#pass
			speak(inp)



		