"""Encontre os coeficientes da reta
            p(x)=a0+a1x
que melhor se aproxima da seguinte lista de 12 pontos
    (0.7064,4.1678), (1.3923,6.563), (2.4829,9.7186), (3.0716,11.0116), (3.8615,13.5959), (4.6128,15.2451), (5.2869,18.5277), (5.9634,19.5883), (6.859,22.2843), (8.0048,25.5162), (8.8814,27.997) e (9.3609,29.2071)
    Em seguida, calcule p(x) para os seguintes valores de x:
    x=3.7086, x=5.2767  e  x=5.4068*"""

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
    x = [0.7064, 1.3923, 2.4829, 3.0716, 3.8615, 4.6128, 5.2869, 5.9634, 6.859, 8.0048, 8.8814, 9.3609]
    y = [4.1678, 6.563, 9.7186, 11.0116, 13.5959, 15.2451, 18.5277, 19.5883, 22.2843, 25.5162, 27.997, 29.2071]
    values = [3.7086, 5.2767, 5.4068]
    z = []

    a0, a1 = linear(x,y)
    
    print(a0, ',', a1,',')

    for i in x:
        z.append(f(a0, a1, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')