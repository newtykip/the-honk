// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
// How many such routes are there through a 20×20 grid?
export {};

/**
 * Calculate n!
 */
const factorial = (n: number) => {
    if (n < 0) return -1;
    else if (n === 0) return 1;
    else return n * factorial(n - 1);
};

/**
 * Count the lattice paths using the formula shown in the thoughts document.
 * @see https://github.com/newtykins/the-honk/tree/main/projects/euler/thoughts/15%20-Lattice%20paths.md
 */
const countLatticePaths = (width: number, height: number) => {
    return factorial(width + height) / (factorial(width) * factorial(height));
};

console.log(countLatticePaths(20, 20));
