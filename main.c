#include "methods.h"

double f(double x) {
	return x - pow(2, -x);
}

/*
double df(double x) {
	return x;
}
*/

int main(void) {
	double a = 0.3891;
	double b = 1.53;
  int n = 5;
  // bisection(f, a, b, n);
	// newton(f, df, x0, n);
	// secant(f, x0, x1, n);
  falsePosition(f, a, b, n);
  // fixedPoint(f, x0, n);


  return 0;
}