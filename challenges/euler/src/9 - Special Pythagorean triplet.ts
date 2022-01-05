// See https://github.com/newtykins/the-honk/tree/main/euler/thoughts/9%20-Special%20Pythagorean%29triplet.md
export {};

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

const triplet = pythagoreanTriplet(1000);
console.log(triplet);
console.log(triplet.a * triplet.b * triplet.c);
