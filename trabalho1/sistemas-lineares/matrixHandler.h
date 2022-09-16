void printArr(double *Arr, int rows){
    for(int i = 0; i < rows; i++){ 
        printf("%.7f, ", Arr[i]);
    }
    printf("\n");
}

void printMatrix(double **matrix, int rows, int cols) {
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			printf("%.9f, ", matrix[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}

void multLine(double **matrix, int cols, int resultLine, double mult) {
	for (int i = 0; i < cols; i++) {
		matrix[resultLine][i] = matrix[resultLine][i] * mult;
	} 
}

void divLine(double **matrix, int cols, int resultLine, double divisor) {
	for (int i = 0; i < cols; i++) {
		matrix[resultLine][i] = matrix[resultLine][i] / divisor;
	}
}

void addLine(double **matrix, int cols, int resultLine, int sumLine, double sumLineMul) {
	for (int i = 0; i < cols; i++) {
		matrix[resultLine][i] = matrix[resultLine][i] + sumLineMul * matrix[sumLine][i];
	}
}

void swapLine(double **matrix, int cols, int Line1, int Line2) {
	double temp;
	for (int i = 0; i < cols; i++) {
		temp = matrix[Line1][i];
		matrix[Line1][i] = matrix[Line2][i];
		matrix[Line2][i] = temp;
	}
}

double **Matrix(int *rows, int *cols) {
	FILE *fptr;

	fptr = fopen("trabalho1/sistemas-lineares/input.txt", "r");
	if (!fptr) {
		printf("Unable to open file, exiting\n");
		exit(-1);
	}
	fscanf(fptr, "%dx%d\n", rows, cols);

	double **matrix = malloc((*rows) * sizeof(double*));

	for (int i = 0; i < *rows; i++) {
		matrix[i] = malloc((*cols) * sizeof(double));

		for (int j = 0; j < *cols; j++) {
			fscanf(fptr, "%lf, ", &matrix[i][j]);
		}
	}
	return matrix;
}
