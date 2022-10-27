from methods import *

def f(x):
    return x**2 * math.cos(x - 1) * math.exp(-3 * x ** 2)

x0 = 0.7496
order = 5
x = [0.5173, 0.5952, 0.6348, 0.6792, 0.7273, 0.7895, 0.8299, 0.8954, 0.9145, 0.9648]
values = [0.5275, 0.5761, 0.7147, 0.7285, 0.7419]
order1 = 1
order2 = 2
order3 = 3
order4 = 4
order5 = 5

p = 0
n = len(values)
for i in range(n):
    p = f(x0) + finite_diffs(x, order1, x0, f)*(values[i] - x0) + ((finite_diffs(x, order2, x0, f)/2) * ((values[i]-x0)**2)) + ((finite_diffs(x, order3, x0, f)/6) * ((values[i]-x0)**3)) + ((finite_diffs(x, order4, x0, f)/24) * ((values[i]-x0)**4)) + ((finite_diffs(x, order, x0, f)/120) * ((values[i]-x0)**5)) 
    erroN = math.sqrt(((f(values[i]) - p)**2))
    print(f'{p}, {erroN}', end=", ")
print("")
