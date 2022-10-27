from methods import *
from math import *

x = [0.0242, 0.063, 0.1259, 0.2094, 0.2472, 0.3178, 0.3794, 0.3902, 0.4911, 0.5299, 0.6051, 0.632, 0.7124, 0.7476, 0.8219, 0.881, 0.933, 0.9998, 1.0444, 1.1037, 1.1361, 1.1735, 1.2424, 1.2953, 1.3384, 1.4148, 1.4532, 1.535, 1.5717, 1.6195, 1.6931, 1.7604, 1.8203, 1.8449, 1.9372, 1.9905]
y = [6.0753, 4.9604, 4.6976, 4.6657, 5.4298, 5.3477, 7.7704, 7.8364, 6.9452, 7.4926, 8.4301, 8.8666, 8.6262, 8.9909, 10.6774, 12.2682, 12.5547, 12.7918, 14.5589, 16.033, 14.6447, 14.9656, 16.0489, 17.5833, 18.1583, 20.2182, 21.4428, 22.5895, 23.5618, 23.3029, 27.3499, 30.2039, 32.2731, 32.633, 36.6516, 38.191]
values = [0.4071, 1.0255, 1.2649, 1.5162, 1.886]

#linearização, transformando x em ln(x)

for i in range(0, len(x)):
    x[i] = log(x[i])

matrizA = []
matrizB = []
listPol = []
matrizA, matrizB, listPol = best_poly(x, y, 1)
b, a = listPol

print('Coefs:\n',f'{a}, {b}', end=',')

def p(x, a, b):
	return a * log(x) + b

print()
print('Values:')
for value in values:
    print(f' {(p(value, a, b))}', end=", ")
print("")
print("\n\nPARA INSERIR\n")
print(f'{a}, {b}', end=', ')
for value in values:
    print(f'{(p(value, a, b))}', end=", ")
print("")