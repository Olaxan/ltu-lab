import utils

class User:

	def __init__(self, name, number = None, *args, **kwargs):
		self.names = utils.toCleanList(name)
		self.numbers = utils.toCleanList(number)

		return super().__init__(*args, **kwargs)

	@property
	def firstName(self):
		return self.names[0].split()[0]

	@property
	def middleName(self):
		return " ".join(self.names[0].split()[1:-1])

	@property
	def lastName(self):
		return self.names[0].split()[-1]

	def addNumber(self, number):
		self.numbers.append(number)

	def addAlias(self, alias):
		self.names.append(alias)

	def namesToString(self):
		return ",".join(self.names)

	def numbersToString(self):
		return ",".join(self.numbers)


