from methods import *

if __name__ == '__main__':
	x = [2.373, 5.729, 8.387]
	y = [4.813, 4.415, 3.501, 2.525, 2.226, 2.0, 2.341, 2.857, 3.324, 3.77, 3.997, 3.933]

	cs = lagrange(x,y)

	for c in cs:
		print('{:.16f},'.format(c), end=" ")
	print()