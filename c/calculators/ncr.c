#include <stdio.h>

int factorial(int n) {
	int ans = 1;

	for (int i = 2; i <= n; i++) {
		ans *= i;
	}

	return ans;
}

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
