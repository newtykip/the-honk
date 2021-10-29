import { calcSum } from './utils';

const multiplesOf = (numbers: number[], upperBound: number) => {
    const results: Set<number> = new Set();

    for (let i = 1; i < upperBound; i++) {
        numbers.forEach(num => (i % num == 0 ? results.add(i) : null));
    }

    return Array.from(results);
};

console.log(calcSum(multiplesOf([3, 5], 1000)));
