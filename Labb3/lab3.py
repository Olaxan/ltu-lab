import utils
import os
import lab3_func

PATH = "words.json"
MODE = 1

menuItems = [
	"Add item",
	"Lookup item",
	"Remove item",
	"Show all items",
	"Save",
	"Load"
	]

print("Welcome to Word-Pal 2000!")

wordList = lab3_func.wordList(MODE)
if wordList.loadWords(PATH):
	print("Loaded from '{0}' (mode {1})!".format(PATH, wordList.mode))

print()

while True:
	select = utils.showMenu(menuItems)

	if select == 0:
		#Exit program
		if utils.ask("Save changes?"):
			wordList.saveWords(PATH)
		break

	elif select == 1:
		#Add new word
		key = input("Enter word: ")
		val = input("Enter definition: ")
		if wordList.setWord(key, val):
			print("Added '{0}'!".format(key))
		else:
			print("Word '{0}' already exists!".format(key))

	elif select == 2:
		#Lookup a word
		key = input("Enter word: ")
		val = wordList.getWord(key)
		if val == None:	
			print("Word '{}' not found.".format(key))
		else:
			print("{}: {}".format(key.upper(), val))

	elif select == 3:
		#Remove a word
		key = input("Enter word: ")
		success = wordList.removeWord(key)
		if success:
			print("Removed '{}'!".format(key))
		else:
			print("Word '{}' not found.".format(key))
			
	elif select == 4:
		#List all words
		wordList.printWords()

	elif select == 5:
		#Save words to file
		if wordList.saveWords(PATH):
			print("Saved to '{}'!".format(PATH))
		else:
			print("Could not save words - unknown error.")

	elif (select == 6):
		#Load words from file
		if wordList.loadWords(PATH):
			print("Loaded from '{}'!".format(PATH))
		else:
			print("Couldn't load words - file not found.")

	input("\nPress enter to continue...")
	os.system("cls")



