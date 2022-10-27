from methods import *

def func(x):
    return math.pow(x, math.pow(x, -x))

h = 0.47503
x0 = 1.53995
orders = [4, 5, 6, 7, 8]

def F1(h):
    return (func(x0 + h) - func(x0)) / h

for j in orders:
    col_F1 = [F1(h/2**i) for i in range(j)]
    aprox = richardson(col_F1)
    print(f'{aprox}', end=", ")
print("")