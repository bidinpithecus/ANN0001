from methods import *

def f(x):
    return math.sqrt(math.sin(math.cos(math.log(math.pow(x, 2) + 1) + 2) + 3) + 4)

intervalo = [-1.829, 1.196]
subintervalos = [4, 14, 46, 72, 90, 114, 128, 164, 184, 234, 304]

n = len(subintervalos)
for i in range(n):
    print(simps(f, intervalo[0], intervalo[1], subintervalos[i]), end=", ")
print()
