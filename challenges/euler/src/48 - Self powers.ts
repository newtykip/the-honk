// The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
// Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
export = {};

const calculateSeries = (upperLimit: number): bigint => {
    let sum = BigInt(0);

    for (let i = 1; i <= upperLimit; i++) {
        sum += BigInt(i) ** BigInt(i);
    }

    return sum;
};

const lastNDigits = (number: number | bigint, n: number) => {
    const string = number.toString();
    return parseInt(string.substring(string.length - n));
};

// Output
console.log(lastNDigits(calculateSeries(1000), 10));
