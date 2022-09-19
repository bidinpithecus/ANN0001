from methods import *
from math import sqrt

"""
# Questão 6) a
def f(x):
  return np.sin(sqrt(1+np.tan(x)))
"""

"""
# Questão 6) b
def f(x):
	return np.sin(x)**3- 3*np.sin(x)**2+np.sin(pow(x,2)) + 4
"""

"""
# Questão 6) c
def f(x):
  return (np.cos(x)**3)+(2*np.cos(x)**2)+1
"""

def p(x):
	return func_poly(x,coeffs)

if __name__ == '__main__':
	x = [-2.896, -1.733, -0.678, 0.236, 1.047, 1.653, 2.302, 2.953, 4.127]
	values = [-1.744, 0.822, 1.47, 3.277, 3.86]
	y = []

	for i in x:
		y.append(f(i))

	coeffs = poly(x,y)

	for value in values:
		print('{:.16f},'.format(abs(f(value) - p(value))), end=" ")
	print()
