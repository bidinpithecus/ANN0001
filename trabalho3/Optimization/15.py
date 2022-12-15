import numpy as np



def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * (h / 2)


def simps(f, a, b, n):
    if n % 2 != 0:
        print('O valor n deve ser par')
        return None

    num_parabolas = n / 2
    soma = 0
    h = (b - a) / n

    for i in range(int(num_parabolas)):
        x0 = a + (2 * i) * h
        x1 = a + (2 * i + 1) * h
        x2 = a + (2 * i + 2) * h
        soma += f(x0) + 4 * f(x1) + f(x2)

    soma *= h / 3

    return soma


def trapz_romberg(f, a, b, h):
    n = int((b - a) / h)
    soma = 0

    for k in range(1, n):
        soma += f(a + k * h)

    return (h / 2) * (f(a) + 2 * soma + f(b))


def romberg(coluna_f1):
    coluna_f1 = [i for i in coluna_f1]
    n = len(coluna_f1)
    for j in range(n - 1):
        temp_col = [0] * (n - 1 - j)
        for i in range(n - 1 - j):
            power = j + 1
            temp_col[i] = (4 ** power * coluna_f1[i + 1] - coluna_f1[i]) / (4 ** power - 1)
        coluna_f1[:n - 1 - j] = temp_col
        # print(f'F_{j+2} = {temp_col}')
  
    return coluna_f1[0]


def quadratura(funcao, pontos, pesos):
    soma = 0

    for xk, ck in zip(pontos, pesos):
        soma += ck * funcao(xk)

    return soma


def change(f, a, b):
    def g(u):
        return f((b + a) / 2 + (b - a) * u / 2) * (b - a) / 2

    return g

def produto_escalar(f1, f2, w, a, b, method):
  
  def func(x):
    return f1(x) * f2(x) * w(x)

  if method[0] == 'trapz':
      return trapz(func, a, b, method[1])
  elif method[0] == 'simps':
      return trapz(func, a, b, method[1])
  elif method[0] == 'romberg':
      tam = int(method[1] / 2)
      hs = [method[2] / 2 ** ki for ki in range(tam)]
      coluna_f1 = [trapz_romberg(func, a, b, hi) for hi in hs]
      return romberg(coluna_f1)
  elif method[0] == 'quadratura':
      return quadratura(change(func, a, b), method[1], method[2])
  

if __name__ == '__main__':
    def f1(x): return x**2
    
    def f2(x): return np.cos(3*x) 
    
    def w(x): return 1
    # Exemplo 01:
    values = [-0.967,1.071]
    a = values[0]
    b = values[1]
    n = 256
    method = ['trapz', n]
    
    
    
    
    print(produto_escalar(f1,f2,w,a,b,method))