""" Uma lancha se move na direção positiva do eixo x, puxando um esquiador aquático ao longo de uma curva C chamada uma Tractriz. Veja a Figura 1.
image is not available
Figura 1: Uma lancha puxando um esquiador aquático por uma corda.
O esquiador aquático é puxado por uma corda de comprimento constante a que é mantida esticada ao longo do trajeto. Assumindo que a corda é sempre tangente à curva C, é possível concluir que a trajetória do esquiador deve satisfazer à seguinte equação diferencial
dydx=−ya2−y2−−−−−−√,y(x0)=y0.
Se P0=(x0,y0), com x0=1.957 e y0=4.718, denota a posição inicial do esquiador. Use o método de Runge-Kutta de ordem 2 com b=0.612 para estimar a posição do esquiador nos pontos xk=x0+kh, onde k=1,2,…,10. Suponha que a=9.13 e h=0.097. """

import math

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
    a = 8.5289
    return -y/(math.sqrt(a**2 - y**2)) # a

x0 = 1.04013
y0 = 5.31202
b = 0.69049
h = 0.17938
n = 100
e = RK2(f,x0,y0, h,n, b)
# for xi, yi in e:
#     print(xi, yi)
for xi, yi in e:
    print(f'{yi},')
    
    
    """
    Uma lancha se move na direção positiva do eixo x, puxando um esquiador aquático 
    ao longo de uma curva C chamada uma Tractriz. Veja a Figura 1.
    
    O esquiador aquático é puxado por uma corda de comprimento constante a 
    que é mantida esticada ao longo do trajeto. Assumindo que a corda é sempre 
    tangente à curva C, é possível concluir que a trajetória do esquiador deve 
    satisfazer à seguinte equação diferencial
    dydx=−ya2−y2−−−−−−√,y(x0)=y0.
    Se P0=(x0,y0), com x0=1.95162 e y0=5.81928, denota a posição inicial do esquiador. 
    Use o método de Runge-Kutta de ordem 2 com b=0.52511 para estimar a 
    posição do esquiador nos pontos xk=x0+kh, onde k=1,2,…,100. Suponha que a=9.31837 
    e use h=0.11081.
    """