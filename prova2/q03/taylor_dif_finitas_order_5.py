from methods import *

def f(x):
    return x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)

x0 = -1.5363
order = 5
x = [-1.7386, -1.7041, -1.6477, -1.5938, -1.5583, -1.5062, -1.4464, -1.4021, -1.3684, -1.2915]
values = [-1.7142, -1.4662, -1.4457]
order1 = 1
order2 = 2
order3 = 3
order4 = 4
order5 = 5

p = 0
n = len(values)
for i in range(n):
    p = f(x0) + finite_diffs(x, order1, x0, f)*(values[i] - x0) + ((finite_diffs(x, order2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(x, order3, x0, f)/6) * ((values[i]-x0)**3)) + ((finite_diffs(x, order4, x0, f)/24) * ((values[i]-x0)**4)) + ((finite_diffs(x, order, x0, f)/120) * ((values[i]-x0)**5)) 
    erroN = abs(f(values[i]) - p)
    print(f'{p}, {erroN}', end=", ")
print("")
