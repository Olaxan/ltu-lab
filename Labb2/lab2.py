import recursion as rec
import math


print("\nBounce(4):")
rec.bounce(4)
print("\nBounce2(4):")
rec.bounce2(4)
print()
print('Sum(15120) =', rec.tvarsumman(15120))
print()
print('Sum2(15120) =', rec.tvarsumman2(15120))
print()
print('Derivative(x^2 - 1, math.pi, 0.0001) =', rec.derivative(rec.testFunction, math.pi, 0.0001))
print()
print('Solve(x^2 - 1, -2, 0.0001) =', rec.solve(rec.testFunction, -2, 0.0001))
print()
print('Solve(x^2 - 1, 0, 0.0001) =', rec.solve(rec.testFunction, 0, 0.0001))
