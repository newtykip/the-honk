const isPrime = (number: number) => {
    for (var i = 2; i < number; i++) {
        if (number % i === 0) return false;
    }

    return true;
};

const nthPrime = (n: number) => {
    const primes: number[] = [];
    let number = 2;

    while (n > primes.length) {
        if (isPrime(number)) primes.push(number);
        number++;
    }

    return primes[n - 1];
};

console.log(nthPrime(10001));
