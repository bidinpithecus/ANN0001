#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	int L1 = 0;
	int L2 = 1;
	int L3 = 2;
	int L4 = 3;
	printMatrix(matrix, *rows, *cols);

	/*
	4/5⋅L1+L2→L2
	6/5⋅L1+L3→L3
	−8/5⋅L1+L4→L4
	11/6⋅L2+L3→L3
	−2/9⋅L2+L4→L4
	170/183⋅L3+L4→L4
	*/
	addLine(matrix, *cols, L2, L1, 0.8);
	addLine(matrix, *cols, L3, L1, 1.2);
	addLine(matrix, *cols, L4, L1, -1.6);
	addLine(matrix, *cols, L3, L2, 1.8333333333333333);
	addLine(matrix, *cols, L4, L2, -0.2222222222222222);
	addLine(matrix, *cols, L4, L3, 0.9289617486338798);

	printMatrix(matrix, *rows, *cols);

	return 0;
}
