#include <stdio.h>
#include <math.h>

#define ERROR_ORDER 8
// numElemsFirstCol deve ser 'error_order / 2'
#define numElemsFirstCol 4

// Método para trapézios

double trapz(double (*f)(double), double a, double b, int n){
    double soma = 0;
    double h = (double)(b - a) / (double)n;
    for (int i = 0; i < n; i++) {
        double xi = a + i * h;
        soma += f(xi);
    }
    soma *= 2;
    soma += f(a);
    soma += f(b);
    soma *= (0.5 * h);
    return soma;
}

void romberg(double array[]) {
    // i = 0 está calculando a coluna F2
    int numCols = ERROR_ORDER / 2 - 1;
    for (int i = 0; i < numCols; i++) {
        for (int j = 0; j < numCols; j++) {
        double numer = pow(2, (i + 1) * 2) * array[j + 1] - array[j];
        double denom = pow(2, (i + 1) * 2) - 1;
        array[j] = numer / denom;
        }
    }
    printf("Aprox O(h^%d) = %.16f\n", ERROR_ORDER, array[0]);
}

double f(double x) {
    return exp(-x*x);
}

int main() {
    // Exemplo
    // Aproximar int exp(-x*x), de 0 a 1
    if (ERROR_ORDER /2 != numElemsFirstCol) {
        return;
    }

    double a = 0;
    double b = 1;
    double h = 0.5;
    int n =  (int)((b-a) / h);
    printf("%.16f\n", (double)n);

    double coluna_F1[numElemsFirstCol] = {};

    for (int i; i < numElemsFirstCol; i++) {
        coluna_F1[i] = trapz(f, a, b, pow(2, i) * n);
        printf("%.16f\n", (double)n);
    }
    romberg(coluna_F1);
}