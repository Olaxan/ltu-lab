import recursion as rec
import utils
import sys

menuItems = [
	"Bounce", "Sum", "Solver"
	]

while True:
	result = utils.showMenu(menuItems)

	if (result == 0):
		break
	elif (result == 1):
		rec.bounce(utils.requestInt("Bounce: "))
	elif (result == 2):
		print(rec.tvarsumman(utils.requestInt("Letter sum: ")))
	elif (result == 3):
		print("x =", rec.solve(lambda x : x**2-1, utils.requestInt("Solver start: "), 0.0001))

	print()

