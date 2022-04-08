// Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
// 1634 = 1^4 + 6^4 + 3^4 + 4^4
// 8208 = 8^4 + 2^4 + 0^4 + 8^4
// 9474 = 9^4 + 4^4 + 7^4 + 4^4
// As 1 = 1^4 is not a sum it is not included.
// The sum of these numbers is 1634 + 8208 + 9474 = 19316.
// Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
export = {};

// something times 9^5 = x digit number
// 9^5 = 59049 therefore x >= 5
// 6 * 9^5 = 354294

const powers = [];

for (let i = 0; i < 10; i++) {
    powers.push(i ** 5);
}

const powerSum = (n: number) => {
    let sum = 0;

    while (n > 0) {
        sum += powers[n % 10];
        n = (n / 10) | 0;
    }

    return sum;
};

let sum = 0;

for (let i = 10; i < 6 * powers[9]; i++) {
    if (i === powerSum(i)) sum += i;
}

// Output
console.log(sum);
