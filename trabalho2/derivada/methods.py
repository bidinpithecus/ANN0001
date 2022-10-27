import numpy as np
import math

def printLists(list1, list2):
    list3 = []

    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])

    return list3

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

def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def finite_diffs(x, order, x0, f):
    A = []
    B = []
    n = len(x)
    for i in range(n):
        A.append([0]*n)
        for j in range(n):
            A[i][j] = x[j] ** i
        potencias = [k + 1 for k in range(i - order, i)]
        fatorial = 0 if i < order else prod(potencias)
        termo = fatorial * x0 ** (i - order)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A,B)
    soma = 0
    for ck, xk in zip(cs, x):
        soma += ck * f(xk)
    return soma

def richardson(col_1):
    n = len(col_1)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = 2 ** (i + 1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i + 1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]
