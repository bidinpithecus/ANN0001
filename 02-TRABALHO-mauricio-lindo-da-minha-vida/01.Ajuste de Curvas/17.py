import numpy as np
import math


'''
Encontre os coeficientes a e b da função taxa de crescimento da saturação y=a(x/(x+b) que melhor se aproxima da seguinte lista de 12 pontos
(2.106,0.8735)...
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
    return a * (x/(x+b))
    # funcaomath.pow(x,b)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp

if __name__ == '__main__':
    x = [1.0781, 1.8312, 2.0517, 2.6368, 2.8194, 3.5217, 4.0923, 4.2111, 4.8726, 5.4915, 5.7438, 6.2387, 6.523, 7.2106, 7.7673, 7.8682, 8.3785, 9.1158, 9.515, 9.7996, 10.1893, 10.9462, 11.1972, 11.4438, 12.2358, 12.6819, 12.9424, 13.6046, 13.9932, 14.1803, 14.9287, 15.3604, 15.8671, 16.0922, 16.7095, 17.1871, 17.7012, 17.8319, 18.4151, 18.7948, 19.4209, 19.7874]
    y = [0.6049, 0.8958, 0.977, 1.1348, 1.1529, 1.3206, 1.4019, 1.4731, 1.5253, 1.5848, 1.6092, 1.6673, 1.696, 1.7337, 1.7865, 1.8406, 1.8375, 1.8883, 1.9418, 1.9213, 1.9415, 1.938, 2.0088, 1.9981, 1.9608, 2.1049, 2.1071, 2.1036, 2.0907, 2.1439, 2.1589, 2.1643, 2.1648, 2.087, 2.1697, 2.1929, 2.2127, 2.2265, 2.2469, 2.2261, 2.3407, 2.2508]
    values = [3.8015, 6.1765, 11.8327, 16.9504, 18.8275]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = (np.divide(1,y))

    xt = [xi + k2 for xi in x]

    x_ = np.divide(1,x)
    grau = 1

    a0, a1 = best_line(x_, y_, grau)

    a = 1/a0

    b = a1/a0
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

''' import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt)

    plt.savefig('best_poly_regressao_potencia.png')
    '''