"""Considere o seguinte PVI
y′=y(2−x)+x+1,y(x0)=y0,
com x0=0.26939 e y0=1.68556. Use o método de Heun para estimar o valor da solução exata desse PVI nos pontos
x1=0.31053, x2=0.35252, x3=0.3787, x4=0.44592, x5=0.50917, x6=0.5509, x7=0.60043, x8=0.6391, x9=0.69363, x10=0.75313, x11=0.79533, x12=0.84201, x13=0.87618, x14=0.92892, x15=0.988, x16=1.06191, x17=1.11304, x18=1.1463, x19=1.20006 e x20=1.23062."""



def heun(f,x0,y0,h,n,x_values):
    for k in range(1,n):
        m1 = f(x0,y0)
        m2 = f(x0 + h, y0 + h * m1)
        y0 += h * (m1+m2) / 2
        h = x_values[k] - x_values[k-1]
        x0 = x_values[k-1]
        yield[x0,y0]

    m1 = f(x0,y0)
    m2 = f(x0 + h, y0 + h * m1)
    y0 += h * (m1+m2) / 2
    h = x_values[n-1] - x_values[n-2]
    x0 = x_values[k-1]
    yield[x0,y0]

if __name__ == '__main__':
    #usar o wolpram alpha como resolvedor de equacoes diferencias.

    def f(x,y):
        func = y * (2 - x) + x + 1
        return func

    
    x0 = 0.70039
    y0 = 0.51423
    x_values = [0.7252, 0.76628, 0.82558, 0.85709, 0.94367, 0.97162, 1.01663, 1.06113, 1.13734, 1.18461, 1.21231, 1.27561, 1.33116, 1.37807, 1.40821, 1.46392, 1.54334, 1.55922, 1.6087, 1.67421]
    n = 20 # nmro de iteracoes

    h = x_values[0] - x0

    r3 = heun(f,x0,y0, h,n,x_values)
    x3,y3 = zip(*r3)

    valores = str(y3)[1:-1] 
    print(valores)

    #ele so vai pedir o valor das coordenadas y.
    

   
