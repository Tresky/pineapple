"""
states_list.py

Title: States List
Author: Tyler Petresky
Date: 7-11-14
Desc: Declares a class to hold all of the states
available to the system.
"""

from sys import exit

class StatesList(object):
	"""
	Class to store all of the states of the currently
	registered programs.
	"""
	def __init__(self, _states_file_path):
		self.states = {}
		self.states_file_path = _states_file_path
		self.needs_to_write = False

	def AddState(self, _identifier, _value):
		"""
		Adds a new states to the system.
		Used, also, to edit current state.
		"""
		self.states[_identifier] = _value
		self.need_to_write = True

	def RemState(self, _identifier):
		"""
		Removes a state from the system.
		Returns None if element doesn't exist.
		"""
		if self.states.has_key(_identifier):
			del self.states[_identifier]
			need_to_write = True
		else:
			return None

	def GetState(self, _identifier):
		"""
		Returns the value of an element if it exists.
		If the element doesn't exist, returns False.
		"""
		if _identifier in self.states:
			return self.state[_identifier]
		else:
			return None

	def NeedToWrite(self):
		"""
		Returns the state of the state machine.
		True if the states file needs to be updated,
		else False.
		"""
		return need_to_write

	def LoadStates(self):
		"""
		Loads the latest states from the states file.
		Returns True if successful, else False.
		"""
		states_file = open(self.states_file_path, 'r')
		print("States:")
		for line in states_file:
			if line[0] == '#':
				continue

			colon_index = line.find(':')
			if colon_index != -1:
				identifier = str(line[:colon_index])
				value = line[colon_index + 1:]

				print("ID: " + identifier)
				print("Value: " + value)

				self.AddState(identifier, value)

		states_file.close()

		return True

	def WriteStates(self):
		states_file = open(self.states_file_path, 'w')

		string = ""
		for key in self.states.keys():
			string += key + ':' + self.states[key] + '\n'

		states_file.write(string)

		states_file.close()

		need_to_write = False

		return True