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
		if valid and (1 - int(showExit)) <= user <= len(menuItems):
			return user
		else:
			title = "\nPlease select an item between "+str(1 - int(showExit))+"-"+str(len(menuItems))+"."

def requestInt(title, prompt = "> ", error = "\nPlease enter an integer.", exitChar = None):
	print(title)
	if (exitChar != None):
		print("Enter", exitChar, "to exit.")
	while True:
		user = input(prompt)
		valid, out = tryParse(user)
		if valid:
			if (user == exitChar):
				break
			return out
		else:
			print(error)

while True:
	print()
	result = showMenu(menuItems)

	if (result == 0):
		break
	elif (result == 1):
		rek.bounce(requestInt("Bounce: "))
	elif (result == 2):
		print(rek.tvarsumman(requestInt("Letter sum: ")))
	elif (result == 3):
		print("x =", rek.solve(lambda x : x**2-1, requestInt("Solver start: "), 0.0001))

