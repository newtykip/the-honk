export {};

// a + b + c = 1000
// we need a * b * c
// pythagorean triplet: a < b < c
// a^2 + b^2 = c^2

const pythagoreanTriplet = (sum: number) => {
    let a: number,
        b = 1,
        c: number;

    for (; b < sum; b++) {
        // let x = sum

        // c = x - (a + b)
        // a^2 + b^2 = (x - (a + b))^2
        // a^2 + b^2 = a^2 + 2ab - 2ax + b^2 - 2bx + x^2
        // 0 = 2ab - 2ax - 2bx + x^2

        // 2bx - 2ab = x^2 - 2ax
        // (x^2 / x) - 2a = 2b - (2ab / x)
        // -2a = 2b - (2ab / x) - (x^2 / x)
        // a = - (((x * 2b) - (x * x)) / ((2 * x) - (2 * b)))
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
