#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	printMatrix(matrix, *rows, *cols);

	addLine(matrix, *cols, 1, 0, -0.333333333);
	addLine(matrix, *cols, 2, 0, 0.666666666);
	addLine(matrix, *cols, 2, 1, 0.5);

	printMatrix(matrix, *rows, *cols);

	return 0;
}
