
"""Seja Tn o polinômio de Chebyshev de grau n definido no intervalo [-1,1] por
Tn(x)=cos(n⋅arccos(x)).
Seja
g(x)=c0T0(x)+c1T1(x)+c2T2(x)+c3T3(x)
uma combinação linear dos 5 primeiros polinômios de Chebyshev. Encontre os coeficientes c0,c1,…,c4 tal que g(x) se aproxime o melhor possível da função f(x)=xsin(-6x2) no intervalo [-1,1]. Para o cálculo dos coeficientes ck, use a regra dos trapézios com 8192 subintervalos. Em seguida calcule g(x) para os seguintes valores de x
x1=-0.753, x2=-0.209 e x3=0.575.
A função g(x) é uma aproximação para a função f(x) no intervalo [-1,1] com erro dado por
erro=∫1-1[f(x)-g(x)]2dx.
Use a regra dos trapézios com 512 subintervalos para determinar o erro."""

import math
import numpy as np

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += (f(a +  k * h))
    soma *= 2
    soma += (f(a) + f(b))
    return soma * (h / 2)

def T(n, x):
    return math.cos(n * math.acos(x))

def aprox(f, f_list):
    n = len(f_list)
    A = [[0 for _ in range(n)] for _ in range(n)] # A é simetrica
    B = []
    for i in range(n):
        for j in range(i, n):
            def f_ji(x):
                return f_list[j](x) * f_list[i](x)
            
            # altere dependendo do metodo de integração
            a = -1
            b = 1
            a_ij = trapz(f_ji, a, b, 8192)
            
            A[i][j] = a_ij
            A[j][i] = a_ij
        
        def ff_i(x):
            return f(x) * f_list[i](x)
        
        # altere dependendo do metodo de integração
        a = -1
        b = 1
        b_i = trapz(ff_i, a, b, 8192)

        B.append(b_i)
    
    return np.linalg.solve(A, B)

def build_g(coeffs, f_list):
    def func(x):
        soma = 0
        for c, f in zip(coeffs, f_list):
            soma += c * f(x)
        return soma
    return func

if __name__ == "__main__":
    def f(x):
        return x * math.sin(-6 * x **2)

    f_list = [
        lambda x: T(0, x),
        lambda x: T(1, x),
        lambda x: T(2, x),
        lambda x: T(3, x),
        lambda x: T(4, x)
    ]
    a = -1
    b = 1
    values = [-0.618, 0.057, 0.759]

    coeffs = aprox(f, f_list)
    g = build_g(coeffs, f_list)

    for c in coeffs:
        print(f"{c},")
    
    for v in values:
        print(f"{g(v)},")

    def f_erro(x):
        return (f(x) - g(x)) ** 2


    erro = trapz(f_erro, a, b, 512)
    print(erro)

    