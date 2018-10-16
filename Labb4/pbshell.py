import cmd
import utils
import kwtok
import phonebook as pb

class PhonebookShell(cmd.Cmd):

	def __init__(self, book : type(pb.PhoneBook)):
		cmd.Cmd.__init__(self)
		self.book = book

	intro = "TelePOST Catalogue System v0.01 ALPHA.\nType help or ? to list commands.\n"
	prompt = "POST> "

	def do_add(self, arg):

		tokenizer = kwtok.KeywordTokenizer(arg, "-id", "alias", "number")
		name = " ".join(tokenizer.rest)
		alias = " ".join(tokenizer.alias)
		number = tokenizer.number

		if tokenizer.id:
			user = self.book.findSingleUser(id=int(tokenizer.id))
			if user[0]:
				user[1].addAlias([alias, name])
				user[1].addNumber(number)
				print("Added to {}.".format(user[1].firstName.upper()))
			else:
				print("User not found!")
		else:
			user = self.book.addUser([name, alias], number)[1]
			print("Added {}.".format(user.firstName.upper()))

	def do_remove(self, arg):
		
		tokenizer = kwtok.KeywordTokenizer(arg, "-id", "number")

		find = self.book.findUsers(" ".join(tokenizer.rest), tokenizer.number, tokenizer.id)

		if not find[0]:
			print("User not found!")
		elif len(find[1]) > 1:
			print("Multiple users found! Please narrow your search using ID or number.\n")
			self.do_lookup(arg)
		else:
			firstName = find[1][0].firstName
			self.book.removeUser(user = find[1][0])
			print("Removed {}!".format(firstName.upper()))

	def do_lookup(self, arg):
		tokenizer = kwtok.KeywordTokenizer(arg, "-id", "number")

		for user in self.book.findUsers(" ".join(tokenizer.rest), tokenizer.number, tokenizer.id)[1]:
			self.book.printSingleUser(user)

	def do_change(self, arg):
		
		tokenizer = kwtok.KeywordTokenizer(arg, "-id", "number")

		find = self.book.findUsers(" ".join(tokenizer.rest), tokenizer.number, tokenizer.id)

		if not find[0]:
			print("User not found!")
		elif len(find[1]) > 1:
			print("Multiple users found! Please narrow your search using ID or number.\n")
			self.do_lookup(arg)
		else:
			shell = PhonebookChangeShell(find[1][0])
			shell.cmdloop()

	def do_list(self, arg):
		self.book.printUsers()

	def do_save(self, arg):
		if self.book.save(arg):
			print("Saved to file {}.".format(arg))
		else:
			print("Failed to save!")

	def do_load(self, arg):
		if self.book.load(arg):
			print("Loaded from file {}.".format(arg))
		else:
			print("Failed to load!")

	def do_exit(self, arg):
		return True

	def help_lookup(self):
		print("LOOKUP: Finds users in the phonebook.")
		print("SYNTAX: lookup <Name> [<Number>] [<ID>]")

	def help_change(self):
		print("CHANGE: Makes changes to a user in the phonebook.")
		print("SYNTAX: change <Name> [number <Number>] [name <Name>]")

	def help_list(self):
		print("LIST: Lists all users in the phonebook.")
		print("SYNTAX: list")

	def help_remove(self):
		print("REMOVE: Removes a user, or if used with additional arguments: data from a user")
		print("SYNTAX: remove <Name>/<ID> [number <Number>] [name <Name>]")

	def help_add(self):
		print("ADD: Adds a user to the phonebook. If used with an ID, appends to an existing user.")
		print("SYNTAX: add <Name>/<ID> number <Number> alias <Alias>")

	def help_exit(self):
		print("EXIT: Exits the phonebook.")
		print("SYNTAX: exit")

class PhonebookChangeShell(cmd.Cmd):

	def __init__(self, user):
		cmd.Cmd.__init__(self)
		self.user = user
		PhonebookChangeShell.prompt = "POST({})> ".format(self.user.firstName.upper())
		utils.clear()

	intro = "TelePOST Catalogue System v0.01 ALPHA.\nType help or ? to list commands.\n"

	def do_add(self, arg):
		
		tokenizer = kwtok.KeywordTokenizer(arg, "number", "alias")
		self.user.addAlias(tokenizer.alias)
		self.xuser.addNumber(tokenizer.number)

	def do_remove(self, arg):
		
		tokenizer = kwtok.KeywordTokenizer(arg, "number", "alias")
		#user.removeAlias(tokenizer.alias)
		#user.removeNumber(tokenizer.number)

	def do_exit(self, arg):
		return True