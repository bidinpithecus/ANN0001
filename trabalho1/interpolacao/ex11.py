from methods import *

if __name__ == '__main__':
	x = [0.937, 1.436, 2.43]
	y = [0.992, 0.789, 0.558]

	coeffs = divDiff(x, y)

	for coeff in coeffs:
		print('{:.16f},'.format(coeff), end=" ")
	print()