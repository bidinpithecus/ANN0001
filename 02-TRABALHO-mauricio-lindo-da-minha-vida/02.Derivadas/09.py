'''De acordo com o teorema de Taylor, toda função n+1 vezes derivável pode ser aproximada
por um polinômio de grau n, mais precisamente, se f é n+1 vezes derivável num ponto x0, 
então para todo x suficientemente próximo de x0, existe um c, entre x e x0, tal que
        f(x)=pn(x)+rn(x),
onde 
        pn(x)=f(x0)+f′(x0)(x−x0)+f′′(x0)2!(x−x0)2+⋯+f(n)(x0)n!(x−x0)n
e
        rn(x)=f(n+1)(c)(n+1)!(x−x0)(n+1)

O polinômio pn(x) é chamado o polinômio de Taylor de grau n da função f em torno do ponto x0. 
Esse polinômio pode ser usado para estimar os valores de f(x) para x próximo de x0 e o erro 
cometido nessas aproximações é medido pela função rn(x).
Sabendo disso, encontre o polinômio de Taylor de grau 3 da função
        f(x)=3cos((x2−1)1/3)

em torno do ponto x0=5.6028, ou seja, encontre as derivadas de f no ponto x0=5.6028 
até a ordem 3 para construir o seguinte polinômio de Taylor
        p3(x)=f(x0)+f′(x0)(x−x0)+f′′(x0)2!(x−x0)2+f′′′(x0)3!(x−x0)3

Em seguida, use esse polinômio para estimar o valor de f(x) nos seguintes valores de x
        x=5.6072 , x=5.6741  e  x=5.7342

e compare os resultados com os valores exatos de f nesses pontos, ou seja, 
para cada valor de x dado acima calcule o erro |f(x)−p3(x)|. 
Para o cálculo das derivadas acima, use o método das diferenças finitas com os seguintes pontos
        x1=5.4175, x2=5.5139, x3=5.5208, x4=5.6213, x5=5.6886  e  x6=5.7983



'''

import numpy as np
import math

# x0 = ponto onde a função será derivada
# x = lista de coordenadas na proximidade de x0
# y = cálculo da função em todos os pontos x
# k = ordem da derivada

def coeffs_dif_fin(x0, x, k):
    n = len(x)
    A, B = [[1]* n], [0]
    for i in range(1, n):
        # construção da matriz A
        row_i = [xi ** i for xi in x]
        A.append(row_i)
        # construção da matriz B
        if i < k:
            B.append(0)
        elif i == k:
            B.append(math.factorial(k))
        else:
            numer = math.factorial(i)
            denom = math.factorial(i - k)
            el = (numer / denom) * x0 ** (i - k)
            B.append(el)
    return np.linalg.solve(A, B)
        
def dif_fin(coeffs, y):
    return sum(ci * yi for ci, yi in zip(coeffs, y))
        

if __name__ == '__main__':
    # exemplo 1:
    def f(x):
        return 3 * math.cos((x**2-1)**(1/3))
    def p(xp):
        x0 = 7.8655
        n = 6 # numero de pontos igualmente espaçados
        # queremos pontos no intervalo [x0-e, x0+e]
        # ao diminuir o epsilon (e) os pontos são cada vez mais próximos
        e = 0.001
        x =  [7.6962, 7.7725, 7.8413, 7.9055, 7.9977, 8.0822]
        y = [f(xi) for xi in x]
        
        coeffs = coeffs_dif_fin(x0, x, 1)
        f_1 = dif_fin(coeffs, y)
        
        coeffs = coeffs_dif_fin(x0, x, 2)
        f_2 = dif_fin(coeffs, y)
        
        coeffs = coeffs_dif_fin(x0, x, 3)
        f_3 = dif_fin(coeffs, y)
        return f(x0) + f_1*(xp - x0) + (f_2/2)*((xp - x0)**2) + (f_3/6)*((xp - x0)**3) 
    
    
    values =   [7.7482, 8.0027, 8.0136]
    px = [p(vi) for vi in values]
    print(f'{px = }')

    fx_menos_px = [np.abs(f(vi) - p(vi)) for vi in values]
    print(f'{fx_menos_px = }')