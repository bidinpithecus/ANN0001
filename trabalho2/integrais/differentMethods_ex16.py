from methods import *

'''
Em 16 de Maio de 2011 o ônibus espacial Endeavour realizou seu último voo (STS-134) em direção à ISS (International Space Station) com a missão de levar o AMS-2 (Espectômetro Magnético Alpha) e o ELC-3 à estação espacial.
'''

answer = []
x = []
y = []

lista = []
lista.append((0, 0))
lista.append((5, 110))
lista.append((10, 230))
lista.append((15, 364))
lista.append((20, 507))
lista.append((25, 671))
lista.append((30, 821))
lista.append((35, 971))
lista.append((40, 1086))
lista.append((45, 1202))
lista.append((50, 1316))
lista.append((55, 1458))
lista.append((60, 1636))
lista.append((65, 1825))
lista.append((70, 2051))
lista.append((75, 2315))
lista.append((80, 2604))
lista.append((85, 2900))
lista.append((90, 3202))

for i in range(len(lista)):
    x.append(lista[i][0] / 3600)
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")
