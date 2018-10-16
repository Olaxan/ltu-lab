import os

def sign(n):
	"""Returns the sign of an integer (1, 0 -1)."""
	if n == 0:
		return int(0)
	else:
		return int(n / abs(n))

def neg(n):
	return -abs(n)

def tryParse(n, base=10):
	"""Attemtpts to convert a string to an integer, returning a tuple of (bool Success, int Integer)."""
	try:
		test = int(n, base)
		return True, test
	except ValueError:
		return False, None

def showMenu(items, title="Menu:", showExit = True):
	"""Displays a menu of strings from 'items', and returns a corresponding user selection."""
	print(title)
	for num, name in enumerate(items, start=1):
		print(num, ". ", name, sep='')
	if showExit:
		print("0. Exit\n")
		return requestInt(lower=0, upper=len(items), error="\nPlease select an item between "+str(1 - int(showExit))+"-"+str(len(items))+".")

def requestInt(prompt = "> ", error = "\nPlease enter an integer.", lower = float('-inf'), upper = float('inf'), exitChar = None):
	"""Prompts the user for a number until they make a correct selection, or enter the exitChar, if set."""
	if (exitChar != None):
		print("Enter", exitChar, "to exit.")
	while True:
		user = input(prompt)
		valid, out = tryParse(user)
		if valid and lower <= out <= upper:
			if user == exitChar:
				return None
			return out
		else:
			print(error)

def ask(text, prompt = "> ", error = "\nPlease answer y/n.", exitChar = None):
	"""Asks the user a question, and looks for positive/negative replies until a correct input is made, or exitChar is entered."""
	print(text, "(y/n)")
	if (exitChar != None):
		print("Enter", exitChar, "to exit.")
	while True:
		user = input(prompt).lower()
		if user == exitChar:
			return None
		elif user in ("y", "yes", "yas", "yep", "ja", "yay"):
			return True
		elif user in ("n", "no", "nope", "nej", "nay"):
			return False
		else:
			print(error)

def query(sep = None, prompt = "> ", error = "\n???", exitChar = None):
	"""Queries the user for input, and returns the input as a list, split by 'sep'."""
	if (exitChar != None):
		print("Enter", exitChar, "to exit.")
	while True:
		user = input(prompt)
		if user == exitChar:
			return None
		return user.split(None)

def toCleanList(obj):
	"""Returns 'obj' as a list, and strips away falsey entries."""
	if type(obj) is not list : obj = [obj]
	return list(filter(None, obj))

def hasCommonMember(a, b):
	"""Returns whether the two enumerables has common members."""
	a2 = set(a) 
	b2 = set(b) 
	return len(a2.intersection(b2)) > 0

def clear(): 
	"""Clears the command prompt in a Win/Linux friendly manner."""
	if os.name == 'nt': 
		os.system('cls') 
	else: 
		os.system('clear')