"""Considere a função f(x)=x2e−xcos(x)+1. Os valores
F1(h)=−0.36325385138041444, F1(h/2)=−0.3448908856994688, F1(h/4)=−0.33542332912868744, 
F1(h/8)=−0.3306253663515193, F1(h/16)=−0.32821124852392813  e  F1(h/32)=−0.327000518687953
são aproximações para f′(2.33977) com erro O(h1). Use o método de 
extrapolação de Richardson para encontrar uma aproximação com erro O(h6) para f′(2.33977)."""

from cmath import cos, e
import math


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
    return x**2 * math.exp(-x)*math.cos(x)+1


if __name__ == '__main__':

    x0 = 2.33977
    approximations = [-0.36325385138041444, -0.3448908856994688, -0.33542332912868744, -0.3306253663515193, -0.32821124852392813, -0.327000518687953]
    aprox = richardson(approximations)

    print(f'{aprox = }')