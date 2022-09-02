#include "methods.h"

#define r1 1.34
#define r2 5.45
#define H 2.58
#define pt 504.53
#define pw 1000
#define x (H*r1)/(r2-r1)


double f(double h) {
    return pt*H*(pow(r1,2) + pow(r2,2) + (r1*r2)) - pw*(H-h)*(pow(r1,2) + 2*pow(r1,2)*h/x + pow(h,2)*pow(r1,2)/pow(x,2) + pow(r2,2) + (r1*r2) + (h*r1*r2)/x);
}

double df(double h) {
    return -pw*(H-h)*(2*pow(r1,2)/x + 2*h*pow(r1,2)/pow(x,2) + (r1*r2)/x) + pw *(pow(r1,2) + 2*pow(r1,2)*h/x + pow(h,2)*pow(r1,2)/pow(x,2) + pow(r2,2) + (r1*r2) + (h*r1*r2)/x);
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
	// int iterationsNewton[] = {1, 3, 5};
	int iterationsSecant[] = {1, 2, 5};
	int iterationsFalsePosition[] = {2, 4, 7, 11};
	// int iterationsFixedPoint[] = {1, 2, 3, 4, 5, 6, 7, 8};

	// Método da Bisseção
	for(int i = 0; i < sizeof(iterationsBissection) / sizeof(iterationsBissection[0]); i++) {
		bisection(f, 0, 2.58, iterationsBissection[i]);
	}
	printf("\n");
/*
	// Método de Newton
	for(int i = 0; i < sizeof(iterationsNewton) / sizeof(iterationsNewton[0]); i++) {
		newton(f, df, 0.76, iterationsNewton[i]);
	}
	printf("\n");
*/
	// Método da Secante
	for(int i = 0; i < sizeof(iterationsSecant) / sizeof(iterationsSecant[0]); i++) {
		secant(f, 0.25, 2.27, iterationsSecant[i]);
	}
	printf("\n");

	// Método da Posição Falsa
	for(int i = 0; i < sizeof(iterationsFalsePosition) / sizeof(iterationsFalsePosition[0]); i++) {
		falsePosition(f, 0, 2.58, iterationsFalsePosition[i]);
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