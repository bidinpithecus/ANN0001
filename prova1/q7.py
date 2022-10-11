from methods import *

def s(x):
	for key, value in eqs.items():
		if value['domain'][0] <= x <= value['domain'][1]:
			return eval(value['eq'])

if __name__ == '__main__':
		x = [-1.147, -0.136, 0.784, 1.532, 2.945, 4.476, 5.541, 6.016]
		y = [1.048, 1.973, 1.408, 1.24, 0.396, -0.932, -0.381, 0.593]
		valores = [-0.713, 2.929, 5.678]

		eqs = spline(x, y)

		for valor in valores:
			print('{:.16f},'.format(s(valor)), end=" ")
		print()