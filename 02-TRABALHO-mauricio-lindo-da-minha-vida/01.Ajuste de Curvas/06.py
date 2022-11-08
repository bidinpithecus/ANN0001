"""Encontre os coeficientes da cúbica
    p(x)=a0+a1x+a2x2+a3x3
que melhor se aproxima da seguinte lista de 34 pontos
(−4.9803,2.8768), (−4.5431,4.5737), (−4.2521,4.9561), (−4.0482,3.8087), (−3.6883,5.9122), (−3.4618,6.1659), (−3.1274,5.8711), (−2.7426,6.6049), (−2.4166,6.8023), (−2.091,7.3901), (−1.8909,6.8149), (−1.641,6.775), (−1.2746,6.3489), (−1.1396,6.6663), (−0.6413,6.1838), (−0.3843,5.8823), (−0.0532,5.6921), (0.2379,5.6433), (0.4283,6.5114), (0.8747,5.2889), (1.0156,6.1613), (1.4507,4.5542), (1.5895,4.9008), (1.8031,4.8695), (2.3481,4.9848), (2.5963,4.7018), (2.8075,4.5103), (2.9737,5.0365), (3.3063,5.4574), (3.7824,5.7829), (3.9756,5.812), (4.328,6.1088), (4.5068,6.8196) e (4.8449,7.8316)
Em seguida, calcule p(x) para os seguintes valores de x:
    x=−2.0397, x=−0.2584, x=2.2973, x=2.9408  e  x=3.5122"""

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
    x = [-4.9803, -4.5431, -4.2521, -4.0482, -3.6883, -3.4618, -3.1274, -2.7426, -2.4166, -2.091, -1.8909, -1.641, -1.2746, -1.1396, -0.6413, -0.3843, -0.0532, 0.2379, 0.4283, 0.8747, 1.0156, 1.4507, 1.5895, 1.8031, 2.3481, 2.5963, 2.8075, 2.9737, 3.3063, 3.7824, 3.9756, 4.328, 4.5068, 4.8449]
    y = [2.8768, 4.5737, 4.9561, 3.8087, 5.9122, 6.1659, 5.8711, 6.6049, 6.8023, 7.3901, 6.8149, 6.775, 6.3489, 6.6663, 6.1838, 5.8823, 5.6921, 5.6433, 6.5114, 5.2889, 6.1613, 4.5542, 4.9008, 4.8695, 4.9848, 4.7018, 4.5103, 5.0365, 5.4574, 5.7829, 5.812, 6.1088, 6.8196, 7.8316]
    values = [-2.0397, -0.2584, 2.2973, 2.9408, 3.5122]

    z = []

    a0, a1, a2, a3 = best_poly(x, y, 3) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',') #cuidado com a quantidade de variaveis, se é a1, a2, a3...

    for i in x:
        z.append(f(a0,a1,a2,a3, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')