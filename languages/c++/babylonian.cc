#include <iostream>
using namespace std;

int sqrt(int number) {
	int initialGuess = 2;

	while (abs(initialGuess - number / initialGuess) > 1) {
		initialGuess = (initialGuess + number / initialGuess) / 2;
	}

	return initialGuess;
}

int main() {
	cout << "Type a number to predict the square root of:";

	int number;
	cin >> number;

	cout << sqrt(number);
}
