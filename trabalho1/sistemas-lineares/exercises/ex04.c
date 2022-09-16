#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	double *arr = malloc((*rows) * sizeof(double));
	arr[0] = -3.78;
	arr[1] = 4.94;
	arr[2] = 2.02;
	int iterations[] = {4, 6, 8, 12, 13, 14, 16, 19};

	printMatrix(matrix, *rows, *cols);
	jacobi(matrix, *rows, *cols, arr, 20);

	return 0;
}
