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
	first = coeffs[0]
	return first + sum([ai * x ** j for j, ai in enumerate(coeffs[1:], 1)])


def lagrange(x,y):
	num = len(x)
	coefs = []
	for i in range(num):
		prod = 1
		for j in range(num):
			if i != j:
				prod *= (x[i] - x[j])
		ci = y[i] / prod
		coefs.append(ci)
	return coefs

def divDiff(x, y):
	num = len(x)
	Y = [yi for yi in y]
	coefs = [y[0]]
	for j in range(num -1):
		for i in range(num - 1 - j):
			numerador = Y[i + 1] - Y[i]
			denominador = x[i + 1 + j] - x[i]
			div = numerador / denominador
			Y[i] = div
		coefs.append(Y[0])
	return coefs

def polyDiff(t, x, coefs):
	val = 0
	num = len(coefs)
	for i in range(num):
		prod = 1
		for j in range(i):
				prod *= (t - x[j])
		val += coefs[i] * prod
	return val

def spline(x, y):
	n = len(x)
	a = {k: v for k, v in enumerate(y)}
	h = {k: x[k + 1] - x[k] for k in range(n - 1)}

	A = [[1] + [0] * (n - 1)]
	for i in range(1, n - 1):
		row = [0] * n
		row[i - 1] = h[i - 1]
		row[i] = 2 * (h[i - 1] + h[i])
		row[i + 1] = h[i]
		A.append(row)
	A.append([0] * (n - 1) + [1])

	B = [0]
	for k in range(1, n - 1):
		row = 3 * (a[k + 1] - a[k]) / h[k] - 3 * (a[k] - a[k - 1]) / h[k - 1]
		B.append(row)
	B.append(0)

	c = dict(zip(range(n), np.linalg.solve(A, B)))

	b = {}
	d = {}
	for k in range(n - 1):
		b[k] = (1 / h[k]) * (a[k + 1] - a[k]) - (h[k] / 3) * (2 * c[k] + c[k + 1])
		d[k] = (c[k + 1] - c[k]) / (3 * h[k])

	s = {}
	for k in range(n - 1):
		print('{:.16},{:.16},{:.16},{:.16},'.format(a[k], b[k], c[k], d[k]))
		eq = f'{a[k]}{b[k]:+}*(x{-x[k]:+}){c[k]:+}*(x{-x[k]:+})**2{d[k]:+}*(x{-x[k]:+})**3'
		s[k] = {'eq': eq, 'domain': [x[k], x[k + 1]]}

	return s
