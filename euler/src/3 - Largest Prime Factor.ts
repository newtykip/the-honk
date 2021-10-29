const largestPrimeFactor = (number: number) => {
    let i = 2;

    while (i * i <= number) {
        if (number % i) i += 1;
        else number = Math.floor(number / i);
    }

    return number;
};

console.log(largestPrimeFactor(600851475143));
