from methods import *
from math import *

x = [0.355, 0.4378, 0.6177, 0.9448, 1.2266, 1.4512, 1.6094, 1.8878, 2.1812, 2.2897, 2.5745, 2.7399, 3.1473, 3.2108, 3.5555, 3.8204, 4.0845, 4.3129, 4.4882, 4.6573, 5.006, 5.1112, 5.4514, 5.6573, 5.8449, 6.1195, 6.4471, 6.483, 6.8788, 7.0498, 7.2943, 7.5104, 7.7241, 8.0374, 8.3322, 8.4813, 8.7207, 8.8255, 9.1006, 9.4414, 9.7473, 9.8078]
y = [1.0825, 1.2935, 1.7025, 2.2717, 2.587, 2.7714, 2.9593, 3.0745, 3.1043, 3.145, 3.111, 3.1072, 3.0072, 3.0613, 2.8968, 2.7691, 2.6859, 2.6236, 2.4948, 2.416, 2.2574, 2.1618, 2.046, 1.9232, 1.8675, 1.7193, 1.6441, 1.5923, 1.4974, 1.3441, 1.2594, 1.225, 1.1461, 1.036, 1.0699, 0.9921, 0.9205, 0.8253, 0.7555, 0.7143, 0.6452, 0.6195]
values = [1.2503, 1.8574, 2.4107, 2.7464, 8.2743]

logxy = list()

#linearização, obtendo ln(y) - ln(x), isso é o que vai entrar no lugar de y no best_poly
for i in range(0, len(x)):
    logxy.append(log(y[i]) - log(x[i]))

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, logxy, 1) 
z, b = listPol

a = exp(z) # a função te retorna um valor z = ln(a), então isola a e obtém a = exp(z)

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * x * exp(b * x)

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