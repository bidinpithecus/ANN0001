#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	double *arr = malloc((*rows) * sizeof(double));
	int iterations[] = {1, 3, 4, 5, 6, 7, 11, 12, 16, 17, 23, 25};
	int numIterations = sizeof(iterations)/sizeof(int);

	printMatrix(matrix, *rows, *cols);
	for (int i = 0; i < numIterations; i++) {
		arr[0] = -1.11;
		arr[1] = 4.9;
		arr[2] = -2.93;
		arr[3] = -4.23;
		seidel(matrix, *rows, *cols, arr, iterations[i]);
		printArr(arr, *rows);
	}

	return 0;
}
