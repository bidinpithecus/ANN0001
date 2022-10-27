import math
from numpy import double

# Usado para aproximar o valor de uma integral
def trapz(f, a, b, n):
    h = (b-a) / n
    soma = 0
    for k in range(1, n):
        soma += f(a + k*h)
    soma *= 2
    soma += (f(a) + f(b))
    return (h/2) * soma


def f(x):
    return math.sqrt(math.sin(math.cos(math.log(x**2+1)+2)+3)+4)

# Variável inferior
a = -1.448

# Variável superior
b = 1.97

# Lista de subintervalos
n = [4, 14, 41, 67, 99, 110, 218, 353, 710, 909, 2056, 6533]

for i in range(len(n)):
    r = trapz(f, a, b, n[i])
    print(r)