from methods import *

x = [0.3279, 1.6466, 1.872, 3.3111, 3.4577, 4.4676, 5.4022, 6.568, 6.77, 7.9654, 8.4088, 9.6938]
y = [5.336, 4.4452, 4.3651, 3.8293, 3.8644, 3.742, 3.9001, 4.218, 4.368, 5.1651, 5.3744, 6.4682]
values = [0.4381, 3.0434, 4.8611]

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 2)
a0 = listPol[0]
a1 = listPol[1]
a2 = listPol[2]
# print(f'{a0}, {a1}, {a2}', end=', ')
print('Coefs:\n',f'{a0}, {a1}, {a2}', end=',')

def p(x, a0, a1, a2):
	return a0 + a1 * x + a2 * pow(x, 2)
print()
print('Values:')
for value in values:
    print(f'{p(value, a0, a1, a2)}', end=", ")
print("")
# Ordem: Matriz A, Coefs, Matriz B, Values

print("\n\nPARA INSERIR\n")
print(*matrizA, sep=", ", end=", ")
print(f'{a0}, {a1}, {a2}', end=', ')
print(*matrizB, sep=", ", end=", ")
for value in values:
    print(f'{p(value, a0, a1, a2)}', end=", ")
print("")