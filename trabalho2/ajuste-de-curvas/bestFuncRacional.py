from methods import *
from math import *

x = [1.0608, 1.7852, 2.1319, 2.4694, 2.9343, 3.5648, 3.8755, 4.358, 4.8227, 5.3326, 5.93, 6.2598, 6.5667, 7.1936, 7.5015, 8.2379, 8.6131, 8.8952, 9.3207, 10.0004, 10.4809, 10.846, 11.3269, 11.5456, 12.1983, 12.5663, 12.9926, 13.5257, 13.7266, 14.2521, 14.7296, 15.4732, 15.6962, 16.1851, 16.4969, 17.1637, 17.6629, 17.9992, 18.3377, 18.9614, 19.3044, 19.9437]
y = [1.1546, 1.7311, 1.9323, 2.055, 2.2679, 2.5339, 2.6038, 2.7039, 2.855, 2.9712, 3.0699, 3.1077, 3.1594, 3.2454, 3.3003, 3.4092, 3.4372, 3.4501, 3.4998, 3.5746, 3.6414, 3.6393, 3.7361, 3.7039, 3.7342, 3.7648, 3.8099, 3.8356, 3.8806, 3.8104, 3.8606, 3.8983, 3.9137, 3.953, 3.9533, 3.9594, 3.9777, 3.9876, 4.045, 4.0383, 4.0554, 4.0728]
values = [5.7544, 7.1984, 10.1871, 13.9802, 16.05]

#linearização, transformando y em 1/y e x em 1/x
for i in range(0, len(y)):
    y[i] = 1/y[i]

for i in range(0, len(x)):
    x[i] = 1/x[i]

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1)
z, w = listPol

a = 1/z # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)
b = a * w
print('Coefs:\n',f'{a}, {b}', end=', ')

def p(x, a, b):
	return a * (x/(x+b))

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