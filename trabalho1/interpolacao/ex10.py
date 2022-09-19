from methods import *
import math


def f(x):
	# return math.exp(math.cos(x)**2) + math.exp(-x**2) + math.log(x) # Questão a
	# return 4 + math.sin(x) - x**2 / 30 # Questão b
	return math.exp(-x**2)+math.cos(x)+3 # Questão c

if __name__ == '__main__':
	x = [0.326, 0.826, 1.335, 2.085, 2.513, 2.756, 3.595, 3.875, 4.364, 5.309, 5.52, 5.987, 6.656]
	y = []

	for i in x:
		y.append(f(i))

	cs = lagrange(x,y)

	for c in cs:
		print('{:.16f},'.format(c), end=" ")
	print()