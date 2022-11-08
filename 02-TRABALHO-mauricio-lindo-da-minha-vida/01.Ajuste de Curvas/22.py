import numpy as np

#BEST_POLY

#FUNC EQUIVALENTE
# y = ((a + sqrt(x)/b sqrt (x))^2
# sqrt( y ) = 1/b + a/b * 1/sqrt( x )

"""Um pesquisador relatou os dados tabulados a seguir.
Sabe-se que tais dados podem ser modelados pela seguinte equação:
    y=(a+√x/√x * b)^2
"""
def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p=i+j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, coefs):
    s = coefs[0]
    for i, ci in enumerate(coefs[1:], 1):
        s += ci * x ** i
    return s

def build_func(coefs):
    def temp(x):
        return poly(x, coefs)
    return temp


def modelo(x):
    a, b = -10, 10
    erro = a + (b - a) * np.random.random()
    return 2 + 2.34 * x - 1.86 * x ** 2 - 3.21 * x ** 3 + erro


if __name__ == '__main__':
    

    x = [0.9197, 1.7216, 2.7227, 3.3103, 3.6818, 4.7897, 5.7298, 6.3204, 7.2283, 7.7483, 8.4684, 9.4994]
    y = [9.258, 5.6163, 4.0148, 3.4187, 3.2098, 2.6647, 2.3125, 2.1707, 2.0569, 1.9618, 1.7852, 1.7686]
    values = [7.5731, 9.0728, 9.4366]

    y_ = np.sqrt(y)
    
    x_ = 1/np.sqrt(x)

    grau = 1

    coefs = best_poly(x_, y_, grau)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    b = 1/a0
    a = a1 * b

    p = build_func(coefs)

    n = len(coefs)

    '''for xi in range(n):
        print(f'a{xi} = [{coefs[xi]}]')'''

    print(f'a = {a} b = {b}')

    n = len(values)
    for xi in range(n):
        print(f'{(a0 + a1 * 1/np.sqrt(values[xi]))**2}, ')


'''   import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    pt = [p(ti) for ti in t]

    plt.plot(t, pt)
    plt.savefig('best_poly.png')
'''