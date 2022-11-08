import numpy as np
'''
Encontre os coeficientes a e b da função potência y=ax^b que melhor se aproxima da seguinte lista de 12 pontos
(0.6168,1.2651)...
'''

def best_poly(x, y, grau=1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if p == 0:
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi**p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi*xi**i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)


def poly(x, a, b):
    return a*x**b


def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


if __name__ == '__main__':
    x = [0.6204, 0.8714, 0.9374, 1.2327, 1.479, 1.6638, 1.7679, 2.1347, 2.31, 2.4158, 2.7491, 2.947]
    y = [0.8178, 1.0021, 0.9138, 2.3883, 4.7, 7.5698, 8.7714, 16.6828, 22.282, 25.6845, 40.0082, 49.9559]
    values = [0.8966, 1.763, 1.7663]
    if min(y) <= 0:
        k1 = abs(min(y)) + 1
    else:
        k1 = 0

    if min(x) <= 0:
        k2 = abs(min(x)) + 1
    else:
        k2 = 0

    yt = [yi + k1 for yi in y]

    y_ = np.log(yt)

    xt = [xi + k2 for xi in x]

    x_ = np.log(xt)

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    a = np.exp(a0)

    b = a1

    print('Coeficientes da reta')
    print(f'{a0 = } e {a1 = }')

    print('Coeficientes da potencia')
    print(f'{a = } e {b = }')

    p = build_func(a, b)

    def q(x):
        return p(x+k2) - k1

    for value in values:
        print(f'{q(value)}, ')

    # visualização

   # import matplotlib.pyplot as plt

   # plt.scatter(x, y)

    #t = np.linspace(min(x), max(x), 200)
    #qt = [q(ti) for ti in t]

    #plt.plot(t, qt)

    #plt.savefig('best_poly_regressao_potencia.png')