import numpy as np

# best line
def bestLine(x, y):
	n = len(x)
	sum_x1 = sum(x)
	sum_x2 = sum(xi ** 2 for xi in x)
	sum_y = sum(y)
	sum_xy = sum(yi * xi for xi,yi in zip(x,y))
	A = [[n,sum_x1],[sum_x1,sum_x2]]
	B = [sum_y, sum_xy]
	return np.linalg.solve(A, B)

# best poly, which serves for polynoms with a degree k
def best_poly (x, y, k):
    n = len(x)
    if n <= k:
        raise ValueError('O número de pontos deve ser maior que k (o grau do polinômio)')
    A_printado = []
    somas = {}
    somas[0] = n
    for n in range(1, 2*k + 1):
        somas[n] = sum(xi ** n for xi in x)
    A = []
    B = []
    for i in range (k + 1):
        row = []
        for j in range(k + 1):
            row.append(somas[i + j])
            A_printado.append(somas[i+j])
        A.append(row)
        if i == 0:
            B.append(sum(y))
        else:
            B.append(sum(xi ** i * yi for xi, yi in zip(x,y)))
    print('Matriz A:\n',A_printado,'\n''Matriz B:\n',B)
    return A_printado, B, np.linalg.solve(A, B)

def best_poly_func_exp(x, y, grau = 1):
    k = grau + 1
    A = [[0 for _ in range(k)] for _ in range(k)]
    B = [sum(y)]
    n = len(x)
    cache = {}
    for i in range(k):
        for j in range(k):
            p = i + j
            if (p == 0):
                A[0][0] = n
                continue
            if p not in cache:
                cache[p] = sum([xi ** p for xi in x])
            A[i][j] = cache[p]
        if i > 0:
            B.append(sum([yi * xi ** i for xi, yi in zip(x, y)]))
    return np.linalg.solve(A, B)