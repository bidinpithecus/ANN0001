from methods import *

'''
Suponha que a força de resistência do ar sobre um objeto
em queda livre é proporcional ao quadrado da velocidade. 
Neste caso, a velocidade pode ser calculada usando-se
'''

def f(nome_funcao, value):
    x = value
    return eval(nome_funcao)
    
def change(nome_funcao, a, b):
    def g(u):
        return f(nome_funcao, (b+a)/2 + (b-a)*u/2) * (b-a)/2
    return g


funcs = ['math.sqrt(({g}*{m})/({cd}))*math.tanh(math.sqrt(({g}*({gc}))/{m})*x)']
a = [0]
b = [9.87]
g = '9.81'
m = '76.55'
cd = '0.22'

exact_for_degree_less_than = [10]
for i in range(len(funcs)):
    order = str(int(exact_for_degree_less_than[i]/2))
    txt_order = ['raiz'+order, 'peso'+order]
    r = quadratura(change(funcs[i], a[i], b[i]), locals()[txt_order[0]], locals()[txt_order[1]])
    print(f'{r = }\n')
