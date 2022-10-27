from methods import *
from math import *

x = [0.1546, 0.2946, 0.4802, 0.6488, 0.67, 0.8669, 1.1372, 1.307, 1.3799, 1.6502, 1.6921, 1.97]
y = [6.1312, 8.9327, 9.7644, 10.3818, 12.7878, 17.3924, 26.1117, 36.4076, 38.7629, 59.9698, 65.9855, 98.5675]
values = [0.3871, 1.6101, 1.7071]

#linearização, transformando y em ln(y)
for i in range(0, len(y)):
    y[i] = log(y[i])

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1)
z, b = listPol

a = exp(z) # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)
print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * exp(b*x) 

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * pow(2, b*x) 

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