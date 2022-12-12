"""Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=1.4 e y0=1.2331. Use o método de Runge-Kutta de ordem 4 para estimar o valor da solução exata desse PVI nos pontos xk=x0+kh, onde k=1,2,…,15. Use h=0.1976."""


def RK4(f, x0, y0, h, n):
    r = []
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1+2 * m2 + 2 * m3 + m4)/6
        x0 += h
        y0 = yk
        r.append((x0,y0))
    return r

def f(x,y):
    return  y * (1 - x) + x + 2

x0 = 1.4
y0 = 1.2331
h = 0.1976
n=15
r = RK4(f,x0,y0, h,n)
for xi, yi in r:
    print(f'{yi}, ')
    