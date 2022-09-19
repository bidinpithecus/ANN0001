from methods import *

if __name__ == '__main__':
	x = [0.53, 1.95, 3.381]
	y = [0.868, 1.946, 0.462]

	cs = lagrange(x,y)

	for c in cs:
		print('{:.16f},'.format(c), end=" ")
	print()