#include "../trabalho1/sistemas-lineares/methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	double *arr = malloc((*rows) * sizeof(double));
	int iterations[] = {1, 3, 4, 6, 11, 14, 16, 18, 19, 21, 23, 29};
	int numIterations = sizeof(iterations)/sizeof(int);

	printMatrix(matrix, *rows, *cols);
	for (int i = 0; i < numIterations; i++) {
		arr[0] = -0.87;
		arr[1] = -1.96;
		arr[2] = 1.4;
		arr[3] = 4.96;
		seidel(matrix, *rows, *cols, arr, iterations[i]);
		printArr(arr, *rows);
	}

	return 0;
}
