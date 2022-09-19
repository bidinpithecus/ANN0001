from weakref import ProxyTypes
import numpy as np

def poly(x,y):
	n = len(x)-1
	A =[]
	B =[]
	for xi in x:
		row = [1]
		for j in range(1, n+1):
			row.append(xi ** j)
		A.append(row)
	return np.linalg.solve(A, y)

def func_poly(x, coeffs):
	first=coeffs[0]
	return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])

if __name__ == '__main__':
	#exemplo 1

	x = [0.354, 0.786, 1.619, 2.149, 2.731, 3.311, 3.694, 4.51, 5.111, 5.451, 6.323, 6.553]
	y = [4.342, 4.687, 4.911, 4.684, 4.151, 3.466, 3.02, 2.342, 2.208, 2.27, 2.707, 2.835]

	coeffs = poly(x,y)
	#print(coeffs)

	for x in (coeffs):
		print("%.16f," %x)
	def p(x):
		return func_poly(x,coeffs)
