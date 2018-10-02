import os
import json

class wordList:

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
		if self.mode == 0:
			return self.__dictAdd(key, val)
		elif self.mode == 1:
			return self.__tupleAdd(key, val)
		elif self.mode == 2:
			return self.__list2Add(key, val)


	def getWord(self, key):
		if self.mode == 0:
			return self.__dictGet(key)
		elif self.mode == 1:
			return self.__tupleGet(key)
		elif self.mode == 2:
			return self.__list2Get(key)
		return None

	def printWords(self):
		if self.mode == 0:
			return self.__dictPrint()
		elif self.mode == 1:
			return self.__tuplePrint()
		elif self.mode == 2:
			return self.__list2Print()
		return None

	def removeWord(self, key):
		if self.mode == 0:
			return self.__dictRemove(key)
		elif self.mode == 1:
			return self.__tupleRemove(key)
		elif self.mode == 2:
			return self.__list2Remove(key)
		return False

	def saveWords(self, path):
		save = (self.mode, self.words)
		with open(path, "w") as wf:
			json.dump(save, wf)
			return True
		return False

	def loadWords(self, path):
		if (os.path.isfile(path)):
			with open(path, "r") as rf:
				save = json.load(rf)
				self.mode = save[0]
				self.words = save[1]
				return True
		return False


	#DICTIONARY FUNCTIONS - MODE 0

	def __dictAdd(self, key, val):
		if self.__dictGet(key) == None:
			self.words[key.lower()] = val
			return True
		else:
			return False

	def __dictGet(self, key):
		return self.words.get(key.lower())

	def __dictPrint(self):
		for key, val in self.words.items():
		    print("{}: {}".format(key.upper(), val))

	def __dictRemove(self, key):
		if self.__dictGet(key) != None:
			del self.words[key.lower()]
			return True
		else:
			return False

	#TUPLE FUNCTIONS - MODE 1

	def __tupleAdd(self, key, val):
		if self.__tupleGet(key) == None:
			self.words.append((key, val))
			return True
		else:
			return False

	def __tupleGet(self, key):
		for k, v in self.words:
			if k == key:
				return v
			else:
				return None

	def __tuplePrint(self):
		for key, val in self.words:
		    print("{}: {}".format(key.upper(), val))

	def __tupleRemove(self, key):
		test = len(self.words)
		self.words = [i for i in self.words if i[0] != key]
		return test != len(self.words)

	#LIST FUNCTIONS - MODE 2

	def __list2Add(self, key, val):
		if self.__list2Get(key) == None:
			self.words[0].append(key)
			self.words[1].append(val)
			return True
		else:
			return False

	def __list2Get(self, key):
		for i, item in enumerate(self.words[0]):
			if item == key:
				return self.words[1][i]
			else:
				return None

	def __list2Print(self):
		for i, item in enumerate(self.words[0]):
		    print("{}: {}".format(item.upper(), self.words[1][i]))

	def __list2Remove(self, key):
		for i, item in enumerate(self.words[0]):
			if item == key:
				del self.words[0][i]
				del self.words[1][i]
				return True
		return False

#if (os.path.isfile(PATH)):
#	with open(PATH, "r") as rf:
#		print("Loaded words from '{}'!".format(PATH))
#		words = json.load(rf)
#else:
#	words = {}