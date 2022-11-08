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
    x = [0.5571, 0.6083, 0.6389, 0.6974, 0.7488, 0.8159, 0.9132, 0.9264, 1.01, 1.0897, 1.1172, 1.163, 1.2535, 1.2752, 1.3398, 1.4272, 1.4578, 1.5581, 1.5734, 1.674, 1.7475, 1.7674, 1.8672, 1.9157, 1.9299, 2.0253, 2.0971, 2.117, 2.2164, 2.2438, 2.3043, 2.3849, 2.4322, 2.5, 2.5257, 2.6089, 2.683, 2.7091, 2.8034, 2.832, 2.8974, 2.9779]
    y = [0.3602, 0.0236, 0.4075, 0.9458, 0.5819, 1.6969, 1.0105, 1.1053, 0.9955, 0.9878, 1.2936, 1.7391, 2.0701, 2.2867, 2.8038, 4.2057, 2.5034, 5.1754, 5.5421, 7.3665, 8.1594, 8.9967, 11.0802, 12.1991, 12.0209, 15.02, 17.4119, 17.2787, 21.6507, 22.6346, 24.3772, 26.5717, 30.2719, 33.3808, 34.5565, 39.8752, 44.2991, 45.1402, 52.0053, 54.3722, 58.132, 66.3003]
    values = [1.5179, 2.3039, 2.5981, 2.6125, 2.7997]
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