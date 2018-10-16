import re
import os
import utils
from user import *

class PhoneBook:

	def __init__(self, *args, **kwargs):
		self.users = list()

	def addUser(self, name, number = None):
		"""Adds a new user to the phonebook and returns the User object."""

		names = utils.toCleanList(name)
		numbers = utils.toCleanList(number)

		for num in numbers:
			test = self.findUsers(number=num)
			if test[0]:
				print("Number {} already exists!".format(num))
				return False, test[1]

		new = User(name, number)
		self.users.append(new)
		return True, new

	def removeUser(self, name = None, number = None, id = None):
		"""Removes users matching specified name (+ alias) and numbers."""
		l = len(self.users)
		r = self.findUsers(name, number, id)[1]
		self.users = [user for user in self.users if user not in r]
		return l != len(self.users)

	def findUsers(self, name = None, number = None, id = None):
		"""Finds users matching specified name (+ alias) and numbers, alternatively using UID."""

		matches = [user for user in self.users if 
			 (id is None or user.id == id) and
			 (name is None or user.namesToString().lower().find(name.lower())) and 
			 (number is None or number in user.numbers) 
			 ]

		return len(matches) > 0, matches

	def findSingleUser(self, name = None, number = None, id = None):
		user = self.findUsers(name, number, id)
		if user[0]:
			return user[0], user[1][0]
		else:
			return False, None

	def printUsers(self):
		"""Prints the contents of the phonebook in a formatted manner."""
		print(len(self.users), "user(s):")
		for user in self.users:
			self.printSingleUser(user)

	def printSingleUser(self, user):
		print("#{0}: {1}, {2} {3}".format(user.id, user.lastName.upper(), user.firstName, user.middleName))
		if len(user.names) > 1:
			print("AKA:", ", ".join(user.names[1:]))
		for num in user.numbers:
			print("  - {0}".format(num))
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