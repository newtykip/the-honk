#include <iostream>
#include <cmath>
#include <limits>

double nthRoot(double n, double x) {
	double lastX;
	double y = 1; // initial guess

	while (y != lastX) {
		// f(y) = yⁿ - x
		// f'(y) = nyⁿ⁻¹
		double f = std::pow(y, n) - x;
		double fprime = n * std::pow(y, n - 1);

		lastX = y;
		y -= f / fprime;
	}

	return y;
}

int promptForInteger(std::string letter) {
    std::cout << "Please input a value for " + letter + ": ";
    
    int input;
    std::cin >> input;

    return input;
}


int main() {
	std::cout << "ⁿ√x\n";
	int n = promptForInteger("n");
	int x = promptForInteger("x");

	// Make sure that cout prints to the highest precision possible
	std::cout.precision(std::numeric_limits<double>::max_digits10);
	std::cout << nthRoot(n, x);
}
