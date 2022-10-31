from methods import *

'''Use o método de Romberg, com o h indicado, para encontrar uma aproximação 
com erro O(hk) para as integrais a seguir:'''

def f(nome_funcao, value):
    x = value
    return eval(nome_funcao)

func = ['(x+1/x)**2', 'math.sqrt(1+x**2)', 'math.cos(-x**2/3)', 'math.exp(x)*math.sin(x)/(1+x**2)', 'math.exp(-x**2)']
a = [0.904, 0.066, 0.715, 0.323, -0.97]
b = [1.904, 1.066, 1.715, 1.323, 0.03]
order = [8, 10, 8, 4, 6]
n = [3, 5, 5, 3, 5]

for i in range(len(func)):
    k = int(order[i]/2)
    h = float((b[i]-a[i])/n[i])
    hs = [h/2**i for i in range(k)]
    col1=[trapzRomberg(func[i],a[i],b[i],hi, f) for hi in hs]

    r = romberg(col1)

    print(r,end=", ")
print()