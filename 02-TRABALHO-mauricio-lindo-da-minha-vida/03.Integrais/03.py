"""A seguinte lista de 7 pontos
(0.166,1.78), (0.619,2.944), (1.815,2.034), (3.408,2.916), (3.892,1.576), 
(4.437,1.663) e (4.552,2.228)
vive no gráfico de uma função f. Use a regra dos trapézios para aproximar a área embaixo 
do gráfico de f no intervalo [0.166,4.552]."""

x = [0.166, 0.619, 1.815, 3.408, 3.892, 4.437, 4.552]

y = [1.78, 2.944, 2.034, 2.916, 1.576, 1.663, 2.228]
soma = 0
xy = zip(x, y)

for a2, b2 in zip(x[1:], y[1:]):  # lista de x e y removidos os primeiros elementos
    for a1, b1 in zip(x, y):
        soma += ((a2-a1) * (b2 + b1))/2.0
        x.pop(0)  # removendo os primeiros elementos das listas de x e y
        y.pop(0)
        break

print('soma de verdade?', soma)