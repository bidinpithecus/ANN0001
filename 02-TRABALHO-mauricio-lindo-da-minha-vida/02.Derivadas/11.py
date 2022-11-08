'''De acordo com o teorema de Taylor, toda função n+1 vezes derivável pode ser aproximada por um polinômio de grau n,
mais precisamente, se f é n+1 vezes derivável num ponto x0, então para todo x suficientemente próximo de x0, existe um c, entre x e x0, tal que
.
.
.
O polinômio pn(x) é chamado o polinômio de Taylor de grau n da função f em torno do ponto x0. Esse polinômio pode ser usado para estimar os valores de f(x) para x próximo de x0 e o erro cometido nessas aproximações é medido pela função rn(x).
Sabendo disso, encontre o polinômio de Taylor de grau 5 da função
.
.
.
em torno do ponto x0=0.0912, ou seja, encontre as derivadas de f no ponto x0=0.0912 até a ordem 5 para construir o seguinte polinômio de Taylor
.
.
.
.
'''


import random
import numpy as np
import math
def prod(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def finite_diffs(xs, ordem, x0, f):
    A = []
    B = []
    n = len(xs)
    for i in range(n):
        A.append([0]*n)
        for j in range(n):
            A[i][j] = xs[j] ** i
        potencias = [k + 1 for k in range(i - ordem, i)]
        fatorial = 0 if i < ordem else prod(potencias)
        termo = fatorial * x0 ** (i - ordem)
        B.append(termo)
    A = np.array(A, dtype='float')
    B = np.array(B, dtype='float')
    cs = np.linalg.solve(A,B)
    soma = 0
    for ck, xk in zip(cs, xs):
        soma += ck * f(xk)
    return soma

def f(x):
    return  x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)
x0 = 0.0912
ordem = 5
xs =  [-0.1413, -0.0591, -0.0444, 0.0076, 0.0641, 0.1401, 0.1879, 0.2024, 0.2823, 0.2916]
values =  [0.0016, 0.0398, 0.133, 0.171, 0.2111]
ordem1 = 1
ordem2 = 2
ordem3 = 3
ordem4 = 4
ordem5 = 5

p = 0
n = len(values)
for i in range(n):
    p = f(x0) + finite_diffs(xs, ordem1, x0, f)*(values[i] - x0) + ((finite_diffs(xs, ordem2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(xs, ordem3, x0, f)/6) * ((values[i]-x0)**3)) + ((finite_diffs(xs, ordem4, x0, f)/24) * ((values[i]-x0)**4)) + ((finite_diffs(xs, ordem, x0, f)/120) * ((values[i]-x0)**5)) 
    erroN = math.sqrt(((f(values[i]) - p)**2))
    print(f'{values[i]} = {p} e |f(x) - p3(x)| = {erroN}')

num_pontos = 0
a = x0 - 0.25
b = x0 + 0.25
#xs = [a + (b - a) * random.random() for _ in range(num_pontos)]
#xs.sort()

#r = finite_diffs(xs, ordem, x0, f)
#print(xs)
#print(f'aprox para derivada de ordem {ordem} de f no ponto {x0} {r}')
