"""
settings_list.py

Title: Settings List
Author: Tyler Petresky
Date: 7-11-14
Desc: Declares a class to hold all of the settings
available to the system.
"""

class SettingsList(object):
	"""
	Class to store all of the settings. All settings
	are stored in a dictionary.
	"""
	def __init__(self, _settings_file_path):
		self.settings = {}
		self.settings_file_path = _settings_file_path

	def AddSetting(self, _identifier, _value):
		"""
		Adds a setting to the dictionary.
		"""
		self.settings[_identifier] = _value

	def RemSetting(self, _identifier):
		"""
		Removes a setting from the dictionary.
		Returns None if element doesn't exist.
		"""
		if self.settings.has_key(_identifier):
			del self.settings[_identifier]
		else:
			return None

	def GetSetting(self, _identifier):
		"""
		Returns the value of a setting.
		Returns None if element doesn't exist.
		"""
		if _identifier in self.settings:
			return self.settings[_identifier]
		else:
			return None

	def LoadSettings(self):
		"""
		Loads the settings of the system from the
		settings file.
		Returns True if successful, else false.
		"""
		settings_file = open(self.settings_file_path, 'r')
		print("Settings:")
		for line in settings_file:
			if line[0] == '#':
				continue

			colon_index = line.find(':')
			if colon_index != -1:
				identifier = str(line[:colon_index])
				value = line[colon_index + 1:]

				print("ID: " + identifier)
				print("Value: " + value)

				self.AddSetting(identifier, value)

		settings_file.close()

		return True

	def WriteSettings(self):
		"""
		Writes the settings to the settings file.
		Returns True if successful, else False.
		"""
		states_file = open(self.settings_file_path, 'w')

		string = ""
		for key in self.settings.keys():
			string += key + ':' + self.settings[key] + '\n'

		settings_file.write(string)

		settings_file.close()

		return True