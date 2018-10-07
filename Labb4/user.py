class User:

	def __init__(self, name : str, number : str = None, alias : str = None, *args, **kwargs):
		self.firstName = ""
		self.middleName = ""
		self.lastName = ""
		self.name = name
		self.numbers = list()
		self.aliases = list()

		if number:
			self.numbers.append(number)
		if alias:
			self.aliases.append(alias)
		return super().__init__(*args, **kwargs)

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, value):
		self._name = value
		n = value.split()
		if len(n) > 1:
			self.firstName = n[0]
			self.lastName = n[-1]
			if len(n) > 2:
				self.middleName = " ".join(n[1:-1])

	@name.deleter
	def name(self):
		del self._name

	def addNumber(self, number):
		self.numbers.append(number)

	def addAlias(self, alias):
		self.aliases.append(alias)

	def namesToString(self):
		return ",".join(self.aliases + self.name.split())

	def numbersToString(self):
		return ",".join(self.numbers)


