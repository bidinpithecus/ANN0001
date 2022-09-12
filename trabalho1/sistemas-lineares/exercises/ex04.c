#include "../methods.h"

int main(void) {
	int *rows = malloc(sizeof(int));
	int *cols = malloc(sizeof(int));
	double **matrix = Matrix(rows, cols);
	double *vetor = malloc((*rows) * sizeof(double));
	vetor[0] = -3.78;
	vetor[1] = 4.94;
	vetor[2] = 2.02;
	int iteracoes[] = {4, 6, 8, 12, 13, 14, 16, 19};

	printMatrix(matrix, *rows, *cols);

	for (int i = 0; i < sizeof(iteracoes)/sizeof(int); i++) {
		jacobi(matrix, *rows, *cols, vetor, iteracoes[i]);
	}

	return 0;
}
