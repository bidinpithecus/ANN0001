import math

'''Use o método de Romberg, com o h indicado, para encontrar uma aproximação 
com erro O(hk) para as integrais a seguir:'''

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
    func = ['math.exp(-x**2)', '(x+1/x)**2', 'math.sqrt(1+x**2)', 'math.cos(-x**2/3)', 'math.exp(x)*math.sin(x)/(1+x**2)']
    a = [-1.265, 0.839, 0.305, 0.249, 0.484]
    b = [-0.265, 1.839, 1.305, 1.249, 1.484]
    order = [6, 4, 10, 10, 10]
    n = [5, 5, 4, 2, 3]

    for i in range(len(func)):
        k = int(order[i]/2)
        h = float((b[i]-a[i])/n[i])
        hs = [h/2**i for i in range(k)]
        col1=[trapz(func[i],a[i],b[i],hi) for hi in hs]

       # print(f'F_1 = {col1}')

        r = romberg(col1)

        print(f'{r}, ')