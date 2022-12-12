"""
Considere o seguinte PVI y′=y(1−x)+x+2,y(x0)=y0,
com x0=0.6715 e y0=2.91396. Use o método de Euler para estimar o valor da solução 
exata desse PVI nos pontos
x1=0.70215, x2=0.73095, x3=0.79682, x4=0.83711, x5=0.90941, x6=0.93153, x7=0.98533, 
x8=1.0647, x9=1.10195, x10=1.16404, x11=1.18143, x12=1.23624, x13=1.27724, x14=1.32682, 
x15=1.3984, x16=1.4658, x17=1.47675, x18=1.54056, x19=1.60633 e x20=1.64622."""

import math
import numpy as np

def euler(f, x0, y0, x_values, n):
    listaX = []
    listaY = []
    for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
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
    
    x0 = 0.91181
    y0 = 2.28761
    x_values = [0.93816, 0.98917, 1.04349, 1.09004, 1.14301, 1.16739, 1.2218, 1.30465, 1.33259, 1.38865, 1.4376, 1.49837, 1.52181, 1.60612, 1.62558, 1.69915, 1.74402, 1.80422, 1.82593, 1.89861]

    n = 20
    resposta = euler(f, x0, y0, x_values, n)

    # def y(x):
    #     return 5 * math.exp(x - 1) - x - 2

    # t = np.linspace(x0, x0 + n * h, 100)
    # yt = [y(i) for i in t]

    # cx, cy = zip(*resposta)
    # plt.plot(t, yt)
    # plt.scatter(cx, cy)
    # plt.show()
