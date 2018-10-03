import os
import json

class wordList:
	"""
		Represents a list of words and definitions, with functions to add, get, or remove.
		Has 3 different options for inner representation:
		1 = DICTIONARY
		2 = TUPLE LIST
		3 = KEY-VALUE-LISTS
	"""

	def __init__(self, mode):
		if mode == 0:
			self.words = {}
			self.mode = 0
		if mode == 1:
			self.words = []
			self.mode = 1
		if mode == 2:
			self.words = [[],[]]
			self.mode = 2

	def setWord(self, key, val):
		"""Adds a word to the wordlist, depending on the mode of the list."""
		if self.mode == 0:
			return self.__dictAdd(key, val)
		elif self.mode == 1:
			return self.__tupleAdd(key, val)
		elif self.mode == 2:
			return self.__list2Add(key, val)


	def getWord(self, key):
		"""Gets a word from the wordlist, depending on the mode of the list."""
		if self.mode == 0:
			return self.__dictGet(key)
		elif self.mode == 1:
			return self.__tupleGet(key)
		elif self.mode == 2:
			return self.__list2Get(key)
		return None

	def printWords(self):
		"""Prints all words in the wordlist, depending on the mode of the list."""
		if self.mode == 0:
			return self.__dictPrint()
		elif self.mode == 1:
			return self.__tuplePrint()
		elif self.mode == 2:
			return self.__list2Print()
		return None

	def removeWord(self, key):
		"""Removes a word from the wordlist, depending on the mode of the list."""
		if self.mode == 0:
			return self.__dictRemove(key)
		elif self.mode == 1:
			return self.__tupleRemove(key)
		elif self.mode == 2:
			return self.__list2Remove(key)
		return False

	def saveWords(self, path):
		"""Saves the wordlist to a JSON file, as well as the mode of the list."""
		save = (self.mode, self.words)
		with open(path, "w") as wf:
			json.dump(save, wf)
			return True
		return False

	def loadWords(self, path):
		"""Loads a wordlist from JSON, as well as the mode of the list."""
		if (os.path.isfile(path)):
			with open(path, "r") as rf:
				save = json.load(rf)
				self.mode = save[0]
				self.words = save[1]
				return True
		return False


	#DICTIONARY FUNCTIONS - MODE 0

	def __dictAdd(self, key, val):
		"""Adds a word to the dictionary, if it doesn't already exist. Returns success."""
		if self.__dictGet(key) == None:
			self.words[key.lower()] = val
			return True
		else:
			return False

	def __dictGet(self, key):
		"""Gets a word from the dictionary, None if not found."""
		return self.words.get(key.lower())

	def __dictPrint(self):
		"""Prints the entire dictionary."""
		for key, val in self.words.items():
		    print("{}: {}".format(key.upper(), val))

	def __dictRemove(self, key):
		"""Removes a word from the list. Returns success."""
		if self.__dictGet(key) != None:
			del self.words[key.lower()]
			return True
		else:
			return False

	#TUPLE FUNCTIONS - MODE 1

	def __tupleAdd(self, key, val):
		"""Adds a key-val tuple to the list, if not already present. Returns success."""
		if self.__tupleGet(key) == None:
			self.words.append((key, val))
			return True
		else:
			return False

	def __tupleGet(self, key):
		"""Gets a word from the list. Returns value of key, None if not present."""
		for k, v in self.words:
			if k == key:
				return v
			else:
				return None

	def __tuplePrint(self):
		"""Prints all words in list."""
		for key, val in self.words:
		    print("{}: {}".format(key.upper(), val))

	def __tupleRemove(self, key):
		"""Removes a key-val tuple from the list."""
		test = len(self.words)
		self.words = [i for i in self.words if i[0] != key]
		return test != len(self.words)

	#LIST FUNCTIONS - MODE 2

	def __list2Add(self, key, val):
		"""Adds a key and value to their respective lists, if not present. Returns success."""
		if self.__list2Get(key) == None:
			self.words[0].append(key)
			self.words[1].append(val)
			return True
		else:
			return False

	def __list2Get(self, key):
		"""Gets a value from its corresponding key. Returns value, None if not present."""
		for i, item in enumerate(self.words[0]):
			if item == key:
				return self.words[1][i]
			else:
				return None

	def __list2Print(self):
		"""Prints all keys and values in the list."""
		for i, item in enumerate(self.words[0]):
		    print("{}: {}".format(item.upper(), self.words[1][i]))

	def __list2Remove(self, key):
		"""Removes key and value from list, if present. Returns success."""
		for i, item in enumerate(self.words[0]):
			if item == key:
				del self.words[0][i]
				del self.words[1][i]
				return True
		return False