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



def trapz(nome_funcao, a, b, h):
    n = int((b-a)/h)
    soma = 0

    for k in range(1, n):
        soma += f(nome_funcao, a+k*h)

    return (h/2)*(f(nome_funcao, a) + 2*soma + f(nome_funcao, b))


def romberg(coluna_f1):
    coluna_f1 = [i for i in coluna_f1]
    n = len(coluna_f1)
    for j in range(n-1):
        temp_col = [0] * (n-1-j)
        for i in range(n-1-j):
            power = j+1
            temp_col[i] = (4**power*coluna_f1[i+1]-coluna_f1[i])/(4**power-1)
        coluna_f1[:n-1-j] = temp_col
        #print(f'F_{j+2} = {temp_col}')
    return coluna_f1[0]




def f(nome_funcao, value):
    x = value
    return eval(nome_funcao)


if __name__ == '__main__':
    func = ['-x*(x-21)*(x+1)']
    a = [0]
    b = [12]
    h= 12/10
    order = [8] #para obter uma aproximação com erro O(h8)

    for i in range(len(func)):
        k = int(order[i]/2)
        
        hs = [h/2**i for i in range(k)]
        col1=[trapz(func[i],a[i],b[i],hi) for hi in hs]

       # print(f'F_1 = {col1}')

        r = romberg(col1)

        print(f'{r}')
        