"""Encontre os coeficientes da parábola
        p(x)=a0+a1x+a2x2
que melhor se aproxima da seguinte lista de 36 pontos
    (0.0444,5.7912), (0.5041,5.4625), (0.7308,5.3431), (1.0678,4.9996), (1.2885,4.6561), (1.6037,4.7264), (1.6668,4.8078), (2.0258,4.5855), (2.3293,4.1601), (2.5123,4.1244), (2.9969,3.8997), (3.098,3.6425), (3.5293,3.6673), (3.625,3.6749), (4.1475,3.5592), (4.3702,3.5189), (4.4522,3.5053), (4.8559,3.5051), (5.204,3.3781), (5.5368,3.4576), (5.5739,3.3949), (5.8534,3.46), (6.2876,3.4834), (6.4591,3.5174), (6.8598,3.5598), (6.9878,3.5904), (7.2971,3.6523), (7.6468,3.6904), (8.0542,4.0192), (8.0733,4.0132), (8.5871,4.2154), (8.7104,4.315), (8.914,4.4469), (9.2396,4.6732), (9.7179,5.2456) e (9.7989,5.3356)
Em seguida, calcule p(x) para os seguintes valores de x:
    x=0.2248, x=3.9807, x=4.2423, x=8.6162  e  x=9.664"""

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
    x = [0.0444, 0.5041, 0.7308, 1.0678, 1.2885, 1.6037, 1.6668, 2.0258, 2.3293, 2.5123, 2.9969, 3.098, 3.5293, 3.625, 4.1475, 4.3702, 4.4522, 4.8559, 5.204, 5.5368, 5.5739, 5.8534, 6.2876, 6.4591, 6.8598, 6.9878, 7.2971, 7.6468, 8.0542, 8.0733, 8.5871, 8.7104, 8.914, 9.2396, 9.7179, 9.7989]
    y = [5.7912, 5.4625, 5.3431, 4.9996, 4.6561, 4.7264, 4.8078, 4.5855, 4.1601, 4.1244, 3.8997, 3.6425, 3.6673, 3.6749, 3.5592, 3.5189, 3.5053, 3.5051, 3.3781, 3.4576, 3.3949, 3.46, 3.4834, 3.5174, 3.5598, 3.5904, 3.6523, 3.6904, 4.0192, 4.0132, 4.2154, 4.315, 4.4469, 4.6732, 5.2456, 5.3356]
    values = [0.2248, 3.9807, 4.2423, 8.6162, 9.664]
    z = []

    a0, a1, a2 = best_poly(x, y, 2) #2 é o grau da parabola
    
    print(a0, ',', a1,',',a2,',') #cuidado com a quantidade de variaveis, se é 1, 2, 3...

    for i in x:
        z.append(f(a0,a1,a2, i))

    np.set_printoptions(suppress=True)
    coefs = poly(x, z)

    for i in values:
        print(p(i,coefs),',')