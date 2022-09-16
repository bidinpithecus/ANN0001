#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	double *arr = malloc((*rows) * sizeof(double));
	arr[0] = 0.37;
	arr[1] = -3.45;
	arr[2] = 3.22;
	arr[3] = 3.61;
	int iterations[] = {3, 6, 8, 10, 11, 15, 16, 19, 23, 24, 26, 29};
	int numIterations = sizeof(iterations)/sizeof(int);

	printMatrix(matrix, *rows, *cols);
	jacobi(matrix, *rows, *cols, arr, iterations[numIterations-1] + 1, iterations);

	return 0;
}
