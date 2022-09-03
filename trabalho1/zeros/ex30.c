#include "methods.h"

#define L 4.17
#define v 9.17
#define t 7.96

double f(double H) {
	return (sqrt(2 * g * H) * tanh(sqrt(2 * g * H) * t / (2 * L))) - v;
}

double sech(double x) {
    return 1 / cosh(x);
}

double df(double H) {
	return (sqrt(2*g/H)/2) * tanh(sqrt(2*g*H)*t/(2*L)) + sqrt(2*g*H)*pow(sech(sqrt(2*g*H)*t/(2*L)),2)*(t*sqrt(2*g)/(4*L*sqrt(H)));
}

int main(void) {
	int iterationsBissection[] = {2, 4, 8, 12};
	int iterationsNewton[] = {1, 3, 5};
	int iterationsFalsePosition[] = {2, 4, 7, 11};

	// Método da Bisseção
	for(int i = 0; i < sizeof(iterationsBissection) / sizeof(iterationsBissection[0]); i++) {
		bisection(f, 0.28, 15.3, iterationsBissection[i]);
	}
	printf("\n");

	// Método de Newton
	for(int i = 0; i < sizeof(iterationsNewton) / sizeof(iterationsNewton[0]); i++) {
		newton(f, df, 0.42, iterationsNewton[i]);
	}
	printf("\n");

	// Método da Posição Falsa
	for(int i = 0; i < sizeof(iterationsFalsePosition) / sizeof(iterationsFalsePosition[0]); i++) {
		falsePosition(f, 0.38, 15.76, iterationsFalsePosition[i]);
	}
	printf("\n");

	return 0;
}
