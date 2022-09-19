from methods import *

if __name__ == '__main__':
	x = [2.791, 2.924, 3.22, 3.494, 3.696, 3.93, 4.212, 4.387]
	y = [0.715, 0.772, 0.862, 0.921, 0.956, 0.988, 0.994, 0.913]

	cs = lagrange(x,y)

	for c in cs:
		print('{:.16f},'.format(c), end=" ")
	print()