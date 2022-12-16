# Questão 17 de otimização muito pior kkkkkkkkkkk
import math
import numpy as np


def trapz(f, a, b, n):
    h = abs(b - a) / n
    sum_fx = 0

    for i in range(1, n):
        sum_fx += f(a + i * h)

    return (f(a) + 2 * sum_fx + f(b)) * h / 2


def coef(f,g):
    a = -1.0786
    b = 1.06651
    n = 500
    
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
    def f5(x): return x**4
    def f6(x): return x**5
    def f7(x): return x**6
    def f8(x): return x**7
    def f9(x): return x**8
    def f10(x): return x**9
    
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
    
    a_51 = coef(f5, g1)
    a_52 = coef(f5, g2)
    a_53 = coef(f5, g3)
    a_54 = coef(f5, g4)
    
    print(f'{a_51:.7f},')
    print(f'{a_52:.7f},')
    print(f'{a_53:.7f},')
    print(f'{a_54:.7f},')
   
    def g5(x): 
        return f5(x) - a_51*g1(x) - a_52*g2(x) - a_53*g3(x) - a_54*g4(x)
    
    a_61 = coef(f6, g1)
    a_62 = coef(f6, g2)
    a_63 = coef(f6, g3)
    a_64 = coef(f6, g4)
    a_65 = coef(f6, g5)
    
    print(f'{a_61:.7f},')
    print(f'{a_62:.7f},')
    print(f'{a_63:.7f},')
    print(f'{a_64:.7f},')
    print(f'{a_65:.7f},')
   
    def g6(x): 
        return f6(x) - a_61*g1(x) - a_62*g2(x) - a_63*g3(x) - a_64*g4(x) - a_65*g5(x)
    
    a_71 = coef(f7, g1)
    a_72 = coef(f7, g2)
    a_73 = coef(f7, g3)
    a_74 = coef(f7, g4)
    a_75 = coef(f7, g5)
    a_76 = coef(f7, g6)
    
    print(f'{a_71:.7f},')
    print(f'{a_72:.7f},')
    print(f'{a_73:.7f},')
    print(f'{a_74:.7f},')
    print(f'{a_75:.7f},')
    print(f'{a_76:.7f},')
   
    def g7(x): 
        return f7(x) - a_71*g1(x) - a_72*g2(x) - a_73*g3(x) - a_74*g4(x) - a_75*g5(x) - a_76*g6(x)
    
    a_81 = coef(f8, g1)
    a_82 = coef(f8, g2)
    a_83 = coef(f8, g3)
    a_84 = coef(f8, g4)
    a_85 = coef(f8, g5)
    a_86 = coef(f8, g6)
    a_87 = coef(f8, g7)
    
    print(f'{a_81:.7f},')
    print(f'{a_82:.7f},')
    print(f'{a_83:.7f},')
    print(f'{a_84:.7f},')
    print(f'{a_85:.7f},')
    print(f'{a_86:.7f},')
    print(f'{a_87:.7f},')
   
    def g8(x): 
        return f8(x) - a_81*g1(x) - a_82*g2(x) - a_83*g3(x) - a_84*g4(x) - a_85*g5(x) - a_86*g6(x) - a_87*g7(x)
    
    a_91 = coef(f9, g1)
    a_92 = coef(f9, g2)
    a_93 = coef(f9, g3)
    a_94 = coef(f9, g4)
    a_95 = coef(f9, g5)
    a_96 = coef(f9, g6)
    a_97 = coef(f9, g7)
    a_98 = coef(f9, g8)
    
    print(f'{a_91:.7f},')
    print(f'{a_92:.7f},')
    print(f'{a_93:.7f},')
    print(f'{a_94:.7f},')
    print(f'{a_95:.7f},')
    print(f'{a_96:.7f},')
    print(f'{a_97:.7f},')
    print(f'{a_98:.7f},')
   
    def g9(x): 
        return f9(x) - a_81*g1(x) - a_82*g2(x) - a_83*g3(x) - a_84*g4(x) - a_85*g5(x) - a_86*g6(x) - a_87*g7(x)
    
    a_10_1 = coef(f10, g1)
    a_10_2 = coef(f10, g2)
    a_10_3 = coef(f10, g3)
    a_10_4 = coef(f10, g4)
    a_10_5 = coef(f10, g5)
    a_10_6 = coef(f10, g6)
    a_10_7 = coef(f10, g7)
    a_10_8 = coef(f10, g8)
    a_10_9 = coef(f10, g9)
    
    print(f'{a_10_1:.7f},')
    print(f'{a_10_2:.7f},')
    print(f'{a_10_3:.7f},')
    print(f'{a_10_4:.7f},')
    print(f'{a_10_5:.7f},')
    print(f'{a_10_6:.7f},')
    print(f'{a_10_7:.7f},')
    print(f'{a_10_8:.7f},')
    print(f'{a_10_9:.7f},')
