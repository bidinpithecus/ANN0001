'''Um pesquisador relatou os dados tabulados a seguir.
    x = [1.5886, 1.8051, 2.5017, 3.8455, 4.6093, 5.4518, 5.7068, 6.2686, 7.6328, 8.46, 9.2121, 9.9954]
    y = [5.7667, 6.2201, 7.0937, 8.2836, 8.7852, 9.2571, 9.5476, 9.6561, 10.1817, 10.4689, 10.7024, 10.8652]
Sabe-se que tais dados podem ser modelados pela seguinte equação:
    e^(y-b)/a
onde a e b são parâmetros. Use uma transformação para linearizar essa equação e use regressão linear para encontrar os valores de a e b.
Em seguida, calcule o valor de y para os seguintes valores de x:
x1=4.9825, x2=5.1283  e  x3=7.7121
'''

from re import A
import numpy as np

#e^(y-b)/a

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


def poly(x, a, b):
    return a*x*np.exp(b*x)

def build_func(a, b):
    def temp(x):
        return poly(x, a, b)
    return temp


def modelo(x):
    a, b = -40, -30
    erro = a + (b - a) * np.random.random()
    return 2.5 * np.e ** (1.47 * x) + erro

if __name__ == '__main__':

    
    x = [1.5886, 1.8051, 2.5017, 3.8455, 4.6093, 5.4518, 5.7068, 6.2686, 7.6328, 8.46, 9.2121, 9.9954]
    y = [5.7667, 6.2201, 7.0937, 8.2836, 8.7852, 9.2571, 9.5476, 9.6561, 10.1817, 10.4689, 10.7024, 10.8652]
    values = [4.9825, 5.1283, 7.7121] # x1, x2


    #transladar os pontos para cima
    k = abs(min(y)) + 1
    yt = [yi + k for yi in y]

    x_ = np.log(x)

    y_ = y

    grau = 1

    a0, a1 = best_poly(x_, y_, grau)

    #print(f'{a0 = } e {a1 = }')

    a = a1
    b = a0

    print(f'{a = } e {b = }')

    n = len(values)
    somas = []
    for xi in range(n):
        print(f'{a0+a1*np.log(values[xi])}, ')

    p = build_func(a, b)

    def q(x):
        return p(x) - k


'''   import matplotlib.pyplot as plt

    plt.scatter(x, y)

    t = np.linspace(min(x), max(x), 200)
    qt = [q(ti) for ti in t]

    plt.plot(t, qt, color='r')
    plt.savefig('best_exp.png')'''
