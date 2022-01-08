// n! means n × (n − 1) × ... × 3 × 2 × 1
// For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
// Find the sum of the digits in the number 100!
export = {};

/**
 * Calculate n! as a BigInt
 */
const factorial = (n: number) => {
    if (n < 0) return BigInt(-1);
    else if (n === 0) return BigInt(1);
    else return BigInt(BigInt(n) * factorial(n - 1));
};

/**
 * Find the sum of the digits in a number
 */
const sumOfDigits = (n: number) => {
    let sum = 0;

    n.toString()
        .split('')
        .map(d => parseInt(d))
        .forEach(digit => (sum += digit));

    return sum;
};

// Output
const digitSum = sumOfDigits(factorial(100));
console.log(digitSum);
