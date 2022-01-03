// n -> n/2 (if n is even)
// n -> 3n + 1 (if n is odd)
// Start at a number, iterate until 1
// Which starting number under one million has the longest chain?

export {};

const isEven = (n: number) => n % 2 === 0;

const collatzSequence = (startNumber: number) => {
    let currentNumber = startNumber;
    let sequence = [startNumber];

    while (currentNumber > 1) {
        if (isEven(currentNumber)) currentNumber = currentNumber / 2;
        else currentNumber = currentNumber * 3 + 1;

        sequence.push(currentNumber);
    }

    return sequence;
};

const longestCollatzUnderLimit = (limit: number) => {
    let longestStartingNumber = -1;
    let longestStartingNumberLength = -1;

    for (let i = 1; i < limit; i++) {
        const sequence = collatzSequence(i);

        if (sequence.length > longestStartingNumberLength) {
            longestStartingNumber = i;
            longestStartingNumberLength = sequence.length;
        }
    }

    return longestStartingNumberLength;
};

console.log(longestCollatzUnderLimit(1000000));
