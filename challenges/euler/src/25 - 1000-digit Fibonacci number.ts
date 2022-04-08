// The Fibonacci sequence is defined by the recurrence relation:
// Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
// The 12th term, F12, is the first term to contain three digits.
// What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
export = {};

function* fibonacciSequence(): Generator<bigint, bigint, bigint> {
    let current = BigInt(1);
    let a = BigInt(1);
    let b = BigInt(1);

    yield BigInt(1);

    while (true) {
        current = b;
        yield current;

        b = a + b;
        a = current;
    }
}

const firstTermWithXDigits = (sequence: Generator<bigint, bigint, bigint>, digitCount: number) => {
    let { value: term } = sequence.next();
    let index = 1;

    while (term.toString().length !== digitCount) {
        term = sequence.next().value;
        index += 1;
    }

    return {
        value: term,
        index
    };
};

// Output

const fibonacci = fibonacciSequence();
const firstTerm = firstTermWithXDigits(fibonacci, 1000);

console.log(firstTerm);
