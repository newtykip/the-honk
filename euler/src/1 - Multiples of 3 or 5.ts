import { calcSum } from './utils';

const below = 1000;
const multiplesOf = [3, 5];
const toAdd: Set<number> = new Set();

// Find all of the multiples of 3 and 5 below 1000
for (let i = 1; i < below; i++) {
    multiplesOf.forEach(num => (i % num == 0 ? toAdd.add(i) : null));
}

console.log(calcSum(Array.from(toAdd)));
