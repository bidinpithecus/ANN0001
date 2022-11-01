from methods import *

'''
Óleo vaza de um tanque a uma taxa de r(t) litros por hora. A taxa decresce à medida que o tempo passa, conforme mostrado na tabela a seguir.
'''

answer = []
x = []
y = []

lista = []
lista.append((0.0, 9.89))
lista.append((0.75, 9.3))
lista.append((1.5, 8.88))
lista.append((2.25, 8.61))
lista.append((3.0, 8.0))
lista.append((3.75, 7.58))
lista.append((4.5, 7.23))
lista.append((5.25, 6.87))
lista.append((6.0, 6.41))
lista.append((6.75, 6.12))
lista.append((7.5, 5.55))
lista.append((8.25, 5.25))
lista.append((9.0, 4.97))
lista.append((9.75, 4.29))
lista.append((10.5, 4.08))
lista.append((11.25, 3.48))
lista.append((12.0, 3.06))

for i in range(len(lista)):
    x.append(lista[i][0])
    y.append(lista[i][1])

answer.append(trapzPonto(x, y))
answer.append(simpsPonto(x, y))

print(*answer, sep=", ")
