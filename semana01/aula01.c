#include <math.h>
#include <stdio.h>

#define NUM_ITERATIONS 20
#define PI (3.141592653589793)

void bisection(double(*f)(double), double a, double b, int n, double tol, int iterations[]) {
	double fa = f(a);
	double fb = f(b);
	if (fa * fb >= 0) {
		printf("Intervalo invalido.\n");
		return;
	} else {
		for (int i = 0; i < n; i++) {
			double m = 0.5 * (a + b);
			double fm = f(m);
			if (fm == 0) {
				printf("Raiz encontrada. r = %.7lf\n", m);
				return;
			}

			printf("x_%2d = %.7lf\n", i + 1, m);
			// if (fabs(fm) < tol) {
			if (fabs(b - a) < tol) {
				printf("Atingiu a tolerancia x_%2d = %.7lf\n", i + 1, m);
				return;
			}
			if (fa * fm < 0) {
				b = m;
			} else {
				a = m;
				fa = fm;
			}
		}
	}
}

double f(double x) {
	return pow(x, 3) - 7 * pow(x, 2) + 14 * x - 7;
}

int main(void) {
	int iterations[] = { 2, 4, 5, 6, 11, 12, 13, 16, 21, 22, 23, 24, 28, 29, 31, 33, 35, 36, 37, 38 };
	
	double a = 3.406364;
	double b = 4.34047;
	int n = 100;
	double tol = 2.05959e-08;

	bisection(f, a, b, n, tol, iterations);
}