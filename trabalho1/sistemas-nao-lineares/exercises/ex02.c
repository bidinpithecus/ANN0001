#include <math.h>
#include <stdio.h>

double f1(double x, double y) {
	return 4*pow(x,2) + pow(y,2) - 5;
}

double f1x(double x, double y) {
	return 8*x;
}

double f1y(double x, double y) {
	return 2*y;
}

double f2(double x, double y) {
	return pow(x,2) + pow(y,3) - 4;
}

double f2x(double x, double y) {
	return 2*x;
}

double f2y(double x, double y) {
	return 3*pow(y,2);
}

double newton(double x0, double y0, int n){
	for(int i = 0; i < n; i++){
		double F[] = {f1(x0, y0), f2(x0, y0)};
		double det = f1x(x0, y0) * f2y(x0, y0) - f1y(x0, y0) * f2x(x0, y0);
		double dF_inv[2][2] = {{f2y(x0, y0) / det, -f1y(x0, y0) / det}, {-f2x(x0, y0) / det, f1x(x0, y0) / det}};
		x0 = x0 - (F[0] * dF_inv[0][0] + F[1] * dF_inv[0][1]);
		y0 = y0 - (F[0] * dF_inv[1][0] + F[1] * dF_inv[1][1]);
	}
	printf("%.16f,%.16f,", x0, y0);
}

int main(){
	int arr[] = {1, 2, 3, 4, 5};
	double x0 = -0.6436;
	double y0 = 1.3754;
	for(int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++){
		newton(x0, y0, arr[i]);
	}
	printf("\n");
}
