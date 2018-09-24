from command import *
import user

def addUser(userList, *args):
	new = user(args)
	userList.append(new)

def lookupUser():
	pass

com_data = [
	Command("add", str, addUser, 
		 Command("number", str),
		 Command("alias", str)
	),
	Command("lookup", str, lookupUser,
		 Command("number", str)
	)
	]