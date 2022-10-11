#include "../trabalho1/zeros/methods.h"

#define t 0.98
#define x 4.79

double f(double w) {
	return (-g / (2 * pow(w,2))) * (sinh(w * t) - sin(w * t)) - x;
}

double df(double w) {
	return (g * (t * w * cos(t * w) - t * w * cosh(t * w) - 2 * sin(t * w) + 2 * sinh(t * w)))/(2 * pow(w, 3));
}

int main(void) {
	int iterationsBissection[] = {2, 4, 8, 12};
	int iterationsNewton[] = {1, 3, 5};
	int iterationsSecant[] = {1, 2, 5};
	int iterationsFalsePosition[] = {2, 4, 7, 11};

	// Método da Bisseção
	for(int i = 0; i < sizeof(iterationsBissection) / sizeof(iterationsBissection[0]); i++) {
		bisection(f, -5.86, 0.46, iterationsBissection[i]);
	}
	printf("\n");

	// Método de Newton
	for(int i = 0; i < sizeof(iterationsNewton) / sizeof(iterationsNewton[0]); i++) {
		newton(f, df, -1.48, iterationsNewton[i]);
	}
	printf("\n");

	// Método da Secante
	for(int i = 0; i < sizeof(iterationsSecant) / sizeof(iterationsSecant[0]); i++) {
		secant(f, -4.53, -1.39, iterationsSecant[i]);
	}
	printf("\n");

	// Método da Posição Falsa
	for(int i = 0; i < sizeof(iterationsFalsePosition) / sizeof(iterationsFalsePosition[0]); i++) {
		falsePosition(f, -5.33, 0.78, iterationsFalsePosition[i]);
	}
	printf("\n");

	return 0;
}
