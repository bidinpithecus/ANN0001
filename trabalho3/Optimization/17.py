import math
import numpy as np


def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2


def coef(f,g):
    a = -1.43842
    b = 1.24497
    n = 256
    
    numer = trapz(
        lambda x: (f(x) * g(x) ),
        a,
        b,
        n
    )
    denom = trapz(
        lambda x: g(x) * g(x),
        a,
        b,
        n
    )
    return numer/denom
def coefs_comb(f, funcs):
    a = -1
    b= 1
    n = 256
    list_coefs = []
    for gk in funcs:
        numer = trapz(
            lambda x: f(x) * gk(x),
            a,
            b,
            n
            )
        denom = trapz(
            lambda x: gk(x) * gk(x),
            a,
            b,
            n
                    )
        ck = numer/denom
        list_coefs.append(ck)
    return list_coefs
        
if __name__ == '__main__':
    
    # Exemplo 01:
    # Change 'a', 'n', 'b' inside coef function
    

    def f1(x): return 1
    def f2(x): return x
    def f3(x): return x**2
    def f4(x): return x**3
    
    def g1(x): 
        return f1(x)

    a_21 =  coef(f2, g1)
    print(f'{a_21:.7f},')
    
    def g2(x):
        return f2(x) - a_21*g1(x)
    
    a_31 = coef(f3, g1)
    a_32 = coef(f3, g2)
    print(f'{a_31:.7f},')
    print(f'{a_32:.7f},')
    
    def g3(x): 
        return f3(x) - a_31*g1(x) - a_32*g2(x)
    
    a_41 = coef(f4, g1)
    a_42 = coef(f4, g2)
    a_43 = coef(f4, g3)
    
    print(f'{a_41:.7f},')
    print(f'{a_42:.7f},')
    print(f'{a_43:.7f},')
   
    def g4(x): 
        return f4(x) - a_41*g1(x) - a_42*g2(x) - a_43*g3(x)
    
    
        
        