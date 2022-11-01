from methods import *

'''
Em uma pessoa contaminada com sarampo, o nível de vírus N (medido em número de células infectadas por mL de plasma de sangue) atinge um pico em cerca de t=12 dias (quando aparecem erupções cutâneas) e, então, diminui bem rápido como resultado da resposta imunológica. A área sob o gráfico de N(t) de t=0 a t=12 (como mostrado na figura) é igual à quantidade total de infecção necessária para desenvolver sintomas (medida em densidade de células infectadas x tempo). A função N tem sido modelada pela função
f(t)=-t(t-21)(t+1)
a) a regra dos trapézios com 31 subintervalos
b) a regra de Simpson com 14 subintervalos
c) o método de Romberg com h=12/10 para obter uma aproximação com erro O(h8)
d) o método da Quadratura Gaussiana que seja exato em polinômios de grau menor que 6 estime a quantidade total de infecção necessária para desenvolver os sintomas de sarampo.
'''

def f(nome_funcao, value):
	x = value
	return eval(nome_funcao)

def change(nome_funcao, a, b):
	def g(u):
		return f(nome_funcao, (b+a)/2 + (b-a)*u/2) * (b-a)/2
	return g

answer = []
a = [0]
b = [12]
order = [8]
n = [10]
exact_for_degree_less_than = [6]
subintervalosTrapezio = 31
subintervalosSimpson = 14

funcs = ['-x*(x-21)*(x+1)']

def F(x):
	return -x*(x-21)*(x+1)

answer.append(trapz(F, a[0], b[0], subintervalosTrapezio))
answer.append(simps(F, a[0], b[0], subintervalosSimpson))

for i in range(len(funcs)):
	k = int(order[i]/2)
	h = float((b[i]-a[i])/n[i])
	hs = [h/2**i for i in range(k)]
	col1 = [trapzRomberg(funcs[i], a[i], b[i], hi, f) for hi in hs]

	answer.append(romberg(col1))

for i in range(len(funcs)):
	order = str(int(exact_for_degree_less_than[i]/2))
	txt_order = ['raiz'+order, 'peso'+order]
	r = quadratura(change(funcs[i], a[i], b[i]), locals()[txt_order[0]], locals()[txt_order[1]])
	answer.append(r)

print(*answer, sep=", ")
