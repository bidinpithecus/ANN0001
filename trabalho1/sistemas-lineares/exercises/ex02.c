#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	printMatrix(matrix, *rows, *cols);

	swapLine(matrix, *cols, 0, 1);
	swapLine(matrix, *cols, 0, 2);
	multLine(matrix, *cols, 1, -0.25);
	addLine(matrix, *cols, 0, 2, -0.85714285714286);

	printMatrix(matrix, *rows, *cols);

	return 0;
}
