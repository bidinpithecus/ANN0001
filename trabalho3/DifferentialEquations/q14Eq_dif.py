"""Considere o seguinte PVI
y′=y(1−x)+x+2,y(x0)=y0,
com x0=0.7477 e y0=1.26231. Use o método de Runge-Kutta de ordem 2 
com b=0.53344 para estimar o valor da solução exata desse PVI nos pontos 
xk=x0+kh, onde k=1,2,…,15. Use h=0.18185."""


def RK2(f, x0, y0, h, n, b):
    a = 1 - b
    p = 1 / (2 * b)
    q = p
    for _ in range(n):
        m1 = f(x0,y0)
        m2 = f(x0+p*h, y0+q*h*m1)
        y0 += (a * m1 + b * m2) * h
        x0 += h
        yield [x0,y0]


#Q11 Prova:
def f(x,y):
    return y*(1-x)+x+2

x0 = 0.764
y0 = 1.11263
h = 0.16547
b = 0.74743
n = 15
e = RK2(f,x0,y0, h,n, b)
for xi, yi in e:
    print(f'{yi}, ')