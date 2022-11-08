import numpy as np
import math

'''
Encontre os coeficientes a e b da função y=axe^bx que melhor se aproxima da seguinte lista de 12 pontos
(0.8185,2.6099)...
'''
def best_line(x, y, grau=1):
    n = len(x)
    # soma das coordenadas x
    sum_x = sum(x)
    # soma das coordenadas x**2
    sum_x2 = sum(xi ** 2 for xi in x)
    # soma das coordenadas y
    sum_y = sum(y)
    #soma das coordenadas x*y
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    # Matriz dos coeficientes
    A = [[n, sum_x], [sum_x, sum_x2]]
    # Matriz dos termos independentes
    B = [sum_y, sum_xy]

    return np.linalg.solve(A, B)

def poly(x, a, b):
    return a*x*np.e**(b*x)
    # return a * (x/(x+b))
    # funcaomath.pow(x,b)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [0.2825, 0.5187, 0.746, 0.9893, 1.1464, 1.3235, 1.5514, 1.9924, 2.044, 2.259, 2.7056, 2.802, 3.0005, 3.1835, 3.4445, 3.7658, 4.0677, 4.3021, 4.5687, 4.6837, 5.0469, 5.1985, 5.3133, 5.7456, 5.9201, 6.1608, 6.4076, 6.5148, 6.9139, 7.1581, 7.2128, 7.46, 7.7978, 8.0091, 8.2583, 8.4578, 8.6507, 9.0137, 9.2554, 9.4681, 9.599, 9.8838]
    y = [0.9078, 1.4848, 1.8428, 2.1705, 2.3646, 2.5034, 2.6637, 2.7856, 2.7494, 2.7471, 2.6964, 2.6416, 2.585, 2.5394, 2.4834, 2.2959, 2.1252, 2.0246, 1.927, 1.8646, 1.672, 1.6159, 1.6192, 1.4164, 1.3433, 1.2344, 1.1265, 1.116, 0.9721, 0.9173, 0.8856, 0.9128, 0.7414, 0.8433, 0.6379, 0.5952, 0.559, 0.5676, 0.6208, 0.4066, 0.3938, 0.3761]
    values = [4.252, 5.0277, 5.8599, 6.7901, 6.8147]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(np.divide(y,x))

    xt = [xi + k2 for xi in x]

    x_ = x
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = np.exp(a0)

    b = a1

    print('Coeficientes da reta')
    print(f'{a0 = } e {a1 = }')

    print('Coeficientes')
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px = }')

    # visualização

""" import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt)

    plt.savefig('best_poly_regressao_potencia.png')
    """