#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);

	/*
	k1 = 24
	k2 = 54
	k3 = 61
	k4 = 31
	k5 = 24
	
	k1 = x1 + x2
	x1 + k5 = k4
	k3 = x3 + k5
	x2 + x3 = k2

	1, 1, 0, k1
	1, 0, 0, k4 - k5
	0, 0, 1, k3 - k5
	0, 1, 1, k2

	1, 1, 0, 24, 1, 0, 0, 7, 0, 0, 1, 37, 0, 1, 1, 54
	*/

	printMatrix(matrix, *rows, *cols);
	gaussJordan(matrix, *rows, *cols);
	printMatrix(matrix, *rows, *cols);

	return 0;
}
