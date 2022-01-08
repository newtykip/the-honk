// The following iterative sequence is defined for the set of positive integers:
// n → n/2 (n is even)
// n → 3n + 1 (n is odd)

// Using the rule above and starting with 13, we generate the following sequence:
// 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

// It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

// Which starting number, under one million, produces the longest chain?
// NOTE: Once the chain starts the terms are allowed to go above one million.
export {};

const calculateSequence = (startNumber: number) => {
    let currentNumber = startNumber;
    let sequence = [startNumber];

    while (currentNumber > 1) {
        if (currentNumber % 2 === 0) currentNumber = currentNumber / 2;
        else currentNumber = currentNumber * 3 + 1;

        sequence.push(currentNumber);
    }

    return sequence;
};

const longestSequenceUnderLimit = (limit: number) => {
    let longestStartingNumber = -1;
    let longestStartingNumberLength = -1;

    for (let i = 1; i < limit; i++) {
        const sequence = calculateSequence(i);

        if (sequence.length > longestStartingNumberLength) {
            longestStartingNumber = i;
            longestStartingNumberLength = sequence.length;
        }
    }

    return longestStartingNumberLength;
};

// Output
console.log(longestSequenceUnderLimit(1000000));
