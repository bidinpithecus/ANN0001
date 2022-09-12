#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	printMatrix(matrix, *rows, *cols);
	printf("\n");

	swapLine(matrix, *cols, 0, 2);
	multLine(matrix, *cols, 1, 0.22222222222222);

	printMatrix(matrix, *rows, *cols);

	return 0;
}
