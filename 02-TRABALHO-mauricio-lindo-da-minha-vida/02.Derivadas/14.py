from cmath import cos, e
import math

'''Considere a função f(x)=cos(sin(ln(x2))). Os valores
F1(h)=0.0837775004374346, F1(h/2)=0.11855055487505517  e  F1(h/4)=0.13420867214887622
são aproximações para f′(2.4507) com erro O(h1). 
Use o método de extrapolação de Richardson para encontrar uma aproximação com erro O(h3) para f′(2.4507).'''

def richardson(col1):
    col1 = [item for item in col1]
    n = len(col1)
    for j in range(n - 1):
        temp_col = [0] * (n-1-j)
        for i in range(n - 1 - j):
            power = j + 1
            temp_col[i] = (2 ** power * col1[i+1] - col1[i]) / (2 ** power - 1)
        col1[:n - 1 - j] = temp_col
        print(temp_col)
    return col1[0]


def func(x):
    return math.cos(math.sin(math.log(x**2)))


if __name__ == '__main__':

    x0 = 2.4507
    approximations = [0.0837775004374346, 0.11855055487505517, 0.13420867214887622]
    aprox = richardson(approximations)

    print(f'{aprox = }')