from methods import *

def f(x):
    return math.sin(x / (math.sqrt(math.pow(x, 2) + 1))) + 1

# Variável inferior, Variável superior
# Lista de subintervalos

intervalo = [-1.013, 1.448]
subintervalos = [1, 24, 43, 60, 75, 102, 235, 420, 558, 917, 1795, 9155]

for i in range(len(subintervalos)):
    r = trapz(f, intervalo[0], intervalo[1], subintervalos[i])
    print(r, end=', ')
print("\n")
