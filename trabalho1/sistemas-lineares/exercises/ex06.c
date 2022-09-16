#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	double *arr = malloc((*rows) * sizeof(double));
	arr[0] = -4.84;
	arr[1] = -3.66;
	arr[2] = 2.34;
	int iterations[] = {7, 8, 11, 12, 15, 17, 18, 19};
	int numIterations = sizeof(iterations)/sizeof(int);

	printMatrix(matrix, *rows, *cols);
	for (int i = 0; i < numIterations; i++) {
		arr[0] = -4.84;
		arr[1] = -3.66;
		arr[2] = 2.34;
		seidel(matrix, *rows, *cols, arr, iterations[i]);
		printArr(arr, *rows);
	}

	return 0;
}
