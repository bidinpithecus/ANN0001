from methods import *
from cmath import log
from math import sqrt,log,pow

"""
# Questão 4) a

def f(x):
  return np.sin(sqrt(1 + np.tan(x)))
"""

"""
# Questão 4) b

def f(x):
  return (np.cos(x)**3)+(2*np.cos(x)**2)+1
"""


# Questão 4) c

def f(x):
	return np.cos(x+sqrt(log(pow(x,2))))

if __name__ == '__main__':
	x = [1.599, 2.012, 2.106, 2.643, 2.957, 3.304, 3.494, 3.761, 4.092, 4.492, 4.717]
	y = []

	for i in x:
		y.append(f(i))

	np.set_printoptions(suppress=True)
	coefs = poly(x, y)

	for coef in coefs:
		print('{:.16f},'.format(coef), end=" ")
	print()