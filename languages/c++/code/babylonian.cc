#include <iostream>

int sqrt(int number) {
	int initialGuess = 2;

	while (abs(initialGuess - number / initialGuess) > 1) {
		initialGuess = (initialGuess + number / initialGuess) / 2;
	}

	return initialGuess;
}

int main() {
	std::cout << "Type a number to predict the square root of: ";

	int number;
	std::cin >> number;

	std::cout << sqrt(number);
}
