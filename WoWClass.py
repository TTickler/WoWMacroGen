import os
import ConfigParser


class Class(object):
	def __init__(self):
		self.Config = ConfigParser()
		self.Config.read(os.getcwd() + "")



class Race(Class):
	def __init__(self):
		self.test = 5


	@property
	def racial(self):
		return self._racial

	@racial.setter
	def racial(self, racial):
		self._racial = 

class Spec(Class):
	def __init__(self):
		self.test = 5
		self._spells = []
		self._

	@property
	def spells(self):
		
