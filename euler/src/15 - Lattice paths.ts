// See https://github.com/newtykins/the-honk/tree/main/euler/thoughts/15%20-Lattice%20Paths.md
export {};

const factorial = (n: number) => {
    if (n < 0) return -1;
    else if (n === 0) return 1;
    else return n * factorial(n - 1);
};

const countLatticePaths = (width: number, height: number) => {
    return factorial(width + height) / (factorial(width) * factorial(height));
};

console.log(countLatticePaths(20, 20));
