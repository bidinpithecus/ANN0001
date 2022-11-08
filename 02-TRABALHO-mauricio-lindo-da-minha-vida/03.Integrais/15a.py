"""Óleo vaza de um tanque a uma taxa de r(t) litros por hora. A taxa decresce à 
medida que o tempo passa, conforme mostrado na tabela a seguir.
      t(h) = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5, 8.25, 9.0, 9.75, 10.5, 11.25, 12.0]
r(t) (L/h) = [9.72, 9.42, 8.97, 8.52, 8.25, 7.59, 7.26, 6.98, 6.49, 6.23, 5.76, 5.34, 4.86, 4.49, 3.9, 3.51, 3.14]

Use (a) a regra dos trapézios e (b) a regra de Simpson, para encontrar estimativas 
para a quantidade total (em L) de óleo que vazou após 12.0 horas."""

import math
from operator import le

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


x = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5, 8.25, 9.0, 9.75, 10.5, 11.25, 12.0]
y = [9.72, 9.42, 8.97, 8.52, 8.25, 7.59, 7.26, 6.98, 6.49, 6.23, 5.76, 5.34, 4.86, 4.49, 3.9, 3.51, 3.14]



trapzPonto(x, y)