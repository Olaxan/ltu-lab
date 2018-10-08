import utils
import os
import comparse
import phonebook as pb

print("TelePOST Catalogue System v0.01 ALPHA")
print()

#parser = comparse.CommandParser()
#parser.add_command("add", "+", "Adds a user to the phonebook.")
#parser.add_command("lookup", "?", "Displays information about a post in the phonebook")

book = pb.PhoneBook()

fl = book.addUser(["Tord Fredrik Gustav Lind", "Smörgås"], "073-3573176")
fl.addNumber("070-2867892")
gl = book.addUser("Göran Lind", "072-2867862")
gl.addAlias("Gås")

print("BEFORE LOAD:")
book.printAll()
book.save("data.txt")
book.clear()
book.load("data.txt")
print("AFTER LOAD:")
book.printAll()
#add Tord Fredrik Gustav Lind (num 0733573176 alias Toady)
#0	 1    2       3      4     5   6          7     8
#!   -    -       -      -     !   -          !     -

#=(add, Tord, Fredrik, Gustav, Lind)
#=(num, 0733573176)
#=(alias, Toady)

