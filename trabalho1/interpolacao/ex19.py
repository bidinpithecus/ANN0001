from methods import *
import math

def s(x):
	for key, value in eqs.items():
		if value['domain'][0] <= x <= value['domain'][1]:
			return eval(value['eq'])

if __name__ == '__main__':
	x = [0.328, 0.871, 1.233, 1.809, 2.52, 3.197, 3.9, 4.591, 5.185, 5.771, 5.948, 6.895]
	y = [5.23, 4.54, 4.525, 3.128, 2.203, 2.602, 2.351, 3.296, 3.65, 4.399, 4.933, 4.115]
	valores = [1.037, 2.658, 4.948, 6.224, 6.725]

	eqs = spline(x, y)

	for valor in valores:
		print('{:.16f},'.format(s(valor)), end=" ")
	print()