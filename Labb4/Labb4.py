import utils
import os
import phonebook as pb
import pbshell as sh

book = pb.PhoneBook()
shell = sh.PhonebookShell(book)

if __name__ == '__main__':
	shell.cmdloop()

