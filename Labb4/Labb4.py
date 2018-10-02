import utils
import os
import comparse
import argparse

print("TelePOST Catalogue System v0.01 ALPHA")

parser = comparse.CommandParser()
parser.add_command("add", "+", "Adds a user to the phonebook.")
parser.add_command("lookup", "?", "Displays information about a post in the phonebook")

while True:

	parser.evaluate(utils.query(prompt = ">"))

#add Tord Fredrik Gustav Lind (num 0733573176 alias Toady)
#0	 1    2       3      4     5   6          7     8
#!   -    -       -      -     !   -          !     -

#=(add, Tord, Fredrik, Gustav, Lind)
#=(num, 0733573176)
#=(alias, Toady)

