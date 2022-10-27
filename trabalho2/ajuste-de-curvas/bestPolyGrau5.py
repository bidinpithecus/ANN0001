from methods import *

x = [-4.8568, -4.6023, -4.2036, -3.9069, -3.6427, -3.3514, -3.0213, -2.7124, -2.4317, -2.3362, -2.0717, -1.5885, -1.4456, -1.0623, -0.8508, -0.5595, -0.2347, -0.0505, 0.2125, 0.5523, 0.8279, 1.1916, 1.5372, 1.6807, 2.1033, 2.2407, 2.6046, 2.9636, 3.1707, 3.6232, 3.857, 4.2573, 4.303, 4.6956, 4.8568, 5.3819, 5.4657, 5.9888]
y = [-8.8505, -5.6419, -1.3934, 1.5237, 1.6811, 2.6073, 3.1209, 2.8981, 2.5185, 2.295, 2.2857, 1.3457, 2.6683, 0.3394, -0.1591, -0.6432, -1.0959, -1.0201, -2.3009, -0.6581, -0.4514, 0.7026, 1.2631, 1.4389, 2.8919, 4.9792, 3.6982, 5.2843, 5.5484, 5.9595, 5.8877, 5.4582, 4.9751, 2.8304, 1.394, -4.4493, -5.7757, -15.7836]
values = [-0.7341, 0.8064, 1.3862, 2.8152, 3.237]

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 5)
a0 = listPol[0]
a1 = listPol[1]
a2 = listPol[2]
a3 = listPol[3]
a4 = listPol[4]
a5 = listPol[5]
print('Coefs:\n', f'{a0}, {a1}, {a2}, {a3}, {a4}, {a5}', end=',')

def p(x, a0, a1, a2, a3, a4, a5):
	return a0 + a1 * x + a2 * pow(x, 2) + a3 * pow(x, 3) + a4 * pow(x, 4) + a5 * pow(x, 5)

print()
print('Values:')
for value in values:
    print(f'{p(value, a0, a1, a2, a3, a4, a5)}', end=", ")
print("")
# Ordem: Matriz A, Coefs, Matriz B, Values

print("\n\nPARA INSERIR\n")
print(*matrizA, sep=", ", end=", ")
print(f'{a0}, {a1}, {a2}, {a3}, {a4}, {a5}', end=', ')
print(*matrizB, sep=", ", end=", ")
for value in values:
    print(f'{p(value, a0, a1, a2, a3, a4, a5)}', end=", ")
print("")
