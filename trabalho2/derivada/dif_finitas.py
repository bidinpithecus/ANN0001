from methods import *

def f(x):
    return x**2 * math.exp(-x) * math.cos(x) + 1

k = 5 # ordem da derivada
n = 15 # número de pontos
x0 = 4.868
x = [4.6397, 4.6701, 4.6967, 4.7319, 4.7523, 4.7931, 4.8512, 4.8795, 4.8884, 4.9473, 4.9748, 4.9881, 5.0414, 5.0658, 5.1137]

y = [f(xi) for xi in x]

coeffs = coeffs_dif_fin(x0, x, k)
aprox = dif_fin(coeffs, y)

print(f'{coeffs}')
print(f'{aprox}')