from user import *

class PhoneBook:

	def __init__(self, *args, **kwargs):
		self.users = list()
		return super().__init__(*args, **kwargs)

	def addUser(self, name, number = None, alias = None):
		"""Adds a new user to the phonebook and returns the User object."""
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
			matches = [user for user in matches if user.numbersToString().find(number)]

		if len(matches) > 0:
			return matches
		else:
			return None

	def printBook(self):
		"""Prints the contents of the phonebook in a formatted manner."""
		print(len(self.users), "user(s):")
		for user in self.users:
			print("{0}, {1} {2}".format(user.lastName.upper(), user.firstName, user.middleName))
			if (len(user.aliases) > 0):
				print("AKA:", ", ".join(user.aliases).join(("'","'")))
			for num in user.numbers:
				print("\t# {0}".format(num))
			print()

	def save(self, path):
		with open(path, "w") as wf:
			for user in self.users:
				wf.writelines()
		return False