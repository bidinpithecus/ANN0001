'''A seguinte lista de 5 pontos
(1.175,2.629), (2.414,2.171), (3.653,2.398), (3.7075,2.224) e (3.762,2.037)
vive no gráfico de uma função f. Use a regra de Simpson para aproximar a área embaixo 
do gráfico de f no intervalo [1.175,3.762].
'''

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


x = [1.175, 2.414, 3.653, 3.7075, 3.762]
y = [2.629, 2.171, 2.398, 2.224, 2.037]

simpsPonto(x, y)

