"""Encontre os coeficientes da parábola
        p(x)=a0+a1x+a2x2
que melhor se aproxima da seguinte lista de 14 pontos
(0.5214,4.8497), (0.9699,4.5825), (1.5672,4.1897), (2.4802,3.8022), (3.508,3.5953), (3.7891,3.5712), (4.3322,3.4629), (5.4911,3.6128), (5.7468,3.6383), (7.1001,4.0907), (7.4395,4.2607), (8.4192,4.9239), (9.0073,5.3796) e (9.3096,5.8089)
Em seguida, calcule p(x) para os seguintes valores de x:
x=6.7293, x=7.6609  e  x=8.1986"""

import numpy as np
import math

def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinônmio)')

    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    return np.linalg.solve(A, B)



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

def f(a0,a1,a2,x):
    return a0+a1*x+a2*math.pow(x,2) #mudar se necessario

if __name__ == '__main__':
    x = [0.5214, 0.9699, 1.5672, 2.4802, 3.508, 3.7891, 4.3322, 5.4911, 5.7468, 7.1001, 7.4395, 8.4192, 9.0073, 9.3096]
    y = [4.8497, 4.5825, 4.1897, 3.8022, 3.5953, 3.5712, 3.4629, 3.6128, 3.6383, 4.0907, 4.2607, 4.9239, 5.3796, 5.8089]
    values = [6.7293, 7.6609, 8.1986]
    z = []

    a0, a1, a2 = best_poly(x, y, 2)
    
    print(a0, ',', a1,',',a2,',') #cuidado com a quantidade de variaveis, se é 1, 2, 3...

    for i in x:
        z.append(f(a0,a1,a2, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')