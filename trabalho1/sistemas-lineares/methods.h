#include "../../utils.h"
#include "matrixHandler.h"

void gaussJordan(double **matrix, int rows, int cols) {
	for (int j = 0; j < cols-1; j++) {
		for (int i = j; i < rows; i++) {
			if (matrix[i][j] == 0 && i < rows-1) {
				int k = i;
				while (matrix[k][j] == 0 && k < rows-1) {
					swapLine(matrix, cols, i, i+1);
				}
			}
		if (matrix[i][j] != 0) {
			divLine(matrix, cols, i, matrix[i][j]);
			for (int k = 0; k < rows; k++) {
				if (k != i) {
					addLine(matrix, cols, k, i, -matrix[k][j]);
				}
			}
			break;
			}
		}
	}
}

void jacobi(double **matrix, int rows, int cols, double *vetor, int n) {
  for (int k = 0; k < n; k++) {
		double tempVetor[rows];
		for (int i = 0; i < rows; i++) {
			double temp = 0;
			for (int j = 0; j < cols; j++) {
				if (j != i && j != cols - 1) {
					temp += (-matrix[i][j] * vetor[j]) / matrix[i][i];
				}
				else if (j == cols - 1) {
					temp += ((matrix[i][j]) / matrix[i][i]);
				}
			}
			tempVetor[i] = temp;
		}
		for(int i = 0; i < rows; i++) {
			vetor[i] = tempVetor[i];
		}
  }
  printVetor(vetor, rows);
}