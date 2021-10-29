import { calcSum } from './utils';

const sumOfSquares = (lowerBound: number, upperBound: number) => {
    // Calculate the square number of all the numbers between the bounds
    const squares: number[] = [];

    for (let i = lowerBound; i < upperBound + 1; i++) {
        squares.push(i ** 2);
    }

    // Return the sum
    return calcSum(squares);
};

const squareOfSum = (lowerBound: number, upperBound: number) => {
    // Get the sum of all of the numbers between the bounds
    const numbers: number[] = [];

    for (let i = lowerBound; i < upperBound + 1; i++) {
        numbers.push(i);
    }

    const sum = calcSum(numbers);

    // Square the sum
    return sum ** 2;
};

console.log(squareOfSum(1, 100) - sumOfSquares(1, 100));
