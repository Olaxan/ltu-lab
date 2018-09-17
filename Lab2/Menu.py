import RekursionIteration as rek
import sys

def tryParse(n, base=10):
	try:
		test = int(n, base)
		return True, test
	except ValueError:
		return False, None

menuItems = [
	"Bounce", "Sum", "Solver"
	]

def showMenu(items, title="Menu:", showExit = True):
	while True:
		print(title)
		for num, name in enumerate(items, start=1):
			print(num, ". ", name, sep='')
		if showExit:
			print("0. Exit\n")
		valid, user = tryParse(input("> "))
		if valid and (1 - int(showExit)) <= user < len(menuItems):
			return user
		else:
			title = "\nPlease select an item between "+str(1 - int(showExit))+"-"+str(len(menuItems))+"."

def requestInt(type, title, showExit = False):
	print(title)
	return tryParse(input("> "))
	
showMenu(menuItems)

#{0: sys.exit(0),
# 1: function2,
# 2: function3,
# 3: function4}[showMenu(menuItems)]()