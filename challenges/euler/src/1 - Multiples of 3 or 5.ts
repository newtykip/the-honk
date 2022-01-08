// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.
export {};

/**
 * Figure out the multiples of two numbers below a bound
 */
const multiplesOf = (numbers: number[], upperBound: number) => {
    const results: Set<number> = new Set();

    for (let i = 1; i < upperBound; i++) {
        numbers.forEach(num => (i % num == 0 ? results.add(i) : null));
    }

    return Array.from(results);
};

// Output
const multiples = multiplesOf([3, 5], 1000);
const sum = multiples.reduce((a, b) => a + b);

console.log(sum);
