
import math
import numpy as np

# exemplo y'= 1 +xy, y(1) = 2

def heun(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h * m1)
        y1 = y0 + h * (m1 + m2) / 2
        x0 += h
        y0 = y1
        r.append( (y0) )
    return r

if __name__ == '__main__':

    def f(x, y):
        return y*(2-x) + x + 1

    x0 = 0.61417
    y0 = 0.90802
    h = 0.125
    n  = 10
    r = heun(f, x0, y0, h, n)
    print(r)

    # x, y = zip(*resposta)
    # print(x)
    # print(y)
    # plt.scatter(x,y)
    # plt.savefig('euler_half.png')
