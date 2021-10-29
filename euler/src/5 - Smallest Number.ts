export {};

/**
 * Is x disible to n?
 */
const isDivisibleTo = (x: number, n: number) => {
    for (; n > 0; n -= 1) {
        if (x % n !== 0) return false;
    }

    return true;
};

const divisibleTo = (n: number) => {
    if (n === 1) return 1;

    for (var step = divisibleTo(n - 1), i = step; !isDivisibleTo(i, n); i += step);
    return i;
};

console.log(divisibleTo(20));
