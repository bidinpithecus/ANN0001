"""Encontre os coeficientes da reta
            p(x)=a0+a1x
que melhor se aproxima da seguinte lista de 32 pontos
(0.2546,2.8356), (0.3353,2.9623), (0.7622,3.5339), (0.9622,3.879), (1.468,4.2861), (1.6996,4.9079), (2.1777,5.9086), (2.4461,5.8112), (2.725,6.0436), (2.8418,6.1973), (3.1693,6.6387), (3.5006,7.1383), (3.9663,8.1136), (4.2153,7.9829), (4.4435,8.2739), (4.7779,8.984), (5.2763,8.9839), (5.6217,9.9275), (5.6802,9.9008), (6.1081,10.4479), (6.3065,10.6848), (6.6898,11.6681), (7.1006,11.8002), (7.2881,11.884), (7.5019,12.1178), (7.9556,12.7062), (8.4169,13.5418), (8.6543,14.1933), (8.7964,13.7848), (9.2063,14.3995), (9.4889,14.7255) e (9.8509,15.7955)
    Em seguida, calcule p(x) para os seguintes valores de x:
x=1.6169, x=3.245, x=3.3568, x=7.1247  e  x=7.4396"""

from ctypes import sizeof
import numpy as np

def linear(x,y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi**2 for xi in x)
    A = [
        [n,sum_x],
        [sum_x,sum_x2]
    ]
    sum_y = sum(y)
    sum_yx = sum(yi*xi for yi,xi in zip(y,x))
    B = [
        sum_y,
        sum_yx
    ]
    return np.linalg.solve(A,B)

def f(a0,a1,x):
    return a0 + a1 * x #mudar se necessario


def poly(x, y):
    n = len(x) - 1
    A = []
    for xi in x:
        row = [1]
        for j in range(1, n + 1):
            row.append(xi**j)
        A.append(row)
    return np.linalg.solve(A, y)


def p(x, coefs):
    first = coefs[0]
    return first + sum([ai*x**j for j, ai in enumerate(coefs[1:], 1)])


if __name__ == '__main__':
    x = [0.2546, 0.3353, 0.7622, 0.9622, 1.468, 1.6996, 2.1777, 2.4461, 2.725, 2.8418, 3.1693, 3.5006, 3.9663, 4.2153, 4.4435, 4.7779, 5.2763, 5.6217, 5.6802, 6.1081, 6.3065, 6.6898, 7.1006, 7.2881, 7.5019, 7.9556, 8.4169, 8.6543, 8.7964, 9.2063, 9.4889, 9.8509]
    y = [2.8356, 2.9623, 3.5339, 3.879, 4.2861, 4.9079, 5.9086, 5.8112, 6.0436, 6.1973, 6.6387, 7.1383, 8.1136, 7.9829, 8.2739, 8.984, 8.9839, 9.9275, 9.9008, 10.4479, 10.6848, 11.6681, 11.8002, 11.884, 12.1178, 12.7062, 13.5418, 14.1933, 13.7848, 14.3995, 14.7255, 15.7955]
    values = [1.6169, 3.245, 3.3568, 7.1247, 7.4396]
    z = []

    a0, a1 = linear(x,y)
    
    print(a0, ',', a1,',')

    for i in x:
        z.append(f(a0, a1, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')