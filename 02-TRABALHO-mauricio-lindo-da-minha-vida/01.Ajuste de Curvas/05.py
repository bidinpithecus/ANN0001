"""Encontre os coeficientes da cúbica
        p(x)=a0+a1x+a2x2+a3x3
que melhor se aproxima da seguinte lista de 11 pontos
(-4.3409,5.3212), (-3.4063,6.4943), (-2.6361,6.4147), (-1.9,6.2777), (-0.5359,5.4594), (0.2306,4.9871), (1.3097,4.0469), (1.8035,3.7699), (3.1605,3.9073), (3.9612,4.5071) e (4.2958,5.6698)
Em seguida, calcule p(x) para os seguintes valores de x:
        x=-3.1568, x=-2.9451  e  x=3.7051"""

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

def f(a0,a1,a2,a3,x):
    #a0+a1x+a2x2+a3x3
    return a0+a1*x+a2*x**2+a3*x**3 #mudar se necessario

if __name__ == '__main__':
    x = [-4.3409, -3.4063, -2.6361, -1.9, -0.5359, 0.2306, 1.3097, 1.8035, 3.1605, 3.9612, 4.2958]
    y = [5.3212, 6.4943, 6.4147, 6.2777, 5.4594, 4.9871, 4.0469, 3.7699, 3.9073, 4.5071, 5.6698]
    values = [-3.1568, -2.9451, 3.7051]
    z = []

    a0, a1, a2, a3 = best_poly(x, y, 3) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',') #cuidado com a quantidade de variaveis, se é 1, 2, 3...

    for i in x:
        z.append(f(a0,a1,a2,a3, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')