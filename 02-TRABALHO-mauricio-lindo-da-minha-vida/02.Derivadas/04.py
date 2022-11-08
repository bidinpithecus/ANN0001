'''Use o método das diferenças finitas e a seguinte lista de 8 pontos
    x1=3.8019, x2=3.8666, x3=3.9756, x4=4.024, x5=4.0855, x6=4.1622, x7=4.213  e  x8=4.2818
para encontrar uma aproximação para f′′(x0), onde
     f(x)=√(cos(x^2)+x) e x0=4.0407.'''

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
        return math.sqrt(math.cos(x**2) + x)

    k = 2 # ordem
    n = 8 # número de pontos
    x0 = 4.0407
    x = [3.8019, 3.8666, 3.9756, 4.024, 4.0855, 4.1622, 4.213, 4.2818]



    # queremos pontos no intervalo [x0-e, x0+e]
    e = 0.1 # tolerancias
    # x = np.linspace(x0 - e, x0 + e, n)
    
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, k)
    aprox = dif_fin(coeffs, y)

   # print(f'{coeffs}')
    print(f'{aprox}')