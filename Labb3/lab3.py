import utils
import os
import json

PATH = "words.json"

menuItems = [
	"Add item",
	"Lookup item",
	"Remove item",
	"Show all items",
	"Save",
	"Load"
	]

words = {}

while True:
	os.system("cls")
	select = utils.showMenu(menuItems)

	if select == 0:
		break
	elif select == 1:
		key = input("Enter word: ")
		val = input("Enter definition: ")
		words[key.lower()] = val
		print("Added '{}'!".format(key))
	elif select == 2:
		key = input("Enter word: ")
		val = words.get(key.lower())
		if val == None:	
			print("Word '{}' not found.".format(key))
		else:
			print("{}: {}".format(key.upper(), val))
	elif select == 3:
		key = input("Enter word: ")
		val = words.get(key)
		if val == None:
			print("Word '{}' not found.".format(key))
		else:
			del words[key]
			print("Removed '{}'!".format(key))
	elif select == 4:
		for key, val in words.items():
		    print("{}: {}".format(key.upper(), val))
	elif select == 5:
		with open(PATH, "w") as wf:
			json.dump(words, wf)
			print("Saved to '{}'!".format(PATH))
	elif (select == 6):
		if (os.path.isfile(PATH)):
			with open(PATH, "r") as rf:
				print("Loaded from '{}'!".format(PATH))
				words = json.load(rf)
		else:
			print("Couldn't load words - file not found.")

	input("\nPress enter to continue...")



