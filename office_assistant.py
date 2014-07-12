"""
office_ass.py

Title: Office Assistant
Author: Tyler Petresky
Date: 7-11-14
Desc: Provides a centralized class for the office assistant.
"""

from sys import exit
from states_list import StatesList
from settings_list import SettingsList

class OfficeAss(object):
	"""
	Central system that runs the Pineapple by configuring
	settings and running all of the sub-systems
	"""
	def __init__(self):
		self.settings_path = "settings/settings.txt"

		self.settings = SettingsList(self.settings_path)
		self.settings.LoadSettings()

		states_path = self.settings.GetSetting("statespath")
		self.states = StatesList(states_path[:-1])
		self.states.LoadStates()

	def Loop(self):
		"""
		Main loop in the system. Runs over and over to check for events
		and run the subsystems.
		"""
		while True:
			for s in self.settings:
				if s.HasChanged():
					print("Need to Update")

if __name__ == "__main__":
	office = OfficeAss()

	#office.Loop()