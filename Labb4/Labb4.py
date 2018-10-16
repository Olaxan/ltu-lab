import utils
import os
import phonebook as pb
import pbshell as sh

DEFAULT_PATH = "users.dat"

book = pb.PhoneBook()
shell = sh.PhonebookShell(book)

if __name__ == '__main__':
	book.load(DEFAULT_PATH)
	shell.cmdloop()

