'''Use o método das diferenças finitas e a seguinte lista de 8 pontos
    x1=5.2859, x2=5.3283, x3=5.38, x4=5.4907, x5=5.5318, x6=5.5609, x7=5.6235  e  x8=5.7203
para encontrar uma aproximação para f(iv)(x0), onde 
f(x)=√sin(π+x^2) e x0=5.4961.'''

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
        return math.sin(math.sqrt(math.pi + x**2))

    k = 4 # ordem
    n = 8 # número de pontos
    x0 = 5.4961
    x = [5.2859, 5.3283, 5.38, 5.4907, 5.5318, 5.5609, 5.6235, 5.7203]



    # queremos pontos no intervalo [x0-e, x0+e]
    e = 0.1 # tolerancias
    # x = np.linspace(x0 - e, x0 + e, n)
    
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)

   # print(f'{coeffs}')
    print(f'{aprox}')