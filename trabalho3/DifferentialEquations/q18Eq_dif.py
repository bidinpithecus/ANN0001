"""Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=0.4621 e y0=2.4893. Use o método de Runge-Kutta de ordem 4 para estimar 
o valor da solução exata desse PVI nos pontos
x1=0.4792, x2=0.5277, x3=0.5985, x4=0.6558, x5=0.6748, x6=0.7531, 
x7=0.7747, x8=0.8275, x9=0.8869, x10=0.95, x11=0.991, x12=1.0178, x13=1.0827, 
x14=1.1483, x15=1.1892, x16=1.2188, x17=1.29, x18=1.3294, x19=1.3983 e x20=1.4283."""


import math

def rk4(f, x0, y0,x_values, n):
    r = []
    h = x_values[0] - x0
    for _ in range(n):
        #realizar as iterações
        if (_>=1):
            h = x_values[_] - x_values[_-1]
        m1 = f(x0, y0)
        m2 = f(x0 + h/2, y0 + (h/2)*m1)
        m3 = f(x0 + h/2, y0 + (h/2)*m2)
        m4 = f(x0 + h, y0 + h *m3)
        yk = y0 + h * (m1+2*m2+2*m3+m4)/6
        #atualizando os valores
        x0 = x_values[_]
        y0 = yk
        #colocando valores na lista
        r.append((x0, y0))
    return r

if __name__ == "__main__":
    #exemplo
    #y'= 1+xy, y(1)=2
    def f(x, y):
        return y * (1 - x) + x + 2

    x0 = 0.4621
    y0 = 2.4893
    x_values = [0.4792, 0.5277, 0.5985, 0.6558, 0.6748, 0.7531, 0.7747, 0.8275, 0.8869, 0.95, 0.991, 1.0178, 1.0827, 1.1483, 1.1892, 1.2188, 1.29, 1.3294, 1.3983, 1.4283]
    n=20
    r = rk4(f, x0, y0, x_values, n)
    for ri in r:
        print(ri[1],',')