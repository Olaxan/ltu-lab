class PhoneBook:

	def __init__(self, *args, **kwargs):
		self.users = []	

	def addUser(self, name : str, number : str = None, *args, **kwargs):
		if self.getSingleUser(name):
			return False
		else:
			self.users.append(User(name, number))
			return True

	def getSingleUser(self, search):
		for user in self.users:
			if user.name == search or user.alias == search:
				return user
		return None

	def getUsers(self, search):
		return [i for i in self.users if i.name == search or i.alias == search]

class User:

	def __init__(self, name : str, number : str = None, *args, **kwargs):
		self.addName(name)
		self.addNumber(number)
		self.alias = []
		for key, value in kwargs.items():
			self.__setattr__(key, value)

	def addName(self, name : str):
		names = name.split()
		self.firstName = names[0]
		if len(names) > 1:
			self.lastName = names[-1]

	def addNumber(self, num : str):
		self.number.extend(num.split())

	def addAlias(self, alias):
		self.alias.append(alias)
		
