#include "methods.h"

double f(double x) {
	return (sqrt(2 * 9.81 * x) * tanh(5.4 * sqrt(2 * 9.81 * x)/(2 * 7.1)) - 10.1);
}

double df(double x) {
	// not correct i presume
	return ((3*sqrt(109)*tanh((81*sqrt(109)*sqrt(x))/(355*sqrt(2))))/(sqrt(2)*sqrt(x))+(26487*sech((81*sqrt(109)*sqrt(x))/(355*sqrt(2)))^2)/710)/10;
}

int main(void) {
	/* 
	Variáveis não utilizadas
	
	double a = 0.3891;
	double b = 1.53;
	double x0 = 1.36485;
	int n = 5;
	*/
	int iterationsBissection[] = {2, 4, 8, 12};
	int iterationsNewton[] = {1, 3, 5};
	// int iterationsSecant[] = {1, 2, 5};
	int iterationsFalsePosition[] = {2, 4, 7, 11};
	// int iterationsFixedPoint[] = {1, 2, 3, 4, 5, 6, 7, 8};

	// Método da Bisseção
	for(int i = 0; i < sizeof(iterationsBissection) / sizeof(iterationsBissection[0]); i++) {
		bisection(f, 0.15, 16.38, iterationsBissection[i]);
	}
	printf("\n");

	// Método de Newton
	for(int i = 0; i < sizeof(iterationsNewton) / sizeof(iterationsNewton[0]); i++) {
		newton(f, df, 0.99, iterationsNewton[i]);
	}
	printf("\n");
/*
	// Método da Secante
	for(int i = 0; i < sizeof(iterationsSecant) / sizeof(iterationsSecant[0]); i++) {
		secant(f, 1.84, 14.49, iterationsSecant[i]);
	}
	printf("\n");
*/
	// Método da Posição Falsa
	for(int i = 0; i < sizeof(iterationsFalsePosition) / sizeof(iterationsFalsePosition[0]); i++) {
		falsePosition(f, 0.47, 19.72, iterationsFalsePosition[i]);
	}
	printf("\n");
/*
	// Método do Ponto Fixo
	for(int i = 0; i < sizeof(iterationsFixedPoint) / sizeof(iterationsFixedPoint[0]); i++) {
		fixedPoint(f, x0, iterationsFixedPoint[i]);
	}
*/
	printf("\n");
	return 0;
}