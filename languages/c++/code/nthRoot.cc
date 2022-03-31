#include <iostream>
#include <cmath>
#include <limits>

std::string superscript[10] = { "⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹" };

struct Result {
	double result;
	int maxIterations;
	int iterationsUsed;
};

// See https://github.com/newtykins/the-honk/tree/main/maths/nth%20root.png
Result nthRoot(double n, double x, int maxIterations = 200) {
	Result output;
	output.result = 1;
	output.maxIterations = maxIterations;
	output.iterationsUsed = 0;

	double lastIteration = 0;

	for (int i = 0; i < maxIterations; i++) {
		if (lastIteration == output.result) {
			break;
		}
		
		output.iterationsUsed += 1;
		lastIteration = output.result;
		output.result = ((lastIteration * (n - 1)) + (x * std::pow(lastIteration, 1 - n))) / n;
	}

	return output;
}

int fetchInput(std::string letter) {
    std::cout << "Please input a value for " + letter + ": ";
    
    double input;
    std::cin >> input;

    return input;
}

bool isInt(double n) {
	return (int) n == n;
}

std::string formatDouble(double input) {
    std::string str = std::to_string(input);
	str.erase(str.find_last_not_of('0') + 1, std::string::npos);
	return str;
}

std::string formatRadical(double n, double x) {
	std::string formattedN = "";
	std::string formattedX = "";

	if (isInt(n)) {
		std::string nString = std::to_string((int) n);

		for (int i = 0; i < nString.length(); i++) {
			int digit = (int) nString[i] - 48;
			formattedN += superscript[digit];
		}
	} else {
		std::string nString = formatDouble(n);

		for (int i = 0; i < nString.length(); i++) {
			try {
				int digit = (int) nString[i] - 48;
				formattedN += superscript[digit];
			} catch (const std::exception) {
				formattedN += "˙";
			}
		}
	}

	if (isInt(x)) {
		formattedX = std::to_string((int) x);
	} else {
		formattedX = formatDouble(x);
	}

	return formattedN + "√" + formattedX;
}

int main() {
	std::cout << "ⁿ√x\n";

	double n = fetchInput("n");
	double x = fetchInput("x");

	std::cout << "Please enter an amount of iterations to perform: ";

	int iterations;
	std::cin >> iterations;

	// Make sure that cout prints to the highest precision possible
	std::cout.precision(std::numeric_limits<double>::max_digits10);

	Result root = nthRoot(n, x, iterations);

	std::cout << "\n" << formatRadical(n, x) << " = " << root.result << "\n";
	std::cout << "Used " << root.iterationsUsed << " out of " << root.maxIterations << " iterations (:";
}
