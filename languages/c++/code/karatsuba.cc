#include <iostream>
#include <math.h>
#include <chrono>

typedef std::chrono::high_resolution_clock Clock;
typedef Clock::time_point ClockTime;

double karatsuba(double num1, double num2) {
	int num1Length = std::to_string((int)num1).size();
	int num2Length = std::to_string((int)num2).size();

	// Fallback to traditional multiplication
	if (num1Length == 1 || num2Length == 1) {
		return num1 * num2;
	} else {
		double n = floor(std::max(num1Length, num2Length) / 2);

		double lowNum1 = fmod(num1, pow(10, n));
		double lowNum2 = fmod(num2, pow(10, n));

		double highNum1 = floor(num1 / pow(10, n));
		double highNum2 = floor(num2 / pow(10, n));

		double z0 = karatsuba(lowNum1, lowNum2);
		double z1 = karatsuba(lowNum1 + highNum1, lowNum2 + highNum2);
		double z2 = karatsuba(highNum1, highNum2);

		return (z2 * pow(10, n * 2)) + ((z1 - z2 - z0) * pow(10, n)) + z0;
	}
}

int main() {
	std::cout << "Give me a number! ";

	double num1;
	std::cin >> num1;

	std::cout << "Give me a number to multiply " + std::to_string(num1) + " by! ";

	double num2;
	std::cin >> num2;

	ClockTime karatsubaBegin, karatsubaEnd;
	karatsubaBegin = Clock::now();
	double karatsubaResult = karatsuba(num1, num2);
	karatsubaEnd = Clock::now();
	double karatsubaTime = std::chrono::duration_cast<std::chrono::nanoseconds>(karatsubaEnd - karatsubaBegin).count();

	ClockTime quadraticBegin, quadraticEnd;
	quadraticBegin = Clock::now();
	double quadraticResult = num1 * num2;
	quadraticEnd = Clock::now();
	double quadraticTime = std::chrono::duration_cast<std::chrono::nanoseconds>(quadraticEnd - quadraticBegin).count();

	std::cout << "\nQuadratic Result: " << quadraticResult << " (" << quadraticTime << "ns)\n";
	std::cout << "Karatsuba Result: " << karatsubaResult << " (" << karatsubaTime << "ns)";
}
