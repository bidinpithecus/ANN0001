"""Em um circuito com tensão aplicada E e com resistência R, indutância 
L e capacitância C em paralelo, a corrente i satisfaz a equação diferencial
didt=Cd2Edt2+1RdEdt+1LE.
Suponha que C=0.2311farads, R=1.3534ohm, L=1.5026henrie e que a tensão seja dada por
E(t)=e−0.0549πtsin(2t−π).
Se i(t0)=i0, com t0=0 e i0=0, use o método de Heun para encontrar estimativas
para a corrente i nos pontos
t1=0.0853, t2=0.124, t3=0.2613, t4=0.3842, t5=0.4704, t6=0.5809, t7=0.6249, 
t8=0.7385, t9=0.8313, t10=0.9542, ...... t149=14.8388 e t150=14.939."""

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
    return y * (1 - x) + x + 2


def g(t, i):
    c = 0.2225
    r = 1.2407
    l = 1.5192

    # considerando a função e(t) = e^(-e_value*pi*t)*sin(2*t-pi)
    # se e^(-0.0549*pi*t) => e_value = 0.0549
    e_value = 0.0544

    def e(t):
        return np.exp(-e_value*np.pi*t)*np.sin(2*t-np.pi)

    def e_(t):
        return np.exp(-e_value*np.pi*t)*(2*np.cos(np.pi-2*t)+e_value*np.pi*np.sin(np.pi-2*t))

    def e__(t):
        return np.exp(-e_value*np.pi*t)*((4-pow(e_value, 2)*pow(np.pi, 2))*np.sin(np.pi-2*t)-4*e_value*np.pi*np.cos(np.pi-2*t))

    return c*e__(t) + (1/r)*e_(t) + (1/l)*e(t)


if __name__ == '__main__':

    x0, y0 = 0,0
    h = 0.101
    n = 150
    b = 1/2
    t_values = [0.0821, 0.1872, 0.2494, 0.3763, 0.4291, 0.5811, 0.6266, 0.7493, 0.8372, 0.9841, 1.0104, 1.1829, 1.2894, 1.3588, 1.419, 1.5228, 1.6731, 1.7646, 1.8437, 1.9876, 2.0524, 2.1386, 2.2132, 2.374, 2.458, 2.5243, 2.6898, 2.7479, 2.8173, 2.9459, 3.0477, 3.139, 3.244, 3.3346, 3.4832, 3.5256, 3.6473, 3.7605, 3.813, 3.9593, 4.0837, 4.1642, 4.2749, 4.3165, 4.464, 4.5131, 4.6173, 4.7461, 4.8225, 4.9152, 5.0323, 5.1888, 5.2635, 5.3546, 5.4386, 5.5673, 5.6214, 5.7421, 5.8248, 5.9329, 6.0125, 6.1484, 6.2599, 6.3572, 6.4804, 6.5763, 6.6773, 6.7869, 6.835, 6.9892, 7.0628, 7.1613, 7.216, 7.3169, 7.4414, 7.5528, 7.6725, 7.7311, 7.8862, 7.9718, 8.0634, 8.1798, 8.2195, 8.3126, 8.4234, 8.5263, 8.6426, 8.7202, 8.8684, 8.9177, 9.0758, 9.1317, 9.2812, 9.3349, 9.4111, 9.5833, 9.6653, 9.756, 9.8489, 9.9782, 10.0543, 10.1441, 10.2806, 10.3767, 10.4137, 10.5716, 10.6679, 10.7772, 10.8277, 10.9687, 11.0745, 11.1764, 11.2241, 11.3535, 11.4123, 11.5535, 11.6662, 11.7844, 11.8121, 11.9468, 12.0195, 12.1672, 12.2541, 12.3801, 12.4407, 12.5108, 12.6106, 12.7513, 12.8199, 12.9287, 13.0436, 13.1828, 13.2327, 13.336, 13.4343, 13.5478, 13.6714, 13.7395, 13.8368, 13.9713, 14.0532, 14.1781, 14.2105, 14.3263, 14.4262, 14.5255, 14.6715, 14.7358, 14.8269, 14.9137]
    """observar o valor de b na função para qual médoto é usado:
    --> b = 1 => metodo = euler_mid
    --> b = 1/2 => metodo = heun
    --> b = 2/3 => metodo = ralston"""
    
    
    # metodo1 = euler(f, x0, y0, h, n)
    # metodo2 = euler_mid(f, x0, y0, h, n)
    # metodo3 = heun(f, x0, y0, h, n)
    # metodo4 = ralston(f, x0, y0, h, n)
    # metodo5 = rk2(g, x0, y0, h, n, b)
    metodo6 = rk2_h_variavel(g, x0, y0, n, b, t_values)

    indice = [i for i in range(n)]
    lista_x, lista_y = zip(*metodo6)

    for i, xi, yi in zip(indice, lista_x, lista_y):
        # print(f'x{i} = {xi} => y{i} = {yi}')
        print(f'{yi},', end='')

 