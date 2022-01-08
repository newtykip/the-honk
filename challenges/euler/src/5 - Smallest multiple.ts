// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
export {};

const canBeDivided = (x: number, n: number) => {
    for (; n > 0; n -= 1) {
        if (x % n !== 0) return false;
    }

    return true;
};

const divisibleTo = (n: number) => {
    if (n === 1) return 1;

    for (var step = divisibleTo(n - 1), i = step; !canBeDivided(i, n); i += step);
    return i;
};

// Output
console.log(divisibleTo(20));
