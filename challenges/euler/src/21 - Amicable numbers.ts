// Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
// Evaluate the sum of all the amicable numbers under 10000.
export = {};

const findProperDivisors = (number: number) => {
    const divisors: number[] = [1];

    for (let i = 2; i < number; i++) {
        if (number % i === 0) {
            divisors.push(i);
        }
    }

    return divisors;
};

const d = (n: number) => findProperDivisors(n).reduce((a, b) => a + b);

const findAmicableNumbers = (upperBound: number) => {
    const amicableNumbers: number[] = [];

    for (let a = 0; a < upperBound; a++) {
        const b = d(a);

        if (d(b) === a && a !== b) {
            amicableNumbers.push(a);
        }
    }

    return amicableNumbers;
};

// Output
console.log(findAmicableNumbers(10000).reduce((a, b) => a + b));
