from methods import *
import math

def f(x):
	# return (1 / (1 + 25 * x**2))
	# return np.cos(x)**3 + 2*np.cos(x)**2 + 1
	return np.cos(x+math.sqrt(np.log(pow(x,2))))

if __name__ == '__main__':
	x = [1.479, 1.824, 2.03, 2.336, 2.402, 2.77, 2.971, 3.14, 3.484, 3.667, 3.846, 4.094, 4.339, 4.665, 4.935]
	y = []

	for i in x:
		y.append(f(i))

	coeffs = divDiff(x, y)

	for coeff in coeffs:
		print('{:.16f},'.format(coeff), end=" ")
	print()