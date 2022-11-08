"""Encontre os coeficientes do polinômio de grau 5
    p(x)=a0+a1x+a2x2+a3x3+a4x4+a5x5
que melhor se aproxima da seguinte lista de 41 pontos
(−4.3929,−3.9203), (−4.1223,−1.2143), (−3.9842,−0.2167), (−3.8212,0.312), (−3.4309,2.9508), (−3.2041,2.2278), (−3.1505,2.171), (−2.878,1.6819), (−2.5818,1.3871), (−2.4781,0.8082), (−2.1317,−0.7085), (−2.0052,0.087), (−1.7134,−0.2822), (−1.5571,−0.8963), (−1.2188,−0.6741), (−1.0109,−0.7167), (−0.8693,−0.6959), (−0.7269,−0.5353), (−0.3605,−0.5241), (−0.1158,−0.0925), (−0.04,−0.0432), (0.3285,0.513), (0.3485,0.333), (0.6673,0.6511), (0.9559,0.9799), (1.1838,1.0884), (1.2594,0.9756), (1.6323,0.5102), (1.6705,0.7575), (2.0398,0.1408), (2.2986,0.3369), (2.5218,−1.5442), (2.688,−2.5904), (2.78,−1.0592), (3.0102,−1.9569), (3.2074,−2.065), (3.4105,−3.2242), (3.6498,−1.431), (3.8785,−1.0431), (4.1274,2.0409) e (4.3616,4.5214)
Em seguida, calcule p(x) para os seguintes valores de x:
    x=−3.5521, x=−3.3737, x=0.4938, x=0.5037  e  x=2.0214
"""

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

def f(a0,a1,a2,a3,a4,a5,x):
    #a0+a1x+a2x2+a3x3
    return a0+a1*x+a2*x**2+a3*x**3+a4*x**4+a5*x**5

if __name__ == '__main__':
    x = [-4.3929, -4.1223, -3.9842, -3.8212, -3.4309, -3.2041, -3.1505, -2.878, -2.5818, -2.4781, -2.1317, -2.0052, -1.7134, -1.5571, -1.2188, -1.0109, -0.8693, -0.7269, -0.3605, -0.1158, -0.04, 0.3285, 0.3485, 0.6673, 0.9559, 1.1838, 1.2594, 1.6323, 1.6705, 2.0398, 2.2986, 2.5218, 2.688, 2.78, 3.0102, 3.2074, 3.4105, 3.6498, 3.8785, 4.1274, 4.3616]
    y = [-3.9203, -1.2143, -0.2167, 0.312, 2.9508, 2.2278, 2.171, 1.6819, 1.3871, 0.8082, -0.7085, 0.087, -0.2822, -0.8963, -0.6741, -0.7167, -0.6959, -0.5353, -0.5241, -0.0925, -0.0432, 0.513, 0.333, 0.6511, 0.9799, 1.0884, 0.9756, 0.5102, 0.7575, 0.1408, 0.3369, -1.5442, -2.5904, -1.0592, -1.9569, -2.065, -3.2242, -1.431, -1.0431, 2.0409, 4.5214]
    values = [-3.5521, -3.3737, 0.4938, 0.5037, 2.0214]
    z = []

    a0, a1, a2, a3, a4, a5 = best_poly(x, y, 5) #3 é o grau da parabola
    
    print(a0,',', a1,',',a2,',',a3,',',a4,',',a5,',') #cuidado com a quantidade de variaveis, se é a1, a2, a3...

    for i in x:
        z.append(f(a0,a1,a2,a3,a4,a5, i)) #nao esqueça de colocar aqui tb

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')