#include <stdio.h>

int main(void) {
	int A;
	int B;
	scanf_s("%d", &A);
	scanf_s("%d", &B);

	if (A > B) {
		printf(">");
	}
	else if (A < B) {
		printf("<");
	}
	else if (A == B) {
		printf("==");
	}

	return 0;
}