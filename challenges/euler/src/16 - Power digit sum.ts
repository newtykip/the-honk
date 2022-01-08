// 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
// What is the sum of the digits of the number 2^1000?
export {};

const powerDigitSum = (base: number, power: number) => {
    const answer = BigInt(base ** power).toString();
    let sum = 0;

    for (let i = 0; i < answer.length; i++) {
        const number = parseInt(answer[i]);
        sum += number;
    }

    return sum;
};

console.log(powerDigitSum(2, 1000));
