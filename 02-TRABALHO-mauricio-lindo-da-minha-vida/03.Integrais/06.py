'''Use a regra de Simpson para aproximar o valor da integral

∫1.709,-1.807 (math.sin(x/(math.sqrt(math.pow(x,2)+1)))+1)dx

Use os números de subintervalos a seguir:
n=8, 14, 26, 70, 78, 104, 136, 166, 176, 248, 470'''

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
    return math.sin(x/(math.sqrt(math.pow(x,2)+1)))+1

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


intervalo = [-1.173, 1.852]
subintervalos = [8, 14, 26, 70, 78, 104, 136, 166, 176, 248, 470]

n = len(subintervalos)
for i in range(n):
    print(f'{simps(f, intervalo[0], intervalo[1], subintervalos[i])}, ')


