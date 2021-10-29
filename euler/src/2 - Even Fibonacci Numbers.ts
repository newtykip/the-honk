import { calcSum } from './utils';

const sequence = [1, 2];
const max = 4000000;

// Keep making new nujm
while (sequence[sequence.length - 1] < max) {
    const newValue = sequence[sequence.length - 1] + sequence[sequence.length - 2];

    sequence.push(newValue);
}

// Filter out the even numbers and find the sum
const even = sequence.filter(n => n % 2 === 0);
console.log(calcSum(even));
