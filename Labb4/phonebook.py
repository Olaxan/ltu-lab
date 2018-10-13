import re
import os
import utils
from user import *

class PhoneBook:

	def __init__(self, *args, **kwargs):
		self.users = list()
		return super().__init__(*args, **kwargs)

	def addUser(self, name, number = None):
		"""Adds a new user to the phonebook and returns the User object."""
		if number is not None:
			test = self.findUsers(name, number)
			if test[0]: return (not test[0], test[1])

		new = User(len(self.users), name, number)
		self.users.append(new)
		return True, new

	def removeUser(self, name, number = None):
		"""Removes users matching specified name (+ alias) and numbers."""
		l = len(self.users)
		self.users = [user for user in self.users if user not in self.findUsers(name, number)]
		return l != len(self.users)

	def findUsers(self, name, number = None):
		"""Finds users matching specified name (+ alias) and numbers."""
		name = utils.toCleanList(name)
		number = utils.toCleanList(number)
		matches = list()

		for i in name:
			matches = [user for user in self.users if user.namesToString().lower().find(i.lower()) > -1]
			for j in number:
				matches = [user for user in matches if user.numbersToString().find(j) > -1]

		return len(matches) > 0, matches

	def getUserFromID(self, id):
		if len(self.users) >= id:
			return self.users[id]
		else:
			return None

	def printUser(self, user):
		print("#{0}: {1}, {2} {3}".format(user.id, user.lastName.upper(), user.firstName, user.middleName))
		if len(user.names) > 1:
			print("AKA:", ", ".join(user.names[1:]))
		for num in user.numbers:
			print("   - {0}".format(num))
		print()

	def printAll(self):
		"""Prints the contents of the phonebook in a formatted manner."""
		print(len(self.users), "user(s):")
		for user in self.users:
			print("#{0}: {1}, {2} {3}".format(user.id, user.lastName.upper(), user.firstName, user.middleName))
			if len(user.names) > 1:
				print("AKA:", ", ".join(user.names[1:]))
			for num in user.numbers:
				print("   - {0}".format(num))
			print()

	def clear(self):
		self.users.clear()

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
					names = re.search("^(.*?);", line).group(1).split("/")
					numbers = re.search(";(.+)$", line).group(1).split("/")
					self.addUser(names, numbers)
				return True
		return False