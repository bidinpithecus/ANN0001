"""Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=1.02835 e y0=1.37083. Use o método do ponto médio de Euler para 
estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, 
onde k=1,2,…,10. Use h=0.125."""

import math
import numpy as np



def euler_mid(f, x0, y0, h, n):
    listaX = []
    listaY = []
    for k in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += + h * m2
        x0 += + h
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
        return y*(2 - x) + x + 1

    x0 = 1.99162
    y0 = 1.43476
    h = 0.17675
    n= 15

    resposta = euler_mid(f, x0, y0, h, n)

    # def y(x):
    #     return 5 * math.exp(x - 1) - x - 2

    # t = np.linspace(x0, x0 + n * h, 100)
    # yt = [y(i) for i in t]

    # cx, cy = zip(*resposta)
    # plt.plot(t, yt)
    # plt.scatter(cx, cy)
    # plt.show()
