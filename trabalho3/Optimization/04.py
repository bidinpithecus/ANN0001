from math import *
import numpy as np

# Métodos de integração (necessários para solução do sistema de equações):
def trapeze_sum(f, a, b, n):
    sum = f(a)/2 + f(b)/2
    base = (b-a)/n
    # Lembre-se que x0 = a e xn = b, por isso no seguinte loop k varia de 1 até n-1:
    for k in range(1, n):
        sum += f(a + k*base)
    area = base*sum
    return area

def richardson(f, a, b, n, k):
    # Lembre-se que h = (b-a)/n ; o valor de n é dado indiretamente nas questões...
    table = []
    # Obs.: dada essa função de erro inicial tem-se que Fk(h) diminui o erro para O(h^(2*k))
    k = int(k/2)

    for i in range(k):
        item = trapeze_sum(f, a, b, (2**i)*n)
        table.append(item)

    for i in range(k):
        for j in range(k-i-1):
            new_item = ((4**(i+1))*table[j+1] - table[j])/(4**(i+1) - 1)
            table[j] = new_item
    return table[0]

def simpson(f, a, b, num_subintervals):

    # Obs.: num_intervals(n) é o número de subintervalos, n/2 é o número de parábolas e n+1 é o número de pontos na partição.
    h = (b-a)/num_subintervals
    sum = f(a) + f(b)

    # k varia até 2n
    for k in range(2, num_subintervals, 2):
        sum += 2*f(a + k*h)

    # k varia até 2n-1 (quando k = 2n+1 o loop para)
    for k in range(1, num_subintervals, 2):
        sum += 4*f(a + k*h)

    sum = (h/3)*sum        
    return sum

# Um monte de de funções apenas para a quadratura gaussiana:
def quadrature(f, a, b, cord, coeffs):

    g = change(f, a, b)

    # exact_for_degree_less_than = 24
    # order = str(int(exact_for_degree_less_than/2))    
    # lists_names = ['raiz'+order, 'peso'+order]

    # cord = locals()[lists_names[0]]
    # coeffs = locals()[lists_names[1]]
    
    sum = 0
    for xi, ci in zip(cord, coeffs):
        sum += ci*g(xi)
    return sum

# Transforma string em função:
def stringToFunc(string):
    def f(x):
        return eval(string)
    return f

# Mudança de variável na função f para se encaixar nos limites de integração [-1, 1]:
def change(f, a, b):
    def g(u):
        return f((b+a)/2 + (b-a) * (u/2)) * (b-a)/2
    return g

def aprox_coeffs(func_list, f, a, b, cord, coeffs):
    A = []
    B = []
    # Obs.: note que a matriz A é simétrica portanto não precisamos calcular n² integrais
    for i, fi in enumerate(func_list):
        row = []
        b_i = quadrature(lambda x: f(x)*fi(x), a, b, cord, coeffs)
        for j, fj in enumerate(func_list):
            """
            Note que:
            (1) a_ij = ∫ fj(x)*fi(x) dx;
            (2) visto que a matriz A é simétrica e a parte acima da diagonal é calculada primeiro,
            não é necessário calcular os elementos em que i > j.
            """
            if(i <= j):
                a_ij = quadrature(lambda x: fi(x)*fj(x), a, b, cord, coeffs)
                row.append(a_ij)
            else:
                row.append(A[j][i])
        B.append(b_i)
        A.append(row)
    return np.linalg.solve(A, B)

"""
Observe que são calculadas n integrais na diagonal + [(n-1) + (n-2) + ... + 2 + 1] integrais das diagonais acima + n integras das integrais
na matriz B, o que resulta em n(n+1)/2 + n = (n² + 3n)/2 integrais, o que é mesmo assim uma valor O(n²) apesar da otimização em relação aos
elementos iguais (pela simetria da matriz).
"""

def build_aprox_func(func_list, coeffs):
    def g(x):
        return sum(ck*fk(x) for ck, fk in zip(coeffs, func_list))
    return g

if __name__ == '__main__':
    # Listas de pontos e pesos para quadratura gaussiana:
    from NodesAndWeights import *

    exact_for_degree_less_than = 24
    order = str(int(exact_for_degree_less_than/2))    
    lists_names = ['raiz'+order, 'peso'+order]

    cord = locals()[lists_names[0]]
    coeffs = locals()[lists_names[1]]


    # Exemplo 01:
    func_list = [lambda x: 1, lambda x: x, lambda x: cos(x), lambda x: x**2, lambda x: sin(x), lambda x: x**3, lambda x: cos(2*x),
        lambda x: x**4, lambda x: sin(3*x)]

    def f(x):
        return x * sin(4 * x * cos(log(1 + x**2)))

    a = 0.16304
    b = 2.09243
    # Obs.01: o valor de n não importa aqui pois estaremos usando o método da quadratura gaussiana.
    # Obs.02: k é definido dentro da função para uso do método de Romberg (função 'Richardson').

    coeffs = aprox_coeffs(func_list, f, a, b, cord, coeffs)
    for ck in coeffs: 
        print(f"{ck},")

    g = build_aprox_func(func_list, coeffs)
    values = [0.42967, 1.2785, 1.92429]

    for xi in values:
        print(f"{g(xi)},")

    n = 720
    print(trapeze_sum(lambda x: (f(x)-g(x))**2, a, b, n))

    # t = np.linspace(a, b, 200)
    # ft = [f(ti) for ti in t]
    # gt = [g(ti) for ti in t]

    # plt.plot(t, ft, label = 'function', color = "red")
    # plt.plot(t, gt, label = 'aproximation', color = "green")
    # plt.legend()
    # plt.savefig("Otimização01.png")