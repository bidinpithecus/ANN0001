from methods import *

def p(x):
	return func_poly(x,coeffs)

if __name__ == '__main__':
	x = [0.351, 0.721, 1.062, 1.561, 2.145, 2.273, 2.89, 3.416, 3.645]
	y = [0.696, 1.085, 1.483, 1.935, 1.745, 1.53, 0.14, 0.566, 1.352]
	values = [0.31, 1.032, 2.675, 3.596]

	coeffs = poly(x,y)

	for value in values:
		print('{:.16f},'.format(p(value)), end=" ")
	print()
