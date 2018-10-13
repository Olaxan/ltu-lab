import cmd
import phonebook as pb

class PhonebookShell(cmd.Cmd):

	def __init__(self, book : type(pb.PhoneBook), completekey = 'tab', stdin = None, stdout = None):
		self.book = book
		return super().__init__(completekey, stdin, stdout)

	intro = "TelePOST Catalogue System v0.01 ALPHA.\nType help or ? to list commands.\n"
	prompt = "POST> "

	def do_add(self, arg):
		args = arg.split()
		iNum, iAlias = len(args), len(args)
		num, alias = None, None
		

		if len(args) > 1:

			if str.isdigit(args[1]):
				user = self.book.getUserFromID(int(args[1]))

			if "number" in args:
				iNum = args.index("number")
			if "alias" in args:
				iAlias = args.index("alias")

			name = " ".join(args[:min(iNum, iAlias)])

			if iAlias < len(args):
				alias = " ".join(args[iAlias + 1:min(iNum + (iAlias > iNum) * 1000, len(args))])
				#fix the stupid shit
			if iNum < len(args):
				num = args[iNum + 1:min(iAlias + (iNum > iAlias) * 1000, len(args))]

			self.book.addUser([name, alias], num)

	def help_add(self):
		print("ADD: Adds a user to the phonebook.")
		print("SYNTAX: add <Name>/<ID> number <Number> alias <Alias>")

	def do_lookup(self, arg):
		for user in self.book.findUsers(arg)[1]:
			print(user.names[0], ":", user.numbersToString())

	def help_lookup(self):
		print("LOOKUP: Finds users in the phonebook.")
		print("SYNTAX: lookup <Name> [number <Number>]")

	def do_change(self, arg):
		args = arg.split()

	def help_change(self):
		print("CHANGE: Makes changes to a user in the phonebook.")
		print("SYNTAX: change <Name> [number <Number>] [name <Name>]")

	def do_list(self, arg):
		self.book.printAll()

	def help_list(self):
		print("LIST: Lists all users in the phonebook.")
		print("SYNTAX: list")

	def do_exit(self, arg):
		return True

	def help_exit(self):
		print("EXIT: Exits the phonebook.")
		print("SYNTAX: exit")