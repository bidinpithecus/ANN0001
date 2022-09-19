from methods import *

if __name__ == '__main__':
	x = [1.664, 1.999, 2.675, 3.149, 3.647, 4.349, 4.916]
	y = [-0.892, -0.999, -0.593, -0.049, 0.517, 0.976, 0.914]

	coeffs = divDiff(x, y)

	for coeff in coeffs:
		print('{:.16f},'.format(coeff), end=" ")
	print()