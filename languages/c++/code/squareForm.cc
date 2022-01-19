#include <iostream>

double power(double base, double exponent) {
    double out = base;

    for (int i = 1; i < exponent; i++) {
        out *= base;
    }

    return out;
}

// Euclid algorithm
int greatestCommonDivisor(int a, int b) {
    int currentA = a;
    int currentB = b;
    bool divisorFound = false;

    while (currentA != currentB) {
        if (currentA > currentB) {
            currentA -= currentB;
        }

        if (currentB > currentA) {
            currentB -= currentA;
        }
    }

    return currentA;
}

// Simplify and then format a fraction
std::string formatFraction(int numerator, int denominator) {
    int gcd = greatestCommonDivisor(numerator, denominator);
    int n = numerator / gcd;
    int d = denominator / gcd;

    if (d == 1) {
        return std::to_string(n);
    } else {
        // Fraction unicode
        return std::to_string(n) + "\u2044" + std::to_string(d);
    }
}

// Format a double by cutting off as many trailing zeros as possible
std::string formatDouble(double input) {
    std::string output = std::to_string(input);
    int pointIndex = output.find_last_of('.');
    int firstZeroIndex = output.find_last_not_of('0') + 1;

    if (firstZeroIndex - 1 == pointIndex) {
        output.erase(firstZeroIndex - 1, std::string::npos);
    } else {
        output.erase(firstZeroIndex, std::string::npos);
    }

    return output;
}

// ax² + b^x + c^x -> a(x + p) + q
std::string completeTheSquare(double a, double b, double c) {
    // Calculate relevant values
    double p = b / (2 * a);
    double q = c - (power(b, 2) / 4 * a);
    std::string output = "(x";

    // Add the p value
    if (p != 0) {
        std::string sign = p > 0 ? "+" : "-";
        output += " " + sign + " " + formatFraction(b, 2 * a) + ")²";
    } else {
        output += ")²";
    }

    // Add the q value
    if (q != 0) {
        std::string sign = q > 0 ? "+" : "-";
        output += " " + sign + " " + formatDouble(q);
    }

    // Add the coefficient if relevant
    if (a > 1) {
        output.insert(0, formatDouble(a));
    }

    return output;
}

int main() {
    std::cout << completeTheSquare(1, 2, 5);
}