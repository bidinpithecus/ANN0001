import numpy as np
import math

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
    x = [1.0041, 1.6979, 2.0742, 2.6122, 2.6683, 3.3922, 3.4523, 3.8994, 4.2421, 4.8478, 5.2514, 5.5516, 6.248, 6.6281, 6.6804, 7.3728, 7.6759, 7.9695, 8.6532, 8.9341, 9.3407, 9.6143, 9.9415, 10.4458, 10.8092, 11.1578, 11.7531, 12.0719, 12.6339, 13.0969, 13.4209, 13.54, 14.0714, 14.403, 14.9898, 15.2505, 15.7099, 16.0653, 16.4971, 17.1136, 17.3754, 17.839, 18.083, 18.4803, 19.1875, 19.2891, 19.8727]
    y = [1.1356, 1.6097, 1.801, 2.0698, 2.0387, 2.2779, 2.286, 2.4231, 2.5195, 2.6261, 2.6748, 2.7205, 2.8286, 2.8571, 2.8643, 2.9712, 2.9952, 3.0024, 3.0344, 3.1094, 3.109, 3.1333, 3.1555, 3.1664, 3.2043, 3.2267, 3.2454, 3.2457, 3.2883, 3.326, 3.3328, 3.3015, 3.3453, 3.3618, 3.3991, 3.4125, 3.3605, 3.4043, 3.41, 3.3648, 3.4489, 3.4262, 3.4608, 3.4507, 3.4351, 3.4337, 3.4908]
    values = [10.8067, 13.6305, 15.6135, 18.403]
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
    print(f'{a0} e {a1}')

    print('Coeficientes')
    print(f'{a} e {b}')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    px = [p(vi) for vi in values]
    print(f'{px}')
