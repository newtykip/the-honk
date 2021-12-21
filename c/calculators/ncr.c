#include <stdio.h>
#include "helpers/factorial.c"

int nCr(int n, int r) {
	return factorial(n) / factorial(r) * factorial(n - r);
}

void main() {
	int n;
	int r;

	printf("Please enter n: ");
	scanf("%i", &n);

	printf("Please enter r: ");
	scanf("%i", &r);
	
	int ans = nCr(n, r);
	printf("The answer is: %i", ans);
}
