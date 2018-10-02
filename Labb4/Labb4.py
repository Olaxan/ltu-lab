import utils
import os
import com_data
from command import *

#com_data = {
#	'add': ["number", "alias", "test"],
#	'lookup': ["name", "number"],
#	'exit': "hello"
#	}

print("TelePOST Catalogue System v0.01 ALPHA")

Command.evaluate(com_data.commmands, utils.query()) #add, Firstname, Lastname, num, 86332, alias, CoolGuy96, Fucko99

#add Tord Fredrik Gustav Lind (num 0733573176 alias Toady)
#0	 1    2       3      4     5   6          7     8
#!   -    -       -      -     !   -          !     -

#=(add, Tord, Fredrik, Gustav, Lind)
#=(num, 0733573176)
#=(alias, Toady)

