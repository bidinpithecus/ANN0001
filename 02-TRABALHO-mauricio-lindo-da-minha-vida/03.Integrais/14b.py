'''"""A tabela a seguir mostra leituras do velocímetro de um carro, durante um período de 60.0 
segundos, numa corrida na Daytona International Speedway, Flórida."""'''

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


x = [0, 5/3600, 10/3600, 15/3600, 20/3600, 25/3600, 30/3600, 35/3600, 40/3600, 45/3600, 50/3600, 55/3600, 60/3600]
y = [166.36, 200.39, 215.66, 245.86, 153.71, 226.21, 107.9, 132.79, 287.93, 273.43, 267.68, 179.3, 124.02]



simpsPonto(x, y)

