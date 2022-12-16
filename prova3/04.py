""" Uma lancha se move na direção positiva do eixo x, puxando um esquiador aquático ao longo de uma curva C chamada uma Tractriz. Veja a Figura 1.
image is not available
Figura 1: Uma lancha puxando um esquiador aquático por uma corda.
O esquiador aquático é puxado por uma corda de comprimento constante a que é mantida esticada ao longo do trajeto. Assumindo que a corda é sempre tangente à curva C, é possível concluir que a trajetória do esquiador deve satisfazer à seguinte equação diferencial
dydx=-ya2-y2------√,y(x0)=y0.
Se P0=(x0,y0), com x0=1.957 e y0=4.718, denota a posição inicial do esquiador. Use o método de Runge-Kutta de ordem 2 com b=0.612 para estimar a posição do esquiador nos pontos xk=x0+kh, onde k=1,2,…,10. Suponha que a=9.13 e h=0.097. """

import math

def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        x0 += h
        xk = x0 + k*h
        y0 += h * f(xk, y0)
        vals.append([xk,y0])
    return vals

#Q11 Prova:
def f(x,y):
    a = 8.15314
    return -y/(math.sqrt(a**2 - y**2)) # a

x0 = 1.2417
y0 = 4.45213
h = 0.13439
n = 100
e = euler(f, x0, y0, h, n)
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
    dydx=-ya2-y2------√,y(x0)=y0.
    Se P0=(x0,y0), com x0=1.95162 e y0=5.81928, denota a posição inicial do esquiador. 
    Use o método de Runge-Kutta de ordem 2 com b=0.52511 para estimar a 
    posição do esquiador nos pontos xk=x0+kh, onde k=1,2,…,100. Suponha que a=9.31837 
    e use h=0.11081.
    """