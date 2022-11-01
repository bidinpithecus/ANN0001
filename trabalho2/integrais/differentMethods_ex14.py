from methods import *

'''
A tabela a seguir mostra leituras do velocímetro de um carro, durante um período de 60.0 segundos, numa corrida na Daytona International Speedway, Flórida.
'''

answer = []
x = []
y = []

lista = []
lista.append((0.0, 181.57))
lista.append((5.0, 271.31))
lista.append((10.0, 117.14))
lista.append((15.0, 296.41))
lista.append((20.0, 199.66))
lista.append((25.0, 143.71))
lista.append((30.0, 169.91))
lista.append((35.0, 264.43))
lista.append((40.0, 212.2))
lista.append((45.0, 151.29))
lista.append((50.0, 226.61))
lista.append((55.0, 247.89))
lista.append((60.0, 109.43))

for i in range(len(lista)):
    x.append(lista[i][0] / 3600)
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")
