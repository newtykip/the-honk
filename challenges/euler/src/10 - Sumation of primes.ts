// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
// Find the sum of all the primes below two million.
export {};

/**
 * Use the Sieve of Eratosthenes to find the sum of primes up until a limit.
 * @see https://github.com/newtykins/the-honk/tree/main/projects/euler/thoughts/10%20-Summation%20of%29primes.md
 */
const sumOfPrimes = (limit: number) => {
    let array: boolean[] = [];
    let upperLimit = Math.sqrt(limit);
    let output: number[] = [];

    // Make an array from 2 to (n - 1) of truthy values
    for (var i = 0; i < limit; i++) {
        array.push(true);
    }

    // Remove multiples of primes starting from 2, 3, 5,...
    for (var i = 2; i <= upperLimit; i++) {
        if (array[i]) {
            for (var j = i * i; j < limit; j += i) {
                array[j] = false;
            }
        }
    }

    // All array[i] set to true are primes
    for (var i = 2; i < limit; i++) {
        if (array[i]) {
            output.push(i);
        }
    }

    return output.reduce((a, b) => a + b);
};

// Output
console.log(sumOfPrimes(2000000));
