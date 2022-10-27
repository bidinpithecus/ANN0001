from methods import *

def f(x):
    return math.log(2 + math.cos(math.exp(-x)))

x0 = 0.744
order = 4
x = [0.5286, 0.5746, 0.6517, 0.7214, 0.7893, 0.8419, 0.8752, 0.9649]
values = [0.6589, 0.7913, 0.8828, 0.8969]

order1 = 1
order2 = 2
order3 = 3
order4 = 4

p = 0
n = len(values)
for i in range(n):
    p = f(x0) + finite_diffs(x, order1, x0, f)*(values[i] - x0) + ((finite_diffs(x, order2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(x, order3, x0, f)/6) * ((values[i]-x0)**3))  + ((finite_diffs(x, order4, x0, f)/24) * ((values[i]-x0)**4))
    erroN = math.sqrt(((f(values[i]) - p)**2))
    print(f'{values[i]} = {p} e |f(x) - p3(x)| = {erroN}')

num_pontos = 0
a = x0 - 0.25
b = x0 + 0.25

print("")
for i in range(n):
    p = f(x0) + finite_diffs(x, order1, x0, f)*(values[i] - x0) + ((finite_diffs(x, order2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(x, order3, x0, f)/6) * ((values[i]-x0)**3))  + ((finite_diffs(x, order4, x0, f)/24) * ((values[i]-x0)**4))
    erroN = math.sqrt(((f(values[i]) - p)**2))
    print(f'{p}, {erroN}', end=", ")
print("")