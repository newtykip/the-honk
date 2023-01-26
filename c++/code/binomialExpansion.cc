#include <iostream>

std::string superscript[10] = {"⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"};

int factorial(int number) {
	int out = 1;

	for (int i = 2; i <= number; i++) {
		out *= i;
	}

	return out;
}

int nCr(int n, int r) {
	return factorial(n) / (factorial(r) * factorial(n - r));
}

std::string formatNomial(int value, std::string nomial) {
	std::string term = nomial;

	if (value != 1) {
		std::string power = "";

		for (char & digit : std::to_string(value)) {
			power += superscript[digit - '0'];
		}

		term += power;
	}

	return term;
}

std::string binomialExpansion(int power) {
	std::string output = "";

	for (int r = 0; r <= power; r++) {
		int a = power - r;
		int c = nCr(power, r);
		std::string term = "";

		if (c != 1) {
			term += std::to_string(c);
		}

		if (a != 0) {
			term += formatNomial(a, "a");
		}

		if (r != 0) {
			term += formatNomial(r, "b");
		}

		if (r != 0) {
			output += " + " + term;
		} else {
			output += term;
		}
	}

	return output;
}

int main() {
	std::cout << "(a + b)ⁿ\nPlease input a value for n! ";

	int n;
	std::cin >> n;

	std::cout << binomialExpansion(n);
}
