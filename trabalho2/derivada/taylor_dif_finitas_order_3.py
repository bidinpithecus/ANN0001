from methods import *

# x0 = ponto onde a função será derivada
# x = lista de coordenadas na proximidade de x0
# y = cálculo da função em todos os pontos x
# k = ordem da derivada

def f(x):
    return 3 * math.cos((x**2-1)**(1/3))

x0 = 2.5476
x = [2.3485, 2.4235, 2.5312, 2.603, 2.6738, 2.7784]
values = [2.3801, 2.4961, 2.5008]

def p(x0, x, xp):
    y = [f(xi) for xi in x]

    coeffs = coeffs_dif_fin(x0, x, 1)
    f_1 = dif_fin(coeffs, y)

    coeffs = coeffs_dif_fin(x0, x, 2)
    f_2 = dif_fin(coeffs, y)

    coeffs = coeffs_dif_fin(x0, x, 3)
    f_3 = dif_fin(coeffs, y)

    return f(x0) + f_1*(xp - x0) + (f_2/2)*((xp - x0)**2) + (f_3/6)*((xp - x0)**3) 

px = [p(x0, x, vi) for vi in values]
print(f'{px = }')

fx_menos_px = [np.abs(f(vi) - p(x0, x, vi)) for vi in values]
print(f'{fx_menos_px = }')

print("")
print(*printLists(px, fx_menos_px), sep=", ")
