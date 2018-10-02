from command import *
import user

def addUser(userList, name, number, alias):
	new = user(args)
	userList.append(new)

def lookupUser():
	pass

commmands = [
	Command("add", str, addUser, 
		 Command("number", str),
		 Command("alias", str)
	),
	Command("lookup", str, lookupUser,
		 Command("number", str)
	)]