// A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
// A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
//
// As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
// Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
export = {};

const findProperDivisors = (number: number) => {
    const divisors: number[] = [1];

    for (let i = 2; i < number; i++) {
        if (number % i === 0) {
            divisors.push(i);
        }
    }

    return divisors;
};

const isNumberAbundant = (number: number) => {
    const divisors = findProperDivisors(number);
    return divisors.reduce((a, b) => a + b) > number;
};

const abundantNumbers = (lowerBound: number, upperBound: number) => {
    const numbers: number[] = [];

    for (let i = lowerBound; i < upperBound; i++) {
        if (isNumberAbundant(i)) numbers.push(i);
    }

    return numbers;
};

const upperLimit = 28123;
const numbers = abundantNumbers(1, upperLimit);
const sums = Array(upperLimit + 1).fill(0);

for (let i = 0; i < numbers.length; i++) {
    for (let j = i; j < numbers.length; j++) {
        const sum = numbers[i] + numbers[j];

        if (sum <= upperLimit) {
            if (sums[sum] == 0) sums[sum] = sum;
        }
    }
}

let answer = 0;

for (let i = 1; i < sums.length; i++) {
    if (sums[i] === 0) answer += i;
}

// Output
console.log(answer);
