import RekursionIteration as rek
import math

print("\nBounce(4):")
rek.bounce(4)
print("\nBounce2(4):")
rek.bounce2(4)
print()
print('Sum(15120) =', rek.tvarsumman(15120))
print()
print('Sum2(15120) =', rek.tvarsumman2(15120))
print()
print('Derivative(x^2 - 1, math.pi, 0.0001) =', rek.derivative(rek.testFunction, math.pi, 0.0001))
print()
print('Solve(x^2 - 1, -2, 0.0001) =', rek.solve(rek.testFunction, -2, 0.0001))
print()
print('Solve(x^2 - 1, 0, 0.0001) =', rek.solve(rek.testFunction, 0, 0.0001))
