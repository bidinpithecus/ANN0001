"""
Use a regra dos Trapézios para aproximar o valor da integral
∫(1.452,-1.988) e^-x²dx.
Use os números de subintervalos a seguir:
n=7,24,33,54,92,138,205,493,714,997,3528,9022"""
import numpy as np
import math

def trapezio(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):  # comecar em 1 evitando que o primeiro ponto seja calculado 2 vezes
        soma += f(a + k * h)
    soma *= 2
    soma += (f(a) + f(b))
    soma *= (h / 2)
    return soma

if __name__ == '__main__':

    def f(x):
        return math.exp(-x**2)

a = -1.988
b= 1.452


subintervalos = [7, 24, 33, 54, 92, 138, 205, 493, 714, 997, 3528, 9022]

n = len(subintervalos)
for i in range(n):
    result = trapezio(f,a, b, subintervalos[i])
    print(f'{result},')

