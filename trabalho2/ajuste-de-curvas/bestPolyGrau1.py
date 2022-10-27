from methods import *

x = [0.1982, 0.4423, 0.696, 1.2048, 1.418, 1.7692, 2.1868, 2.4281, 2.6981, 3.1103, 3.4145, 3.5446, 3.9798, 4.162, 4.5053, 4.9234, 5.1947, 5.5445, 5.9041, 5.9673, 6.5407, 6.8057, 7.0156, 7.305, 7.5103, 7.8987, 8.1441, 8.6753, 8.8228, 9.2908, 9.3755, 9.9407]
y = [1.4325, 1.6655, 2.1765, 2.543, 2.5429, 3.121, 3.8182, 3.9357, 4.3599, 4.8685, 5.1814, 5.3526, 5.9826, 5.8645, 6.3769, 6.9866, 6.4143, 7.5661, 8.0674, 8.1365, 8.9033, 9.0341, 9.3387, 9.6726, 9.8669, 11.2337, 10.8151, 11.3808, 11.4024, 12.1523, 12.2678, 12.8957]
values = [1.6193, 4.4528, 5.0659, 5.7751, 8.0083]

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1)
a0 = listPol[0]
a1 = listPol[1]
# print(f'{a0}, {a1}', end=', ')
print('Coefs:\n',f'{a0}, {a1}', end=',')

def p(x, a0, a1):
	return a0 + a1 * x
print()
print('Values:')
for value in values:
    print(f'{p(value, a0, a1)}', end=", ")
print("")
# Ordem: Matriz A, Coefs, Matriz B, Values

print("\n\nPARA INSERIR\n")
print(*matrizA, sep=", ", end=", ")
print(f'{a0}, {a1}', end=', ')
print(*matrizB, sep=", ", end=", ")
for value in values:
    print(f'{p(value, a0, a1)}', end=", ")
print("")