"""Óleo vaza de um tanque a uma taxa de r(t) litros por hora. A taxa decresce à 
medida que o tempo passa, conforme mostrado na tabela a seguir.
      t(h) = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5, 8.25, 9.0, 9.75, 10.5, 11.25, 12.0]
r(t) (L/h) = [9.72, 9.42, 8.97, 8.52, 8.25, 7.59, 7.26, 6.98, 6.49, 6.23, 5.76, 5.34, 4.86, 4.49, 3.9, 3.51, 3.14]

Use (a) a regra dos trapézios e (b) a regra de Simpson, para encontrar estimativas 
para a quantidade total (em L) de óleo que vazou após 12.0 horas."""

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

#def f(x):
#    return math.sqrt((9.81*70.7)/(0.47/70.7))*math.tanh(math.sqrt((9.81*(0.47/70.7))/70.7*x))

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


x = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0, 6.75, 7.5, 8.25, 9.0, 9.75, 10.5, 11.25, 12.0]
y = [9.72, 9.42, 8.97, 8.52, 8.25, 7.59, 7.26, 6.98, 6.49, 6.23, 5.76, 5.34, 4.86, 4.49, 3.9, 3.51, 3.14]



simpsPonto(x, y)

