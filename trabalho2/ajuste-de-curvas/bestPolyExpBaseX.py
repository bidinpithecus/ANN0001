from methods import *
from math import *

x = [0.2104, 1.3175, 2.2366, 2.7225, 3.6843, 4.9469, 5.1212, 6.2407, 6.9498, 7.6988, 9.0564, 9.2345]
y = [0.7893, 3.1008, 3.711, 3.781, 3.6384, 3.0637, 2.9958, 2.429, 2.0694, 1.7435, 1.255, 1.205]
values = [0.8096, 2.5419, 8.428]

#linearização, transformando y em ln(y) e x em ln(x)
for i in range(0, len(y)):
    y[i] = log(y[i])

for i in range(0, len(x)):
    x[i] = log(x[i])

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1) 
z, b = listPol

a = exp(z) # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * pow(x, b)

print()
print('Values:\n')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")

print("\n\nPARA INSERIR\n")
print(f'{a}, {b}', end=', ')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")