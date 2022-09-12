#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	printMatrix(matrix, *rows, *cols);

	addLine(matrix, *cols, 2, 0, 0.42857142857143);
	multLine(matrix, *cols, 2, 5);
	swapLine(matrix, *cols, 2, 3);
	multLine(matrix, *cols, 0, -1.8);
	addLine(matrix, *cols, 1, 2, -4.5);
	swapLine(matrix, *cols, 0, 2);

	printMatrix(matrix, *rows, *cols);

	return 0;
}
