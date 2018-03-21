import ConfigParser
import os
import WoWClass
import re

class Macro(object):
    def __init__(self):
        self.test = 5
        self._target = ''
        self._spell = ''
        self._icon = ''
        self._command = ''

    # property for the target of macro being generated
    @property
    def target(self):
        return self._target

    # setter for target property
    @target.setter
    def target(self, target):
        self._target = target

    @property
    def spell(self):
        return self._spell

    @spell.setter
    def spell(self, spell):
        self._spell = spell

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon):
        self._icon = icon

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, command):
        self._command = command


    #returns True if macro is generated successfully 
    #else, returns false
    def generateMacro(self):
        


	return True

	return False



#class to handle generation functionality such as creation/placement of macros in
#specified locations
class Generator(object):
    def __init__(self):
        self.test = 5

class MacroCLI(object):
    def __init__(self):
        self.test = 5

    # returns True if input is valid syntax from CLI
    # else, returns false
    def checkSyntax(self, args, Macro):

        # list of valid flags allowed in CLI. Allows future additions without hassle
        validFlags = ['target', 'icon', 'spell', 'character']

        for arg in args:
            if arg not validArgument(arg):
                return false
            else:

        return True

        return False

    # returns true if specific argument contains valid flags and input
    # else, returns false
    def validArgument(self, argument):
        validTargets = []
        validIcons = []
        validSpells = 
        return True

        return False


    #returns all flags matching syntax of a valid flag from the command line input
    #ignores semantics/validity of flags and only focuses on syntax matching
    def determineFlags(self, cli_input):

        #regular expression to parse out all flags assuming flag starts with '--' and ends with '='
        flags = re.search('--(.*)=', cli_input)

        return flags


if __name__ == "__main__":
    from sys import argv

    myargs = getopts(argv)

    macro = Macro()
    macroCLI = MacroCLI()
