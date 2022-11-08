'''Use a regra dos Trapézios para aproximar o valor da integral
    ∫(1.828, -1.734)((sin(x/(√(x²+1)))+1)dx
Use os números de subintervalos a seguir:
    n=8,13,30,53,95,149,185,438,742,883,2721,8728'''
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
        return math.sin (x/math.sqrt(x**2+1))+1

a = -1.734
b =  1.828

subintervalos = [8, 13, 30, 53, 95, 149, 185, 438, 742, 883, 2721, 8728]

n = len(subintervalos)
for i in range(n):
    result = trapezio(f,a, b, subintervalos[i])
    print(f'{result},')

