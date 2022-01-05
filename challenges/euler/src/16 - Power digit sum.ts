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
