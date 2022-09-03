#include "../../utils.h"

void bisection(double(*f)(double), double a, double b, int n) {
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
				printf("Raiz encontrada. r = %.17lf\n", m);
				return;
			}
			if (i + 1 == n) {
        		printf("%.17lf,", m);
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

void newton(double (*f) (double), double (*df) (double), double x0, int n) {
	for (int i = 0; i < n; i++) {
		double dfx0 = df(x0);

		if (dfx0 == 0) {
			break;
		}
		double xi = x0 - f(x0) / dfx0;
		if (i + 1 == n) {
     		printf("%.17lf,", xi);
    	}
		x0 = xi;
	}
}

void secant(double (*f)(double), double x0, double x1, int n) {
	for (int i = 0; i < n; i++) {
		double fx0 = f(x0);
		double fx1 = f(x1);
		if (fx0 == fx1) {
			break;
		}
		double x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);
		if (i + 1 == n) {
			printf("%.17lf,", x2);
		}
		x0 = x1;
		x1 = x2;
	}
}

void falsePosition(double (*f)(double), double a, double b, int n) {
	for (int i = 0; i < n; i++) {
		double fa = f(a);
		double fb = f(b);
		if (fa * fb >= 0) {
			return;
		}
		double x = (a * fb - b * fa) / (fb - fa);

		if (i + 1 == n) {
		  printf("%.17lf,", x);
		}

		double fx = f(x);

    if (fx == 0) {
      printf("A raiz procurada e: x = %.17lf, e foi encontrada na %d iteracao",x, i+1);
      return;
    } else {
  		if (fa * fx < 0) {
  			b = x;
  			fb = fx;
  		} else {
  			a = x;
  			fa = fx;
  		}
    }
	}
}

void fixedPoint(double (*f)(double), double x0, int n) {
	for (int i = 0; i < n; i++) {
		x0 = f(x0);
		if (i + 1 == n) {
			printf("%.17lf,", x0);
		}
	}
}
