import re
import os
from user import *

class PhoneBook:

	def __init__(self, *args, **kwargs):
		self.users = list()
		return super().__init__(*args, **kwargs)

	def addUser(self, name, number = None, alias = None):
		"""Adds a new user to the phonebook and returns the User object."""
		test = self.findUsers(name, number)
		if test[0]: return test[1]

		new = User(name, number, alias)
		self.users.append(new)
		return new

	def removeUser(self, name, number = None):
		"""Removes users matching specified name (+ alias) and numbers."""
		l = len(self.users)
		self.users = [user for user in self.users if user not in self.findUsers(name, number)]
		return l != len(self.users)

	def findUsers(self, name, number = None):
		"""Finds users matching specified name (+ alias) and numbers."""
		matches = [user for user in self.users if user.namesToString().lower().find(name.lower()) > -1]
		if number != None:
			matches = [user for user in matches if user.numbersToString().find(number) > -1]

			return len(matches) > 0, matches

	def printAll(self):
		"""Prints the contents of the phonebook in a formatted manner."""
		print(len(self.users), "user(s):")
		for user in self.users:
			print("{0}, {1} {2}".format(user.lastName.upper(), user.firstName, user.middleName))
			if len(user.names) > 1:
				print("AKA:", ", ".join(user.names[1:]))
			for num in user.numbers:
				print("\t# {0}".format(num))
			print()

	def save(self, path):
		with open(path, "w") as wf:
			for user in self.users:
				wf.write("{0};{1}\n".format("/".join(user.names), "/".join(user.numbers)))
			return True
		return False

	def load(self, path):
		if (os.path.isfile(path)):
			with open(path, "r") as rf:
				for line in rf.readlines():
					names = re.search("([\w\s]+)[/;]", line)
					print(names[0])
				return True
		return False