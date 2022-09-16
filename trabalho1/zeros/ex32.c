#include "methods.h"

#define V 125.62
#define R 4.69

double f(double h) {
	return pow(h,2) * ((-(h * PI))/3 + PI * R) - V;
}

double df(double h) {
	return PI * (-h) * (h - 2 * R);
}

int main(void) {
	int iterationsBissection[] = {2, 4, 8, 12};
	int iterationsNewton[] = {1, 3, 5};
	int iterationsSecant[] = {1, 2, 5};
	int iterationsFalsePosition[] = {2, 5, 7, 11};

	// Método da Bisseção
	for(int i = 0; i < sizeof(iterationsBissection) / sizeof(iterationsBissection[0]); i++) {
		bisection(f, 0, 9.38, iterationsBissection[i]);
	}
	printf("\n");

	// Método de Newton
	for(int i = 0; i < sizeof(iterationsNewton) / sizeof(iterationsNewton[0]); i++) {
		newton(f, df, 5.02, iterationsNewton[i]);
	}
	printf("\n");

	// Método da Secante
	for(int i = 0; i < sizeof(iterationsSecant) / sizeof(iterationsSecant[0]); i++) {
		secant(f, 0.93, 8.98, iterationsSecant[i]);
	}
	printf("\n");

	// Método da Posição Falsa
	for(int i = 0; i < sizeof(iterationsFalsePosition) / sizeof(iterationsFalsePosition[0]); i++) {
		falsePosition(f, 0, 9.38, iterationsFalsePosition[i]);
	}
	printf("\n");

	return 0;
}
