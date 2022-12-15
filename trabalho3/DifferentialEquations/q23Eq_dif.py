"""Em um circuito com tensão aplicada E e com resistência R, indutância L e capacitância C
em paralelo, a corrente i satisfaz a equação diferencial
    didt=Cd2Edt2+1RdEdt+1LE.
Suponha que C=0.2365farads, R=1.1947ohm, L=1.9022henrie e que a tensão seja dada por
E(t)=e−0.0573πtsin(2t−π).
Se i(t0)=i0, com t0=0 e i0=0, use o método de Heun para encontrar
estimativas para a corrente i nos pontos tk=t0+kh, onde k=1,2,…,150 e h=0.1597."""

import numpy as np



def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        y0 += h*f(x0, y0)
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1
def euler_mid(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h/2) * m1)
        y0 += h*m2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 1/2
def heun(f, x0, y0, h, n):
    vals = []
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h, y0 + h*m1)
        y0 += h*(m1+m2)/2
        x0 += h
        vals.append([x0, y0])
    return vals


# b = 2/3
# def ralston(f, x0, y0, h, n):
#     vals = []
#     for _ in range(n):
#         m1 = f(x0, y0)
#         m2 = f(x0 + 0.75*h, y0 + 0.75*h*m1)
#         y0 = h*(m1 + 2*m2)/3
#         x0 += h
#         vals.append([x0, y0])
#     return vals


# padrao = euler_mid
def rk2(f, x0, y0, h, n, b=1.0):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def rk2_h_variavel(f, x0, y0, n, b, x_values):
    # b = 1 => metodo = euler_mid
    # b = 1/2 => metodo = heun
    # b = 2/3 => metodo = ralston
    vals = []
    a = 1-b
    p = 1/(2*b)
    q = p
    for i in range(n):
        if i == 0:
            h = x_values[0] - x0
        else:
            h = x_values[i] - x_values[i-1]
        m1 = f(x0, y0)
        m2 = f(x0 + p*h, y0 + q*h*m1)
        y0 += (a*m1 + b*m2)*h
        x0 += h
        vals.append([x0, y0])
    return vals


def diff(a, b):
    return sum((ai - bi)**2 for ai, bi in zip(a, b))


def f(x, y):
    return  y * (1 - x) + x + 2


def g(t, i):
    c = 0.2768
    r = 1.1829
    l = 1.9973

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0573*pi*t) => e_value = 0.0573
    e_value = 0.0573

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.1983
    n = 150
    b = 1/2
    """observar o valor de b na função para qual médoto é usado:
    --> b = 1 => metodo = euler_mid
    --> b = 1/2 => metodo = heun
    --> b = 2/3 => metodo = ralston"""
    
    
    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo5 = rk2(g, x0, y0, h, n, b)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo5)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi}, ')

    