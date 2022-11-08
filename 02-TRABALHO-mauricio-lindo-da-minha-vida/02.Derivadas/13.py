'''Considere a função f(x)=x**(x**−x). A fórmula F1(h)=f(x0+h)−f(x0)h
é usada para aproximar f′(x0) com erro O(h1). Use o método de extrapolação de Richardson sobre
a fórmula F1 para obter aproximações para f′(1.92541) com erros O(h4), O(h5), O(h6), O(h7) e O(h8).
  Use h=0.32603.'''

import math

def richardson(col_1):
    n = len(col_1)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            numer = 2 ** (i + 1) * col_1[j + 1] - col_1[j]
            denom = 2 ** (i + 1) - 1
            value = numer / denom
            col_1[j] = value
    return col_1[0]

if __name__ == '__main__':

    #exemplo 1

    def func(x):
        return x**(x**-x)

    h =  0.32603
    x0 = 1.92541
  
    err_order = [4, 5, 6, 7, 8]

    def F1(h):
        return (func(x0 + h) - func(x0)) / h
    for i in range(len(err_order)):
        hs = [h, h/2, h/4, h/8]
        col_F1 = [F1(h/2**i) for i in range(err_order[i])]

        approx = richardson(col_F1)

        print(f'{approx}, ')

    richardson(col_F1)