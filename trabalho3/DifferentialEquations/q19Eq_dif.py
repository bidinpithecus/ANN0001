""" Uma das primeiras tentativas de modelar o crescimento de uma população por meio de equações matemáticas foi realizada pelo economista inglês Thomas Malthus (1766-1834) em 1798. A ideia por trás do modelo Malthusiano é de que a taxa de crescimento da população de um país é proporcional à população total P daquele país. Em termos matemáticos, se P(t) denota a população total num tempo t (em anos), então a ideia acima pode ser expressa usando a seguinte equação diferencial
dPdt=kP,
em que k é uma constante de proporcionalidade. Assuma que a população de um país em t=0 seja de 1763761 indivíduos e que k=0.0648. Use o método de Euler para estimar o número de indivíduos nessa população após 1 ano. Use tamanho do passo h=0.0625. """

def true_euler(f, k, x0, y0, h, n):
    for i in range(n):
        y0 += h * f(x0, y0, k)
        x0 += h        
        print(f'x_{i + 1} = {x0} e y_{i+1} = {y0}')

def euler(f, x0, y0, h, n):
    vals = []
    for k in range(n):
        x0 += h
        xk = x0 + k*h
        y0 += h * f(xk, y0)
        vals.append([xk,y0])
    return vals

def euler_mid(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + h / 2, y0 + (h / 2) * m1)
        y0 = y0 + h * m2
        x0 += h
        yield x0, y0

if __name__ == '__main__':
    def f(x, y, k):
        # y = P
        return k*y
    # t == x
    x0, y0 = 0.0, 1199787 # x0 = t, y0 = individuos
    h = 0.0625
    k = 0.07635
    n = int(1 / h)
    r1 = true_euler(f, k, x0, y0, h, n)
    #print(r1)
    #x1, y1 = zip(*r1)
    #print(y1)

    #r2 = euler_mid(f, x0, y0, h, n)
    #x2, y2 = zip(*r2)
    #print(y2)

    #plot 
    """
   Uma das primeiras tentativas de modelar o crescimento de uma população por 
   meio de equações matemáticas foi realizada pelo economista inglês
   Thomas Malthus (1766-1834) em 1798. A ideia por trás do modelo Malthusiano
   é de que a taxa de crescimento da população de um país é proporcional à 
   população total P daquele país. Em termos matemáticos, se P(t) denota a 
   população total num tempo t (em anos), então a ideia acima pode ser expressa 
   usando a seguinte equação diferencial
                dPdt=kP,
    em que k é uma constante de proporcionalidade. Assuma que a população de um país 
    em t=0 seja de 1086709 indivíduos e que k=0.02249 Use o método de Euler para 
    estimar o número de indivíduos nessa população após 1 ano. 
    Use tamanho do passo h=0.0625.
    """