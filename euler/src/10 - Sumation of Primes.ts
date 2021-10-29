export {};

const calcSum = (numbers: number[]) => numbers.reduce((a, b) => a + b);

// Sieve of Eratosthenes time!!!
const sumOfPrimes = (upperBound: number) => {
    let array: boolean[] = [];
    let upperLimit = Math.sqrt(upperBound);
    let output: number[] = [];

    // Make an array from 2 to (n - 1) of truthy values
    for (var i = 0; i < upperBound; i++) {
        array.push(true);
    }

    // Remove multiples of primes starting from 2, 3, 5,...
    for (var i = 2; i <= upperLimit; i++) {
        if (array[i]) {
            for (var j = i * i; j < upperBound; j += i) {
                array[j] = false;
            }
        }
    }

    // All array[i] set to true are primes
    for (var i = 2; i < upperBound; i++) {
        if (array[i]) {
            output.push(i);
        }
    }

    return calcSum(output);
};

console.log(sumOfPrimes(2000000));
