import os
import ConfigParser

class Race(object):
	def __init__(self, race):
		self.race = race

		self.Config = ConfigParser()
		self.Config.read(os.getcwd() + '/../Classes/Racials.ini')

	@property
	def race(self):
		return self._race

	@race.setter
	def race(self, race):
		self._race = race


	@property
	def racial(self):
		racial = self.Config.get(self._race , 'racial')
		return racial

class Class(Race):
	def __init__(self, wClass, race):
		Race.__init__(self, race)

		self.Config = ConfigParser()
		self.Config.read(os.getcwd() + '/../Classes/' + wClass + '.ini')

		self.type = wClass

		@property
		def type(self):
			return self._type

		@type.setter
		def type(self, type):
			self._type = type


class Spec(Class):
	def __init__(self):
		self.test = 5
		self._spells = []
		self._

	@property
	def spells(self):
		
