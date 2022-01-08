// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143?
export {};

/**
 * Work out the largest prime factor of a number
 */
const largestPrimeFactor = (number: number) => {
    let i = 2;

    while (i * i <= number) {
        if (number % i) i += 1;
        else number = Math.floor(number / i);
    }

    return number;
};

// Output
console.log(largestPrimeFactor(600851475143));
