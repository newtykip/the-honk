// The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385
// The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025
// Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
// Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
export {};

/**
 * Calculate the sum of the squares between a lower and upper bound.
 */
const sumOfSquares = (lowerBound: number, upperBound: number) => {
    // Calculate the square number of all the numbers between the bounds
    const squares: number[] = [];

    for (let i = lowerBound; i < upperBound + 1; i++) {
        squares.push(i ** 2);
    }

    // Return the sum
    return squares.reduce((a, b) => a + b);
};

/**
 * Square the sum of the numbers between a lower and upper bound, and return it.
 */
const squareOfSum = (lowerBound: number, upperBound: number) => {
    // Get the sum of all of the numbers between the bounds
    const numbers: number[] = [];

    for (let i = lowerBound; i < upperBound + 1; i++) {
        numbers.push(i);
    }

    // Square the sum
    return numbers.reduce((a, b) => a + b) ** 2;
};

// Output
console.log(squareOfSum(1, 100) - sumOfSquares(1, 100));
