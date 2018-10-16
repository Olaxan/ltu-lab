import utils

class User:

	numUsers = 0

	def __init__(self, name, number = None):
		self.id = User.numUsers
		self.names = utils.toCleanList(name)
		self.numbers = utils.toCleanList(number)
		User.numUsers += 1

	@property
	def firstName(self):
		return self.names[0].split()[0]

	@property
	def middleName(self):
		return " ".join(self.names[0].split()[1:-1])

	@property
	def lastName(self):
		return self.names[0].split()[-1]

	def addNumber(self, args):
		"""Adds one or several numbers to the user."""
		l = utils.toCleanList(args)
		for arg in l:
			self.numbers.append(arg)

	def addAlias(self, args):
		"""Adds one or several names to the user."""
		l = utils.toCleanList(args)
		for arg in l:
			self.names.append(arg)

	def removeNumber(self, args):
		"""Removes one or several numbers from the user."""
		l = utils.toCleanList(args)
		t = len(self.numbers)
		for arg in l:
			if arg in self.numbers:
				self.numbers.remove(arg)
		return t is not len(self.numbers)

	def removeAlias(self, args):
		"""Removes one or several names from the user."""
		l = utils.toCleanList(args)
		t = len(self.names)
		for arg in l:
			if arg in self.names and arg != self.names[0]:
				self.names.remove(arg)
		return t is not len(self.names)

	def namesToString(self):
		"""Returns a string of comma-separated names and aliases for the user."""
		return ", ".join(self.names)

	def numbersToString(self):
		"""Returns a string of comma-separated numbers for the user."""
		return ", ".join(self.numbers)

	def toString(self):
		"""Prints a formatted overview of user info."""
		print("#{0}: {1}, {2} {3}".format(self.id, self.lastName.upper(), self.firstName, self.middleName))
		if len(self.names) > 1:
			print("AKA:", ", ".join(self.names[1:]))
		for num in self.numbers:
			print("  - {0}".format(num))
		print()


