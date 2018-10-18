import cmd
import utils
import kwtok
import phonebook as pb

class PBShell(cmd.Cmd):

	def __init__(self, book : type(pb.PhoneBook)):
		cmd.Cmd.__init__(self)
		self.book = book

	intro = "TelePOST Catalogue System v0.5\nType help or ? to list commands.\n"
	prompt = "POST> "

	def precmd(self, line):
		"""Just for formatting - these commands will not print a newline before running."""
		if line and line.split()[0] not in ("help", "?"):
			print()
		return line

	def postcmd(self, stop, line):
		"""Just for formatting - these commands will not print a newline after running."""
		if line and line.split()[0] not in ("clear", "help", "?", "lookup", "list", "exit"):
			print()
		return stop

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
				print("Added to {0}.".format(user[1].firstName.upper()))
			else:
				print("User not found!")
		elif name:
			add = self.book.addUser([name, alias], number)
			if add[0]:
				print("Added {0}.".format(add[1].firstName.upper()))
			else:
				print("Can't add user with an existing number!")
		else:
			print("Can't add user without name or ID!")

	def do_remove(self, arg):
		"""Removes a user from the phonebook. Can be filtered using name, ID, and number."""

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
		"""Finds matching users in the phonebook, and prints their information.
		Filtered using name, number, and ID."""

		tokenizer = kwtok.KeywordTokenizer(arg, "-id", "number")

		for user in self.book.findUsers(" ".join(tokenizer.rest), tokenizer.number, tokenizer.id)[1]:
			self.book.printSingleUser(user)

	def do_change(self, arg):
		"""Enters 'change mode' for the specified user.
		Filtered with name, ID, and number."""

		tokenizer = kwtok.KeywordTokenizer(arg, "-id", "number")

		find = self.book.findUsers(" ".join(tokenizer.rest), tokenizer.number, tokenizer.id)

		if not find[0]:
			print("User not found!")
		elif len(find[1]) > 1:
			print("Multiple users found! Please narrow your search using ID or number.\n")
			self.do_lookup(arg)
		else:
			shell = PBShellChange(self.book, find[1][0])
			shell.cmdloop()

	def do_alias(self, arg):
		"""Directly adds or removes aliases to a user, filtered by name, ID, or number."""

		tokenizer = kwtok.KeywordTokenizer(arg, "-id", "number", "add", "remove")
		find = self.book.findUsers(" ".join(tokenizer.rest), tokenizer.number, tokenizer.id)

		if not find[0]:
			print("User not found!")
		elif len(find[1]) > 1:
			print("Multiple users found! Please narrow your search using ID or number.\n")
			self.do_lookup(arg)
		else:
			add = " ".join(tokenizer.add)
			remove = " ".join(tokenizer.remove)
			if tokenizer.add and find[1][0].addAlias(add):
				print("Alias {0} added successfully.".format(add.upper()))
			if tokenizer.remove:
				if find[1][0].removeAlias(remove):
					print("Alias {0} removed successfully.".format(remove.upper()))
				else:
					print("Alias {0} not found in user {1}.".format(remove.upper(), find[1][0].firstName.upper()))

	def do_number(self, arg):
		"""Directly adds or removes numbers to a user, filtered by name, ID, or number."""

		tokenizer = kwtok.KeywordTokenizer(arg, "-id", "number", "add", "remove")
		find = self.book.findUsers(" ".join(tokenizer.rest), tokenizer.number, tokenizer.id)

		if not find[0]:
			print("User not found!")
		elif len(find[1]) > 1:
			print("Multiple users found! Please narrow your search using ID or number.\n")
			self.do_lookup(arg)
		else:
			if tokenizer.add and find[1][0].addNumber(tokenizer.add):
				print("Number(s) {0} added successfully.".format(", ".join(tokenizer.add)))
			if tokenizer.remove:
				if find[1][0].removeNumber(tokenizer.remove):
					print("Number(s) {0} removed successfully.".format(", ".join(tokenizer.remove)))
				else:
					print("Number(s) {0} not found in user {1}.".format(", ".join(tokenizer.remove), find[1][0].firstName.upper()))

	def do_list(self, arg):
		"""Lists all users in the phonebook."""
		self.book.printUsers()

	def do_clear(self, arg):
		"""Clears the screen, OS safe."""
		utils.clear()

	def do_save(self, arg):
		"""Saves the phonebook to disk, to the specified path."""
		if self.book.save(arg):
			print("Saved to file {}.".format(arg))
		else:
			print("Failed to save!")

	def do_load(self, arg):
		"""Loads a phonebook from disk, using the specified path."""
		if self.book.load(arg):
			print("Loaded from file {}.".format(arg))
		else:
			print("Failed to load!")

	def do_exit(self, arg):
		"""Exists the shell
		TODO: Ask for save confirmation."""
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

	def help_alias(self):
		print("Adds or removes aliases to a phonebook user.")
		print("SYNTAX: alias [<Name>] [number <Number>] [id <ID>] [add <Alias>] [remove <Alias>]")

	def help_number(self):
		print("Adds or removes numbers to a phonebook user.")
		print("SYNTAX: number [<Name>] [number <Number>] [id <ID>] [add <Number>] [remove <Number>]")

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

class PBShellChange(cmd.Cmd):

	def __init__(self, book, user):
		cmd.Cmd.__init__(self)
		self.book = book
		self.user = user
		PBShellChange.prompt = "POST({})> ".format(self.user.firstName.upper())
		utils.clear()

	def preloop(self):
		print("Editing user:\n")
		self.user.toString()

	def precmd(self, line):
		if line and line.split()[0] not in ("help", "?"):
			print()
		return line

	def postcmd(self, stop, line):
		if line and line.split()[0] not in ("clear", "help", "?", "exit", "show", "add", "remove"):
			print()
		return stop

	def do_add(self, arg):
		"""Adds data to the user, number or alias."""

		tokenizer = kwtok.KeywordTokenizer(arg, "number", "alias")
		self.user.addAlias(" ".join(tokenizer.alias))
		self.user.addNumber(tokenizer.number)
		self.user.toString()

	def do_remove(self, arg):
		"""Removes data from the user, number or alias."""

		tokenizer = kwtok.KeywordTokenizer(arg, "number", "alias")
		self.user.removeAlias(tokenizer.alias)
		self.user.removeNumber(tokenizer.number)
		self.user.toString()

	def do_name(self, arg):
		"""Changes the user's primary name."""

		self.user.names[0] = arg
		print("Name change successful!")
		PBShellChange.prompt = "POST({})> ".format(self.user.firstName.upper())

	def do_show(self, arg):
		"""Shows user info."""
		self.user.toString()

	def do_delete(self, arg):
		"""Deletes the user, upon confirmation from the user."""

		if utils.ask("Are you sure you want to delete {0}?".format(self.user.firstName)):
			self.book.removeUser(user = self.user)
			return True

	def do_clear(self, arg):
		utils.clear()

	def do_exit(self, arg):
		"""Exits the shell."""
		return True

	def help_add(self):
		print("Adds values to the user.")
		print("SYNTAX: add [number <Number>] [alias <Alias>]")

	def help_remove(self):
		print("Removes values from the user.")
		print("SYNTAX: remove [number <Number>] [alias <Alias>]")

	def help_name(self):
		print("Changes the user's primary name.")
		print("SYNTAX: name <Name>")

	def help_show(self):
		print("Displays the user in a formatted manner.")

	def help_delete(self):
		print("Deletes the user completely from the phonebook.")

	def help_clear(self):
		print("Clears the screen.")

	def help_exit(self):
		print("Exits the user editing mode.")