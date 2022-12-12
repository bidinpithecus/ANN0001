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

def RK4GivenX(f, x0, y0, h, n, x_values):
    r = []
    for k in range(n):
        m1 = f(x0,y0)
        m2 = f(x0 + h/2, y0 + (h/2) * m1)
        m3 = f(x0 + h/2, y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1+2 * m2 + 2 * m3 + m4)/6
        h = x_values[k] - x_values[k-1]
        x0 = x_values[k-1]
        y0 = yk
        r.append((x0,y0))
    
    m1 = f(x0,y0)
    m2 = f(x0 + h/2, y0 + (h/2) * m1)
    m3 = f(x0 + h/2, y0 + (h/2) * m2)
    m4 = f(x0 + h, y0 + h * m3)
    yk = y0 + h * (m1+2 * m2 + 2 * m3 + m4)/6
    h = x_values[n-1] - x_values[n-2]
    x0 = x_values[k-1]
    y0 = yk
    r.append((x0,y0))
    return r

def f(x,y):
    return  y * (1 - x) + x + 2

x0 = 0.825
y0 = 2.3035
x_values = [0.8502, 0.881, 0.9342, 1.01, 1.0344, 1.1007, 1.1596, 1.1839, 1.2453, 1.2932, 1.3435, 1.4192, 1.4361, 1.5123, 1.5532, 1.6193, 1.6326, 1.708, 1.7474, 1.7844]
n=20

h = x_values[0] - x0

r = RK4GivenX(f,x0,y0, h,n, x_values)
x, y = zip(*r)

valores = str(y)[1:-1] 
print(valores)
