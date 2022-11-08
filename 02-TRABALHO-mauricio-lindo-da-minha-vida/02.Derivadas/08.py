'''Use o método das diferenças finitas e a seguinte lista de 15 pontos
    x1=0.2335, x2=0.2405, x3=0.2744, x4=0.3229, x5=0.3627, x6=0.4038, x7=0.4196, x8=0.4426, x9=0.4963, x10=0.5259, x11=0.5631, x12=0.5946, x13=0.6223, x14=0.6502  e  x15=0.7037
para encontrar uma aproximação para f(v)(x0), onde 
    f(x)=x²*e^-x * cos(x)+1 e x0=0.456.'''

from cmath import exp
import numpy as np
import math

def coeffs_dif_fin(x0, x, k):
    n = len(x)
    A, B = [[1] * n], [0]
    for i in range(1, n):
        # construção da matriz A
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        # construção da matrz B
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i - k)
            el = (numer / denom) * x0 ** (i - k)
            B.append(el)
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)
    return np.linalg.solve(A, B)

def dif_fin(coeffs, y):
    return sum(ci * yi for ci, yi in zip(coeffs, y))


if __name__ == '__main__':
    
    def f(x):
        return  x**2 * math.exp(-x) * math.cos(x) + 1

    k = 5 # ordem
    n = 15 # número de pontos
    x0 = 0.456
    x =  [0.2335, 0.2405, 0.2744, 0.3229, 0.3627, 0.4038, 0.4196, 0.4426, 0.4963, 0.5259, 0.5631, 0.5946, 0.6223, 0.6502, 0.7037]



    # queremos pontos no intervalo [x0-e, x0+e]
    e = 0.1 # tolerancias
    # x = np.linspace(x0 - e, x0 + e, n)
    
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)

   # print(f'{coeffs}')
    print(f'{aprox}')