"""Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.12542 e y0=2.0532. Use o método de Euler para estimar 
o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,15. Use h=0.16746."""

import math

import numpy as np

def euler(f, x0, y0, h, n):
    listaX = []
    listaY = []
    for i in range(n):
        y0 += f(x0, y0) * h
        x0 += h
        #print(x0,y0)
        listaX.append(x0)
        listaY.append(y0)
    print('Valores X')
    for i in listaX:
        print(f'{i}, ')
    print()
    print('Valores Y')
    for i in listaY:
        print(f'{i}, ')
    
    

if __name__ == '__main__':

    #def f(x, y):
    #     return k*y

    #x0, y0 = 0.0, 1185514 # x0 = t, y0 = indivíduos
   # h = 0.0625
    #n = int(1/h)
    #k = 0.0712

    #P3.7
    def f(x, y):
        return y * (1 - x) + x + 2

    x0 = 1.56263
    y0 = 2.52268
    h = 0.15548
    n = 15

    resposta = euler(f, x0, y0, h, n)

    # def y(x):
    #     return 5 * math.exp(x - 1) - x - 2

    # t = np.linspace(x0, x0 + n * h, 100)
    # yt = [y(i) for i in t]

    # cx, cy = zip(*resposta)
    # plt.plot(t, yt)
    # plt.scatter(cx, cy)
    # plt.show()
