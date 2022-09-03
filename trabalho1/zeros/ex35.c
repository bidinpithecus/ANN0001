#include "methods.h"

#define V 171.78
#define L 8.42
#define r 3.77

double f(double h) {
	return L*((0.5*PI*pow(r,2)) - pow(r,2)*asin(h/r)- h*(sqrt(pow(r,2)-pow(h,2))))-V;
}

int main(void) {
	int iterationsBisection[] = {2, 4, 8, 12};
	int iterationsSecant[] = {1, 2, 5};
	int iterationsFalsePosition[] = {2, 4, 7, 11};

	// Método da Bisseção
	for(int i = 0; i < sizeof(iterationsBisection) / sizeof(iterationsBisection[0]); i++) {
		bisection(f, 0, 3.77, iterationsBisection[i]);
	}
	printf("\n");

	// Método da Secante
	for(int i = 0; i < sizeof(iterationsSecant) / sizeof(iterationsSecant[0]); i++) {
		secant(f, 0.03, 3.39, iterationsSecant[i]);
	}
	printf("\n");

	// Método da Posição Falsa
	for(int i = 0; i < sizeof(iterationsFalsePosition) / sizeof(iterationsFalsePosition[0]); i++) {
		falsePosition(f, 0, 3.77, iterationsFalsePosition[i]);
	}
	printf("\n");

	return 0;
}
