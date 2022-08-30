#include "methods.h"

double f(double x) {
	return ((3 * pow(x, 4) + 2 * pow(x, 2) + 3) / (4 * pow(x, 3) + 4 * x - 1));
}

/*
double df(double x) {
	return x;
}
*/

int main(void) {
	// double a = 0.3891;
	// double b = 1.53;
	// int n = 5;
	double x0 = 1.36485;
	int iterations[] = {1, 2, 3, 4, 5, 6, 7, 8};

	for(int i = 0; i < sizeof(iterations) / sizeof(iterations[0]); i++) {
		// newton(f, df, m, iterations[i]);
		// bisection(f, a, b, iterations[i]);
		// newton(f, df, x0, iterations[i]);
		// secant(f, x0, x1, iterations[i]);
		// falsePosition(f, a, b, iterations[i]);
		fixedPoint(f, x0, iterations[i]);
	}
	printf("\n");

	return 0;
}