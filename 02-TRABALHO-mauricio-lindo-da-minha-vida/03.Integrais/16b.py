'''Em 16 de Maio de 2011 o ônibus espacial Endeavour realizou seu último voo (STS-134) 
em direção à ISS (International Space Station) com a missão de levar o AMS-2 
(Espectômetro Magnético Alpha) e o ELC-3 à estação espacial.

As velocidades do Endeavour, medidas em intervalos de 5 segundos, 
estão apresentadas na tabela a seguir
        t (s) = [0, 5/3600, 10/3600, 15//3600, 20//3600, 25/3600, 30/3600, 35/3600, 40/3600, 45/3600, 
50/3600, 55/3600, 60/3600, 65/3600, 70//3600, 75/3600, 80/3600, 85/3600, 90/3600]
        v (km/h) = [0, 102, 226, 359, 514, 666, 821, 963, 1089, 1202, 1320, 1464, 1628, 1819, 2045, 2312, 2604, 2895, 3204]


'''

import math

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))

#def f(x):
#    return math.sqrt((9.81*70.7)/(0.47/70.7))*math.tanh(math.sqrt((9.81*(0.47/70.7))/70.7*x))

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')


x = [0, 5/3600, 10/3600, 15/3600, 20/3600, 25/3600, 30/3600, 35/3600, 40/3600, 45/3600, 50/3600, 55/3600, 60/3600, 65/3600, 70/3600, 75/3600, 80/3600, 85/3600, 90/3600]
y = [0, 108, 233, 363, 506, 675, 817, 970, 1087, 1212, 1319, 1466, 1632, 1819, 2050, 2316, 2598, 2899, 3205]


simpsPonto(x, y)

