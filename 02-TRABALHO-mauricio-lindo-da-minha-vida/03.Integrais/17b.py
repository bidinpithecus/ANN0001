'''
Em uma pessoa contaminada com sarampo, o nível de vírus N (medido em número de células 
infectadas por mL de plasma de sangue) atinge um pico em cerca de t=12 dias 
(quando aparecem erupções cutâneas) e, então, diminui bem rápido como resultado da resposta 
imunológica. A área sob o gráfico de N(t) de t=0 a t=12 (como mostrado na figura) 
é igual à quantidade total de infecção necessária para desenvolver sintomas 
(medida em densidade de células infectadas x tempo). A função N tem sido modelada pela função:
    f(t)=-t(t-21)(t+1)

Usando
a) a regra dos trapézios com 31 subintervalos
b) a regra de Simpson com 14 subintervalos
c) o método de Romberg com h=12/10 para obter uma aproximação com erro O(h8)
d) o método da Quadratura Gaussiana que seja exato em polinômios de grau menor que 6
estime a quantidade total de infecção necessária para desenvolver os sintomas de sarampo.

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
    return -x*(x-21)*(x+1)

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


intervalo = [0, 12]
subintervalos = [14]

n = len(subintervalos)
for i in range(n):
    print(f'{simps(f, intervalo[0], intervalo[1], subintervalos[i])} ')


