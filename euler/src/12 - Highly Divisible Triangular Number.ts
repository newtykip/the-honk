export {};

const factorsOf = (num: number) => {
    const isEven = num % 2 === 0;
    const max = Math.sqrt(num);
    const inc = isEven ? 1 : 2;
    const factors = [1, num];

    for (let curFactor = isEven ? 2 : 3; curFactor <= max; curFactor += inc) {
        if (num % curFactor !== 0) continue;
        factors.push(curFactor);

        let compliment = num / curFactor;
        if (compliment !== curFactor) factors.push(compliment);
    }

    return factors;
};

// https://www.mathsisfun.com/algebra/triangular-numbers.html
const nthTriangleNumber = (n: number) => (n * (n + 1)) / 2;

const firstTriangleWithOverNDivisors = (n: number) => {
    let divisorCountFound = false;
    let i = 1;

    while (!divisorCountFound) {
        const triangle = nthTriangleNumber(i);
        const factors = [...factorsOf(triangle)];
        i++;

        if (factors.length > n) {
            divisorCountFound = true;
            return triangle;
        }
    }
};

console.log(firstTriangleWithOverNDivisors(500));
