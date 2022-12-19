// A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
//
// 1/2= 0.5
// 1/3= 0.(3)
// 1/4= 0.25
// 1/5= 0.2
// 1/6= 0.1(6)
// 1/7= 0.(142857)
// 1/8= 0.125
// 1/9= 0.(1)
// 1/10= 0.1
//
// Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
// Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
export = {};

const cycleLength = (denominator: number, numerator: number = 1) => {
    let dividend = numerator;
    let position = 1;
    let lastPosition: { [number: number]: number } = {};

    while (true) {
        const remainder = dividend % denominator;

        // If the remainder is zero, there is no recurring cycle
        if (remainder === 0) return 0;

        // If the remainder has been seen before, return.
        if (lastPosition.hasOwnProperty(remainder)) {
            return position - lastPosition[remainder];
        }

        // Move onto the next digit
        lastPosition[remainder] = position;
        position++;
        dividend = remainder * 10;
    }
};

let longestLength = 0;
let correspondingNumber = null;

for (let i = 1; i < 1000; i++) {
    const length = cycleLength(i);

    if (length > longestLength) {
        longestLength = length;
        correspondingNumber = i;
    }
}

console.log(
    `The number with the longest recurring cycle is ${correspondingNumber} with a length of ${longestLength}.`
);
