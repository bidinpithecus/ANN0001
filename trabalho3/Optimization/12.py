import math
import numpy as np

def simps(f, a, b, n):
    if n % 2 != 0 or n < 1:
        raise ValueError("n deve ser par e maior que 1")

    h = (b - a) / n
    soma_odd, soma_even = 0, 0
    for k in range(1, n , 2):
        soma_odd += f(a + k * h)
    for k in range(2, n, 2):
        soma_even += f(a + k * h)
    return (f(a) + 4 * soma_odd + 2 * soma_even + f(b)) * (h / 3)

def romberg(x, b=1):
    n = len(x)
    for k in range(1, n):
        for i in range(n - k):
            numer = 4 ** (b * k) * x[i + 1] - x[i]
            denom = 4 ** (b * k) - 1
            x[i] = numer/denom
    return x[0]

def trapz(f, a, b, h):
    n = int((b - a) / h)
    soma = 0
    for k in range(1, n):
        soma += (f(a +  k * h))
    soma *= 2
    soma += (f(a) + f(b))
    return soma * (h / 2)


def T(n, x):
    return math.cos(n * math.acos(x))

def aprox(f, f_list):
    n = len(f_list)
    A = [[0 for _ in range(n)] for _ in range(n)] # A é simetrica
    B = []
    for i in range(n):
        for j in range(i, n):
            def f_ji(x):
                return f_list[j](x) * f_list[i](x)
            
            # altere dependendo do metodo de integração
            a = -1
            b = 1
            a_ij = simps(f_ji, a, b, 4096)
            
            A[i][j] = a_ij
            A[j][i] = a_ij
        
        def ff_i(x):
            return f(x) * f_list[i](x)
        
        # altere dependendo do metodo de integração
        a = -1
        b = 1
        b_i = simps(ff_i, a, b, 4096)

        B.append(b_i)
    
    return np.linalg.solve(A, B)

def build_g(coeffs, f_list):
    def func(x):
        soma = 0
        for c, f in zip(coeffs, f_list):
            soma += c * f(x)
        return soma
    return func

if __name__ == "__main__":
    def f(x):
        return x * math.cos(10 * x**2 * math.exp(-x**2))
    #quantidade de c
    f_list = [
        lambda x: T(0, x),
        lambda x: T(1, x),
        lambda x: T(2, x),
        lambda x: T(3, x),
        lambda x: T(4, x),
        lambda x: T(5, x),
        lambda x: T(6, x),
        lambda x: T(7, x),
        lambda x: T(8, x),
        lambda x: T(9, x)
    ]
    a = -1
    b = 1
    values = [-0.917, -0.059, 0.514]

    coeffs = aprox(f, f_list)
    g = build_g(coeffs, f_list)

    for c in coeffs:
        print(f"{c},")
    
    for v in values:
        print(f"{g(v)},")

    def f_erro(x):
        return (f(x) - g(x)) ** 2


    h = (b-(a))/10
    erro_da_ordem = int(8/2)
    hs = [h / 2 ** i for i in range(erro_da_ordem)]
    col1 = [trapz(f_erro, a, b, hi) for hi in hs]
   
    r = romberg(col1)
    print(r)
    