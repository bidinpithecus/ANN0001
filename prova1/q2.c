#include "../trabalho1/zeros/methods.h"

#define k1 50700
#define k2 60
#define m 94
#define h 0.64


double f(double d) {
	return ((2 * k2 * pow(d, 2.5)) / 5) + (0.5 * k1 * pow(d, 2)) - (m * g * d) - (m * g * h);
}

double df(double d) {
	return (k2 * pow(d, 1.5)) + (k1 * d) - (g * m);
}

int main(void) {
	int iterationsBissection[] = {1, 4, 7, 10};
	int iterationsNewton[] = {1, 3, 6};
	int iterationsSecant[] = {1, 2, 5, 8};
	int iterationsFalsePosition[] = {2, 5, 7, 11};

	// Método da Bisseção
	for(int i = 0; i < sizeof(iterationsBissection) / sizeof(iterationsBissection[0]); i++) {
		bisection(f, 0.0,1.53, iterationsBissection[i]);
	}
	printf("\n");

	// Método de Newton
	for(int i = 0; i < sizeof(iterationsNewton) / sizeof(iterationsNewton[0]); i++) {
		newton(f, df, 1.09, iterationsNewton[i]);
	}
	printf("\n");

	// Método da Secante
	for(int i = 0; i < sizeof(iterationsSecant) / sizeof(iterationsSecant[0]); i++) {
		secant(f, 0.9, 1.88, iterationsSecant[i]);
	}
	printf("\n");

	// Método da Posição Falsa
	for(int i = 0; i < sizeof(iterationsFalsePosition) / sizeof(iterationsFalsePosition[0]); i++) {
		falsePosition(f, 0.0,1.89, iterationsFalsePosition[i]);
	}
	printf("\n");

	return 0;
}
