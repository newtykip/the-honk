// Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
// 21 22 23 24 25
// 20  7  8  9 10
// 19  6  1  2 11
// 18  5  4  3 12
// 17 16 15 14 13
// It can be verified that the sum of the numbers on the diagonals is 101.
// What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
export = {};

const sumOfSpiralDiagonals = (size: number) => {
    let sum = 1;

    // Matrix is size n
    // Lowest number is n(n - 3) + 4
    // Numbers increase by n - 1

    for (let n = 3; n <= size; n += 2) {
        const corners = [];

        for (let i = n * (n - 3) + 3; corners.length < 4; i += n - 1) {
            corners.push(i);
        }

        sum += corners.reduce((a, b) => a + b);
    }

    return sum;
};

// Output
console.log(sumOfSpiralDiagonals(1001));
