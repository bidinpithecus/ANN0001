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
    func = ['math.sqrt((9.81*67.26)/(0.42))*math.tanh(math.sqrt((9.81*(0.42))/67.26)*x)']
    a = [0]
    b = [10.76]
    h= 10.76/10.0
    order = [8] #para obter uma aproximação com erro O(h8)

    for i in range(len(func)):
        k = int(order[i]/2)
        
        hs = [h/2**i for i in range(k)]
        col1=[trapz(func[i],a[i],b[i],hi) for hi in hs]

       # print(f'F_1 = {col1}')

        r = romberg(col1)

        print(f'{r}')
        