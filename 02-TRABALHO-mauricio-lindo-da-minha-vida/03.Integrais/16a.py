"""'''Em 16 de Maio de 2011 o ônibus espacial Endeavour realizou seu último voo (STS-134) 
em direção à ISS (International Space Station) com a missão de levar o AMS-2 
(Espectômetro Magnético Alpha) e o ELC-3 à estação espacial.

As velocidades do Endeavour, medidas em intervalos de 5 segundos, 
estão apresentadas na tabela a seguir
        t (s) = [0, 5/3600, 10/3600, 15//3600, 20//3600, 25/3600, 30/3600, 35/3600, 40/3600, 45/3600, 
50/3600, 55/3600, 60/3600, 65/3600, 70//3600, 75/3600, 80/3600, 85/3600, 90/3600]
        v (km/h) = [0, 102, 226, 359, 514, 666, 821, 963, 1089, 1202, 1320, 1464, 1628, 1819, 2045, 2312, 2604, 2895, 3204]

use o excel colar > colar transposto(para colar um no lado do outro)
"""

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


x = [0, 5/3600, 10/3600, 15/3600, 20/3600, 25/3600, 30/3600, 35/3600, 40/3600, 45/3600, 50/3600, 55/3600, 60/3600, 65/3600, 70/3600, 75/3600, 80/3600, 85/3600, 90/3600]
y = [0, 108, 233, 363, 506, 675, 817, 970, 1087, 1212, 1319, 1466, 1632, 1819, 2050, 2316, 2598, 2899, 3205]

trapzPonto(x, y)