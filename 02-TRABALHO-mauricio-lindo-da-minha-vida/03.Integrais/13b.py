'''
Suponha que a força de resistência do ar sobre um objeto
em queda livre é proporcional ao quadrado da velocidade. 
Neste caso, a velocidade pode ser calculada usando-se

    v(t) = math.sqrt((9.81*67.26)/(0.42))*math.tanh(math.sqrt((9.81*(0.42))/67.26)*x)
onde cd é um coeficiente de arrasto de segunda ordem. Sabendo que g=9.81m/s2, m=67.26kg e cd=0.42kg/m. Use

a) a regra dos trapézios com 32 subintervalos
b) a regra de Simpson com 16 subintervalos
c) o método de Romberg com h=10.76/10 para obter uma aproximação com erro O(h8)
d) o método da Quadratura Gaussiana que seja exato em polinômios de grau menor que 10
para determinar a distância percorrida pelo objeto após 10.76s.
'''

import math

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior q 1")
    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1,n,2):
        soma_odd += f(a+k*h)
    for k in range(2,n,2):
        soma_even += f(a + k * h)
    return (h/3) * (f(a) + 4 * soma_odd + 2 * soma_even + f(b))

def f(x):
    return math.sqrt((9.81*67.26)/(0.42))*math.tanh(math.sqrt((9.81*(0.42))/67.26)*x)

def simp(x0,x1,x3,y0,y1,y2):
    return ((x1-x0)/3)*(y0+4*y1+y2)

def simpsPonto(x, y):
    tam = (len(x) - 1) // 2
    somas = 0
    k = 0
    for i in range(tam):
        somas += simp(x[k],x[k+1],x[k+2],y[k],y[k+1],y[k+2])
        k += 2
    print(f'{somas}')


intervalo = [0, 10.76]
subintervalos = [16]

n = len(subintervalos)
for i in range(n):
    print(f'{simps(f, intervalo[0], intervalo[1], subintervalos[i])}, ')


