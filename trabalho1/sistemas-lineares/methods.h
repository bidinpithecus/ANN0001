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

void jacobi(double **matrix, int rows, int cols, double *arr, int n, int *iterations) {
	int index = 0;
	for (int k = 0; k < n; k++) {
		double tempArr[rows];
		for (int i = 0; i < rows; i++) {
			double temp = 0;
			double bi = matrix[i][cols - 1];
			for (int j = 0; j < cols; j++) {
				if (j != i) {
					temp -= matrix[i][j] * arr[j];
				}
			}
			double xi = (bi + temp) / matrix[i][i];
			tempArr[i] = xi;
			if (k == iterations[index]) {
				printArr(arr, rows);
				index++;
			}
		}
		for(int i = 0; i < rows; i++) {
			arr[i] = tempArr[i];
		}
	}
}

void seidel(double **matrix, int rows, int cols, double *arr, int n) {
	for (int k = 0; k < n; k++) {
		for (int i = 0; i < rows; i++) {
			double temp = 0;
			for (int j = 0; j < cols; j++) {
				if (j != i && j != cols-1) {
					temp += (-matrix[i][j] * arr[j]) / matrix[i][i];
				} else if (j == cols-1) {
					temp += ((matrix[i][j]) / matrix[i][i]);
				}
			}
			arr[i] = temp;
		}
	}
}