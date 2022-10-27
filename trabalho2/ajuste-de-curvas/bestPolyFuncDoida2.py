from methods import *
from math import *

x = [1.0334, 1.3073, 2.2383, 3.2322, 4.2848, 4.655, 5.8296, 6.4036, 6.9149, 8.3332, 8.6803, 9.4491]
y = [7.0445, 5.9126, 3.9788, 3.0567, 2.6371, 2.5486, 2.1543, 1.9902, 2.0392, 1.8085, 1.6938, 1.6318]
values = [1.5901, 2.7127, 3.1026]

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

def p(x, a, b):
	return pow((a+sqrt(x))/(b*sqrt(x)),2)


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