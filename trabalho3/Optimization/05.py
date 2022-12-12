""" Encontre os coeficientes dos 11 primeiros termos da série de Fourier da função 
f(x)=xsin(6e−x2) no intervalo [−π,π], ou seja, encontre os coeficientes da função

        g(x)=c+∑n=15[ancos(nx)+bnsin(nx)]
        
Para o cálculo dos coeficientes c, an e bn, use a regra dos trapézios com 1024 subintervalos. Em seguida calcule g(x) para os seguintes valores de x
x1=−1.454, x2=0.696 e x3=2.336.

A função g(x) é uma aproximação para a função f(x) no intervalo [−π,π] com erro dado por

erro=∫π−π[f(x)−g(x)]2dx.

Use o método de Romberg com h=(b−a)/10 e erro da ordem de O(h8) para determinar o erro.. """

from math import cos, sin, exp, pi, ceil
import numpy as np



def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2

def trapz2(f, a, b, h):
    n = int((b - a)/h)
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a) + f(b)
    soma *= h/2
    return soma


def romberg(coluna_f1):
    coluna_f1 = [i for i in coluna_f1]
    n = len(coluna_f1)
    for j in range(n - 1):
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):
            power = j + 1
            temp_col[i] = (4 ** power * coluna_f1[i + 1] - coluna_f1[i]) / (4 ** power - 1)
        coluna_f1[:n - 1 - j] = temp_col
        # print(f'F_{j+2} = {temp_col}')
    return coluna_f1[0]

def quadratura(funcao, pontos, pesos):
    soma = 0

    for xk, ck in zip(pontos, pesos):
        soma += ck * funcao(xk)

    return soma


def change(f, a, b):
    def g(u):
        return f((b + a) / 2 + (b - a) * u / 2) * (b - a) / 2

    return g

def comb(c, funcs):
    def g(x):
        return sum(ci * fi(x) for ci, fi in zip(c, funcs))
    return g

def f(x):
    return x * sin(6 * exp(-x**2))

if __name__ == '__main__':  


    a = -3.141592653589793
    b = 3.141592653589793
    values = [-1.454, 0.696, 2.336]
    subintervalos = 1024
    grau = 11 
    order = 8

    coeffs = []

    c = (1/(2 * pi)) * trapz(f, a, b, subintervalos)
    coeffs.append(c)

    for m in range(1, 6):
        am = (1/pi) * trapz(lambda x: f(x) * cos(m * x), a, b, subintervalos)
        coeffs.append(am)
        bm = (1/pi) * trapz(lambda x: f(x) * sin(m * x), a, b, subintervalos)
        coeffs.append(bm)
        
    for i in range(len(coeffs)):
        print(f"{coeffs[i]}, ")
    
        
    def g(x, coeffs):
        soma = coeffs[0]
        for i in range(1, len(coeffs), 2):
            soma += coeffs[i] * cos(ceil(i/2)*x)
            soma += coeffs[i+1] * sin(ceil(i/2)*x)
        return soma
    
    for xi in values:
        print(f"{g(xi, coeffs)}, ")
        
        
        
    def func_erro(x):
        return pow((f(x) - g(x, coeffs)), 2)
    
    
    h = (b-(a))/10
    erro_da_ordem = int(order/2)
    hs = [h / 2 ** i for i in range(erro_da_ordem)]
    col1 = [trapz2(func_erro, a, b, hi) for hi in hs]
   
    r = romberg(col1)
    print(r)