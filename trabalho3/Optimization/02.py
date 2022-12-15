"""Sejam
f1(x)=1, f2(x)=x, f3(x)=x2, f4(x)=x3, f5(x)=x4, f6(x)=x5, f7(x)=x6, f8(x)=x7  e  f9(x)=x8
Encontre os coeficientes da combinação linear
g(x)=c1f1(x)+c2f2(x)+c3f3(x)+c4f4(x)+c5f5(x)+c6f6(x)+c7f7(x)+c8f8(x)+c9f9(x)
que melhor se aproxima da função f(x)=x2exln(2+cos(−x2))−−−−−−−−−−−−−√ no intervalo [a,b], com a=−2.06485 e b=0.84178. Para o cálculo dos coeficientes ck, use a regra de Simpson com 256 subintervalos. Em seguida calcule g(x) para os seguintes valores de x
x1=−1.53854, x2=−0.88865 e x3=0.46267.
A função g(x) é uma aproximação para a função f(x) no intervalo [−2.06485,0.84178] com erro dado por
erro=∫0.84178−2.06485[f(x)−g(x)]2dx.
Use o método de Romberg com h=(b−a)/10 e erro da ordem de O(h8) para determinar o erro."""

import numpy as np
import math

def aprox(f, f_list, a, b, num_intervals):
    n = len(f_list)
    A = [[0 for _ in range(n)] for _ in range(n)]  #A é simetrica
    B = []
    for i in range(n):
        for j in range(i, n): #elementos na diagonal da matriz 
             def f_ji(x):
                return f_list[j](x) * f_list[i](x)
             
             a_ij = simps(f_ji,a,b,num_intervals) #inetgral de f_j *f_i
             #nao altere mais
             A[i][j] = a_ij
             A[j][i] = a_ij
        def ff_i(x):
            return f(x) * f_list[i](x)
        
        b_i = simps (ff_i,a,b,num_intervals) #inetgral de f *ff_i
        #nao altere mais
        B.append(b_i)
    return np.linalg.solve(A,B)


def build_g(coefs, f_list):
    def func_g(x):
        return sum (ci* fi(x) for ci, fi in zip (coefs, f_list))
    return func_g


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


def romberg(col1):
    n = len(col1)
    col1 = [item for item in col1]

    for j in range(n - 1):     # percorrer as colunas
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):  # percorrer as linhas
            power = j + 1
            temp_col[i] = ((4 ** power) * col1[i + 1] -
                           col1[i]) / (4 ** power - 1)
        col1[:n - 1 - j] = temp_col
       # print(f'F_{j+2}', temp_col)
    return col1[0]


def trapz(f, a, b, h):
    n = int((b - a)/h)
    soma = 0
    for k in range(1, n):
        soma += f(a + k * h)
    soma *= 2
    soma += f(a) + f(b)
    soma *= h/2
    return soma


def build_func(s, var: str='x'):
    scope = {}
    scope['math'] = math
    func = f'def f({var}): return {s}'
    exec(func, scope)
    return scope['f']


if __name__ == '__main__':

    

    def func(x):
         return  x**2 * math.exp(x) * math.sqrt(math.log(2 + math.cos(-x**2)))

    funcs_str =   ['1', 'x', 'x**2', 'x**3', 'x**4', 'x**5', 'x**6', 'x**7', 'x**8']
    a = -2.06485
    b = 0.84178
    n = 256
    order = 8


    funcs = []
    for func_str in funcs_str:
        f = build_func(func_str)
        funcs.append(f)

   
    

    
    
    
    coefs = aprox(func, funcs, a, b, n)
    #essa é a funçao g que melhor se aproxima f(x)
    
    g = build_g(coefs, funcs)
    
    for i in coefs:
        print(f"{i}, ")

    x1 = g(-1.53854)
    print(f'{x1},')
    x2 = g(-0.88865 )
    print(f'{x2},')
    x3 = g(0.46267)
    print(f'{x3},')


    def ferro(x):
        return (func(x) - g(x))**2

    
    h = (b-(a))/10
    erro_da_ordem = int(order/2)
    hs = [h / 2 ** i for i in range(erro_da_ordem)]
    col1 = [trapz(ferro, a, b, hi) for hi in hs]
   
    r = romberg(col1)
    print(r)




            

 