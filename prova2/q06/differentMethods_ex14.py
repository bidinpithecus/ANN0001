from methods import *

'''
A tabela a seguir mostra leituras do velocímetro de um carro, durante um período de 60.0 segundos, numa corrida na Daytona International Speedway, Flórida.
'''

answer = []
x = []
y = []

lista = []

lista.append((0.0, 175.22))
lista.append((5.0, 231.36))
lista.append((10.0, 274.78))
lista.append((15.0, 214.95))
lista.append((20.0, 197.38))
lista.append((25.0, 248.42))
lista.append((30.0, 128.12))
lista.append((35.0, 135.81))
lista.append((40.0, 267.68))
lista.append((45.0, 154.21))
lista.append((50.0, 179.4))
lista.append((55.0, 289.5))
lista.append((60.0, 106.6))

for i in range(len(lista)):
    x.append(lista[i][0] / 3600)
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")
