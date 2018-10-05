from user import *

class PhoneBook:

	def __init__(self, *args, **kwargs):
		self.users = []
		return super().__init__(*args, **kwargs)

	def addUser(self, name, number = None):
		self.users.append(User(name, number))

	def findUser(self, search):
		for user in self.users:
			if user.name.find(search):
				return user
		return False

	def findUsers(self, search):


	
