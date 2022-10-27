from methods import *
from math import *

x = [1.0239, 2.0746, 2.9553, 4.3378, 4.8023, 5.6899, 7.3994, 7.9593, 8.446, 9.7079, 11.0359, 11.0924]
y = [0.3181, 0.9484, 1.6268, 2.1008, 2.1757, 2.3783, 2.7092, 2.7163, 2.7981, 2.7993, 2.9143, 2.9095]
values = [3.856, 4.6653, 5.2024]

#linearização, transformando y em 1/y e x em 1/x**2
for i in range(0, len(y)):
    y[i] = 1/y[i]

for i in range(0, len(x)):
    x[i] = pow(1/x[i],2)

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1)
z, w = listPol

a = 1/z # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)
b = a * w

print('Coefs:\n',f'{a}, {b}', end=', ')

def p(x, a, b):
	return a * (x**2/(x**2+b))

print()
print('Values:')
for value in values:
    print(f' {(p(value, a, b))}', end=", ")
print("")
print("\n\nPARA INSERIR\n")
print(f'{a}, {b}', end=', ')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")