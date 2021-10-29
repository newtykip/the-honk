export {};

const calcSum = (numbers: number[]) => numbers.reduce((a, b) => a + b);

const fibonacciNumbers = (upperBound: number) => {
    const sequence = [1, 2];

    // Keep making new numbers in the sequence until we hit the upper bound
    while (sequence[sequence.length - 1] < upperBound) {
        const newValue = sequence[sequence.length - 1] + sequence[sequence.length - 2];
        sequence.push(newValue);
    }

    return sequence;
};

const evenFibonacciNumbers = (upperBound: number) => {
    const sequence = fibonacciNumbers(upperBound);
    const even = sequence.filter(n => n % 2 === 0);

    return even;
};

console.log(calcSum(evenFibonacciNumbers(4000000)));
