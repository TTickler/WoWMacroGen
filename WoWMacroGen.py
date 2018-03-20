import ConfigParser
import os



class Macro(object):
	def __init__(self):
		self.test = 5
		self._target = ''
		self._spell = ''
		self._icon = ''

	
	#property for the target of macro being generated	
	@property
	def target(self):
		return self._target

	#setter for target property
	@target.setter
	def target(self, target):
		self._target = target

	@property 
	def spell(self):
		return self._spell

	@spell.setter
	def spell(self, spell):
		self._spell = spell

	@propery
	def icon(self):
		return self._icon

	@icon.setter
	def icon(self, icon):
		self._icon = icon


class MacroCLI(object):
	def __init__(self):
		self.test = 5




if __name__ == "__main__":
	macro = Macro()
	macroCLI = MacroCLI()
	
	while True:
		



