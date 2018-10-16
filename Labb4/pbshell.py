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

	def precmd(self, line):
		if line != "help":
			print()
		return line

	def do_add(self, arg):
		"""Adds a new user to the phonebook, or appends data to an existing one if  used with ID.
		All fields are optional. User name needs no prefix in command."""

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
			shell = PhonebookChangeShell(self.book, find[1][0])
			shell.cmdloop()

	def do_list(self, arg):
		"""Lists all users in the phonebook."""
		self.book.printUsers()

	def do_clear(self, arg):
		utils.clear()

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
		print("Finds users in the phonebook.")
		print("SYNTAX: lookup [<Name>] [number <Number>] [alias <Alias>] [id <ID>]")

	def help_change(self):
		print("Makes changes to a user in the phonebook.")
		print("SYNTAX: change [<Name>] [number <Number>] [alias <Alias>] [id <ID>]")

	def help_remove(self):
		print("Removes a user, or if used with additional arguments: data from a user")
		print("SYNTAX: remove [<Name>] [number <Number>] [alias <Alias>] [id <ID>]")

	def help_add(self):
		print("Adds a user to the phonebook. If used with an ID, appends to an existing user.")
		print("SYNTAX: add [<Name>] [number <Number>] [alias <Alias>] [id <ID>]")

	def help_save(self):
		print("Saves the phonebook to the disk.")
		print("SYNTAX: save <Path>")

	def help_load(self):
		print("Loads a saved phonebook from disk.")
		print("SYNTAX: load <Path>")

	def help_exit(self):
		print("EXIT: Exits the phonebook.")

	def help_list(self):
		print("Lists all users in the phonebook.")

	def help_clear(self):
		print("Clears the screen.")

class PhonebookChangeShell(cmd.Cmd):

	def __init__(self, book, user):
		cmd.Cmd.__init__(self)
		self.book = book
		self.user = user
		PhonebookChangeShell.prompt = "POST({})> ".format(self.user.firstName.upper())
		utils.clear()

	intro = "TelePOST Catalogue System v0.01 ALPHA.\nType help or ? to list commands.\n"

	def precmd(self, line):
		if line != "help":
			print()
		return line

	def do_add(self, arg):
		
		tokenizer = kwtok.KeywordTokenizer(arg, "number", "alias")
		self.user.addAlias(" ".join(tokenizer.alias))
		self.user.addNumber(tokenizer.number)
		self.user.toString()

	def do_remove(self, arg):
		
		tokenizer = kwtok.KeywordTokenizer(arg, "number", "alias")
		self.user.removeAlias(tokenizer.alias)
		self.user.removeNumber(tokenizer.number)
		self.user.toString()

	def do_show(self, arg):
		self.user.toString()

	def do_delete(self, arg):
		if utils.ask("Are you sure you want to delete {}?".format(self.user.firstName)):
			self.book.removeUser(user = self.user)
			return True

	def do_exit(self, arg):
		return True

	def help_add(self):
		print("Adds values to the user.")
		print("SYNTAX: add [number <Number>] [alias <Alias>]")

	def help_remove(self):
		print("Removes values from the user.")
		print("SYNTAX: remove [number <Number>] [alias <Alias>]")

	def help_show(self):
		print("Displays the user in a formatted manner.")

	def help_delete(self):
		print("Deletes the user completely from the phonebook.")

	def help_exit(self):
		print("Exits the user editing mode.")