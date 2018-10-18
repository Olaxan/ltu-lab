import utils
import os
import phonebook as pb
import pbshell as sh

DEFAULT_PATH = "users.dat"

book = pb.PhoneBook(DEFAULT_PATH)
shell = sh.PBShell(book)

if __name__ == '__main__':
	shell.cmdloop()

