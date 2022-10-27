from methods import *

x = [-4.9151, -4.6292, -4.261, -3.9789, -3.6592, -3.4168, -3.2289, -2.7008, -2.5359, -2.2079, -1.8856, -1.7017, -1.1893, -1.0149, -0.6102, -0.4085, -0.1258, 0.0794, 0.5601, 0.873, 1.0594, 1.1771, 1.5423, 1.8957, 2.2377, 2.5815, 2.7751, 3.2212, 3.3797, 3.5397, 4.0877, 4.3234, 4.6216, 4.9574]
y = [3.2319, 3.8891, 4.6739, 5.2627, 5.4062, 5.3477, 6.024, 6.4449, 6.1176, 6.3213, 6.3316, 6.0677, 5.6222, 5.4178, 5.141, 4.9991, 4.9753, 4.6386, 4.031, 3.1303, 3.2675, 3.1119, 3.0064, 2.6804, 2.6333, 2.6024, 2.5582, 2.7378, 2.909, 3.097, 3.1198, 4.3957, 5.0394, 7.0543]
values = [-4.6677, -3.6264, -1.5035, 2.8415, 4.5424]

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 3)
a0 = listPol[0]
a1 = listPol[1]
a2 = listPol[2]
a3 = listPol[3]
print('Coefs:\n', f'{a0}, {a1}, {a2}, {a3}', end=',')

def p(x, a0, a1, a2, a3):
	return a0 + a1 * x + a2 * pow(x, 2) + a3 * pow(x, 3)

print()
print('Values:')
for value in values:
    print(f'{p(value, a0, a1, a2, a3)}', end=", ")
print("")
# Ordem: Matriz A, Coefs, Matriz B, Values

print("\n\nPARA INSERIR\n")
print(*matrizA, sep=", ", end=", ")
print(f'{a0}, {a1}, {a2}, {a3}', end=', ')
print(*matrizB, sep=", ", end=", ")
for value in values:
    print(f'{p(value, a0, a1, a2, a3)}', end=", ")
print("")