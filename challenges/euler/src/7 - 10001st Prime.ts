// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
// What is the 10 001st prime number?
export {};

/**
 * Is this number prime?
 */
const isPrime = (number: number) => {
    for (var i = 2; i < number; i++) {
        if (number % i === 0) return false;
    }

    return true;
};

/**
 * Calculate the nth prime number.
 */
const nthPrime = (n: number) => {
    const primes: number[] = [];
    let number = 2;

    while (n > primes.length) {
        if (isPrime(number)) primes.push(number);
        number++;
    }

    return primes[n - 1];
};

// Output
console.log(nthPrime(10001));
