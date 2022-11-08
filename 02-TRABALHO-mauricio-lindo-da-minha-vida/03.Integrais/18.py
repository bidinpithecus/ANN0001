'''Use a regra dos trapézios para aproximar o valor da integral
    math.cos(pow(x,2))*math.sin(pow(y,2)*x)*math.exp(-y**2) + 1
    
onde R=[−1.978,1.597]×[−1.344,1.75]. Particione o intervalo [−1.978,1.597] em
n1=6 subintervalos e o intervalo [−1.344,1.75] em n2=8 subintervalos.'''

import math


def double_trapz(f, a: float, b: float, c: float, d: float, n1: int, n2: int) -> float:
    if n1 <= 0 or n2 <= 0:
        raise ValueError('Erro de valor')
    h1 = (b - a) / n1
    h2 = (d - c) / n2
    soma_interior = 0
    for i in range(1, n1):
        for j in range(1, n2):
            soma_interior += f(a + i * h1, c + j * h2)
    soma_arestas_horizontais = 0
    for i in range(1, n1):
        for j in [0, n2]:
            soma_arestas_horizontais += f(a + i * h1, c + j * h2)
    soma_arestas_verticais = 0
    for j in range(1, n2):
        for i in [0, n1]:
            soma_arestas_verticais += f(a + i * h1, c + j * h2)
    soma_vertices = 0
    for i in [0, n1]:
        for j in [0, n2]:
            soma_vertices += f(a + i * h1, c + j * h2)
    return (h1*h2/4)*(soma_vertices+4*soma_interior + 2*(soma_arestas_horizontais+soma_arestas_verticais))


def f(x, y):
    return math.cos(pow(x,2))*math.sin(pow(y,2)*x)*math.exp(-y**2) + 1

a,b = [-1.978, 1.597]
c,d =  [-1.344, 1.75]
n1 = 6
n2 = 8

r = double_trapz(f, a, b, c, d, n1, n2)
print(r)