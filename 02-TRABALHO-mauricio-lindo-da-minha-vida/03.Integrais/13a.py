'''
Suponha que a força de resistência do ar sobre um objeto
em queda livre é proporcional ao quadrado da velocidade. 
Neste caso, a velocidade pode ser calculada usando-se

    v(t) = math.sqrt((9.81*67.26)/(0.42))*math.tanh(math.sqrt((9.81*(0.42))/67.26)*x)
a) a regra dos trapézios com 32 subintervalos
b) a regra de Simpson com 16 subintervalos
c) o método de Romberg com h=10.17/10 para obter uma aproximação com erro O(h8)
d) o método da Quadratura Gaussiana que seja exato em polinômios de grau menor que 10

Basta estimar a integral de v(t) no intervalo [0,10.17] usando os métodos indicados. 
E clicando nesse link você encontrará uma lista com as raízes dos polinômios de Legendre e 
os pesos associados.
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
        return math.sqrt((9.81*67.26)/(0.42))*math.tanh(math.sqrt((9.81*(0.42))/67.26)*x)

a = 0
b =  10.76

subintervalos = [32]

n = len(subintervalos)
for i in range(n):
    result = trapezio(f,a, b, subintervalos[i])
    print(f'{result}')

