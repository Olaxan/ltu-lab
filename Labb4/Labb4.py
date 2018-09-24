import utils
import os
import com_data
from command import *

com_data = {
	'add': ["number", "alias", "test"],
	'lookup': ["name", "number"],
	'exit': "hello"
	}

print("TelePOST Catalogue System v0.01 ALPHA")

while True:
	com = utils.query() #add, Firstname, Lastname, num, 86332, alias, CoolGuy96, Fucko99

	valid = []
	if com[0] in com_data and len(com) > 1:

		com.append(None) #Until I can figure out a better program flow, None serves as a null terminator for the command parser.
		curr = []

		for sub in com:
			if sub in list(com_data) + com_data[com[0]] + [None]:
				if len(curr) > 0:
					valid.append(curr.copy())
					curr.clear()
			curr.append(sub)
		
		print(valid)

#add Tord Fredrik Gustav Lind (num 0733573176 alias Toady)
#0	 1    2       3      4     5   6          7     8
#!   -    -       -      -     !   -          !     -

#=(add, Tord, Fredrik, Gustav, Lind)
#=(num, 0733573176)
#=(alias, Toady)

