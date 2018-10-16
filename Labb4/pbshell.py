import cmd
import utils
import kwtok
import phonebook as pb

class PhonebookShell(cmd.Cmd):

	def __init__(self, book : type(pb.PhoneBook), completekey = 'tab', stdin = None, stdout = None):
		self.book = book
		return super().__init__(completekey, stdin, stdout)

	intro = "TelePOST Catalogue System v0.01 ALPHA.\nType help or ? to list commands.\n"
	prompt = "POST> "

	def do_add(self, arg):

		tokenizer = kwtok.KeywordTokenizer(arg, "alias", "number")
		name = " ".join(tokenizer.rest)
		alias = " ".join(tokenizer.alias)
		number = tokenizer.number

		if str.isdigit(tokenizer.user[0]):
			user = self.book.findSingleUser(id=int(tokenizer.user[0]))
			if user[0]:
				name = " ".join(tokenizer.rest[1:])
				user[1].addAlias([alias, name])
				user[1].addNumber(number)
				print("Added to {}.".format(user[1].firstName.upper()))
			else:
				print("User not found!")
		else:
			user = self.book.addUser([name, alias], number)[1]
			print("Added {}.".format(user.firstName.upper()))

	def do_remove(self, arg):
		
		tokenizer = kwtok.KeywordTokenizer(arg, "number")
		name = " ".join(tokenizer.rest)
		number = tokenizer.number

		if str.isdigit(tokenizer.user[0]):
			success = self.book.removeUser(id=int(tokenizer.user[0]))
		else:
			if len(self.book.findUsers(name, number)[1]) > 1:
				print("ERROR: Ambiguity - clarify or specify UID.")
				self.do_lookup(arg)
				success = False
			else:
				success = self.book.removeUser(name, number)

		if success:
			print("User {} removed.".format(name))
		else:
			print("Failed to remove user(s).")

	def do_lookup(self, arg):
		tokenizer = kwtok.KeywordTokenizer(arg, "number", "id")

		for user in self.book.findUsers(" ".join(tokenizer.rest), tokenizer.number, tokenizer.id)[1]:
			self.book.printSingleUser(user)

	def do_change(self, arg):
		args = arg.split()

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