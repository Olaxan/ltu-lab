def tryParse(n, base=10):
	try:
		test = int(n, base)
		return True, test
	except ValueError:
		return False, None

def showMenu(items, title="Menu:", showExit = True):
	print(title)
	for num, name in enumerate(items, start=1):
		print(num, ". ", name, sep='')
	if showExit:
		print("0. Exit\n")
		return requestInt(lower=0, upper=len(items), error="\nPlease select an item between "+str(1 - int(showExit))+"-"+str(len(items))+".")

def requestInt(prompt = "> ", error = "\nPlease enter an integer.", lower = float('-inf'), upper = float('inf'), exitChar = None):
	if (exitChar != None):
		print("Enter", exitChar, "to exit.")
	while True:
		user = input(prompt)
		valid, out = tryParse(user)
		if valid and lower <= out <= upper:
			if (user == exitChar):
				return None
			return out
		else:
			print(error)