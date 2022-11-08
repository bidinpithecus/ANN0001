'''
Em uma pessoa contaminada com sarampo, o nível de vírus N (medido em número de células 
infectadas por mL de plasma de sangue) atinge um pico em cerca de t=12 dias 
(quando aparecem erupções cutâneas) e, então, diminui bem rápido como resultado da resposta 
imunológica. A área sob o gráfico de N(t) de t=0 a t=12 (como mostrado na figura) 
é igual à quantidade total de infecção necessária para desenvolver sintomas 
(medida em densidade de células infectadas x tempo). A função N tem sido modelada pela função:
    f(t)=-t(t-21)(t+1)

Usando
a) a regra dos trapézios com 31 subintervalos
b) a regra de Simpson com 14 subintervalos
c) o método de Romberg com h=12/10 para obter uma aproximação com erro O(h8)
d) o método da Quadratura Gaussiana que seja exato em polinômios de grau menor que 6
estime a quantidade total de infecção necessária para desenvolver os sintomas de sarampo.
'''
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
        return -x*(x-21)*(x+1)

a = 0
b = 12

subintervalos = [31]

n = len(subintervalos)
for i in range(n):
    result = trapezio(f,a, b, subintervalos[i])
    print(f'{result}')

