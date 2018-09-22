import utils
import os

print("TelePOST Catalogue System v0.01 ALPHA")

com_data = {
	'add': ("number", "alias", "test"),
	'lookup': ("name", "number"),
	'exit': "hello"
	}

while True:
	com = utils.query() #add, Firstname, Lastname, num, 86332, alias, CoolGuy96, Fucko99

	if com[0] in com_data:					#if the initial command is valid...
		for sub_com in com_data[com[0]]:	#loop through subcommands...
			if sub_com in com:				#if a subcommand is recognized...
				ind = com.index(sub_com)	#find index of subcommand in tuple of valid subcommands (see com_data)
				#print("command '{}' accepted (index {})".format(sub_com, ind))
				if len(com) - 1 > ind and com[ind + 1] not in com_data[com[0]]:		#if a valid subcommand is found, check if it's followed by a value (not a subcommand)
					print(com[ind].upper())
					for x in range(ind + 1, len(com)):		#loop through next values, until the end of the command string...
						if com[x] in com_data[com[0]]:		#or until a valid subcommand is found...
							del com[ind:x]					#in which case, delete these subcommands (leaving only the main command string)...
							break							#then break TODO: make natural end-of-loop also delete commands
						print (com[x])
					#print("{0}: {1}".format(sub_com, com[ind + 1]))
					#del com[ind:len(com)]
				else:
					print("SYNTAX: '{0}' {1}".format(com[0], com_data[com[0]]))
		print(com)









#add Tord Fredrik Gustav Lind (num 0733573176 alias Toady)
#0	 1    2       3      4     5   6          7     8
#!   -    -       -      -     !   -          !     -

