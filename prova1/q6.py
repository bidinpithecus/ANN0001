from methods import *

def p(x):
	return func_poly(x,coeffs)

if __name__ == '__main__':
	x = [-3.758, -2.609, -1.886, -0.889, 0.191, 0.755, 2.017, 2.438, 3.621]
	y = [4.19, 3.596, 0.025, 2.434, 3.935, 3.453, 1.493, 2.682, 3.782]
	values = [-2.907, -2.602, -2.471, -0.396]

	coeffs = poly(x,y)

	for value in values:
		print('{:.16f},'.format(p(value)), end=" ")
	print()
