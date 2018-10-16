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

	def removeUser(self, user = None, name = None, number = None, id = None):
		"""Removes users matching specified name (+ alias) and numbers."""
		l = len(self.users)
		if user:
			r = utils.toCleanList(user)
		else:
			r = self.findUsers(name, number, id)[1]
		self.users = [user for user in self.users if user not in r]
		return l != len(self.users)

	def findUsers(self, name = None, number = None, id = None):
		"""Finds users matching specified name/alias, number, or UID."""

		names = utils.toCleanList(name)
		numbers = utils.toCleanList(number)
		ids = utils.toCleanList(id)

		#print("Name(s): {}, Number(s): {}, ID(s): {}".format(names, numbers, ids))

		matches = []

		for user in self.users:
			test_name = len(names) == 0
			test_num = len(numbers) == 0
			test_id = len(ids) == 0

			for name in names:
				for userName in user.names:
					if userName.lower().find(name.lower()) > -1:
						test_name = True
			for num in numbers:
				for userNum in user.numbers:
					if userNum.find(num) > -1:
						test_num = True
			for id in ids:
				if str(id) == str(user.id):
					test_id = True

			if test_name and test_num and test_id:
				matches.append(user)

		return len(matches) > 0, matches

	def findSingleUser(self, name = None, number = None, id = None):
		"""Finds a single user matching specified name/alias, number, or UID."""
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
		"""Prints details about a single specified user."""
		user.toString()

	def clear(self):
		"""Clears the phonebook."""
		self.users.clear()

	def save(self, path):
		"""Saves the phonebook to a file, using a super special proprietary format."""
		with open(path, "w") as wf:
			for user in self.users:
				wf.write("{0};{1}\n".format("/".join(user.names), "/".join(user.numbers)))
			return True
		return False

	def load(self, path):
		"""Loads all users from the specified file."""
		if (os.path.isfile(path)):
			with open(path, "r") as rf:
				for line in rf.readlines():
					names = re.search("^(.*?);", line)
					numbers = re.search(";(.+)$", line)
					if names and numbers:
						names = names.group(1).split("/")
						numbers = numbers.group(1).split("/")
						self.addUser(names, numbers)
					else:
						return False
				return True
		return False