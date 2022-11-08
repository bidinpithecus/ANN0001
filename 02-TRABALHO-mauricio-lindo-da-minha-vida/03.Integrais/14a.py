"""A tabela a seguir mostra leituras do velocímetro de um carro, durante um período de 60.0 
segundos, numa corrida na Daytona International Speedway, Flórida."""

import math

def trapz(f, a, b, n):
    h = (b - a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a)
    soma += f(b)
    soma *= (h/2.0)
    print(f'Area aproximadamente: {soma}')

#def f(x):
 #   return math.sqrt(math.sin(math.cos(math.log(x**2 + 1) + 2) + 3) + 4)

def trapzPonto(x, y):
    tam = len(x) - 1
    somas = 0
    for i in range(tam):
        h = x[i+1] - x[i]
        somas += (h/2) * (y[i] + y[i+1])
    print(f'{somas}')


x = [0, 5/3600, 10/3600, 15/3600, 20/3600, 25/3600, 30/3600, 35/3600, 40/3600, 45/3600, 50/3600, 55/3600, 60/3600]
y = [166.36, 200.39, 215.66, 245.86, 153.71, 226.21, 107.9, 132.79, 287.93, 273.43, 267.68, 179.3, 124.02]


trapzPonto(x, y)