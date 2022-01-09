// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2
// For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.
export {};

/**
 * Find a Pythagorean triplet based on its sum
 * @see https://github.com/newtykins/the-honk/tree/main/challenges/euler/thoughts/9%20-%20Special%20Pythagorean%29triplet.md
 */
const pythagoreanTriplet = (sum: number) => {
    let a: number,
        b = 1,
        c: number;

    for (; b < sum; b++) {
        a = -((sum * (2 * b) - sum * sum) / (2 * sum - 2 * b));

        if (Math.floor(a) === a) {
            c = sum - a - b;
            break;
        }
    }

    return { a, b, c };
};

// Output
const triplet = pythagoreanTriplet(1000);
console.log(triplet.a * triplet.b * triplet.c);
