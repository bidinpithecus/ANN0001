import math
import numpy as np



def euler_mid(f, x0, y0, x_values, n):
    vals = []
    for k in range(n):
        if k == 0:
            h = x_values[0] - x0
        else:
            h = x_values[k] - x_values[k-1]
        
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += + h * m2
        x0 += + h
        print(f'{y0},')
        vals.append([x0, y0])
    return vals

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

    x0 = 1.22252
    y0 = 0.95022
    x_values = [1.23738, 1.27815, 1.3619, 1.38307, 1.45499, 1.50959, 1.55064, 1.60484, 1.65794, 1.70654, 1.75079, 1.79674, 1.86401, 1.91287, 1.95561, 1.9834, 2.05733, 2.10742, 2.15828, 2.18946]
    n = 20
    resposta = euler_mid(f, x0, y0, x_values, n)

    # def y(x):
    #     return 5 * math.exp(x - 1) - x - 2

    # t = np.linspace(x0, x0 + n * h, 100)
    # yt = [y(i) for i in t]

    # cx, cy = zip(*resposta)
    # plt.plot(t, yt)
    # plt.scatter(cx, cy)
    # plt.show()
