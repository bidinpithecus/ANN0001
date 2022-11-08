from methods import *
from math import *

x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
y = [1.36094, 0.98115, 0.80546, 0.70063, 0.62771, 0.57346, 0.53173, 0.49776, 0.46913, 0.44487, 0.42448, 0.40741, 0.39192, 0.37661]
values = [1.1, 4.1, 6.2]

#linearização, transformando x em sqrt(x)

for i in range(0, len(x)):
    x[i] = 1/sqrt(x[i])

for i in range(0, len(y)):
    y[i] = sqrt(y[i])

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1)
w, z = listPol

b = 1/w
a = z*b

print('Coefs:\n',f'{a}, {b}', end=',')

# c0 -> a
# k -> b
def p(x, a, b):
    return a * 1/(1 + 2 * b * pow(a, 2)*x)

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