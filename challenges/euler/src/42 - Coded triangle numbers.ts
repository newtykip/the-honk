// The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
// 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
// By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
// Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import fs from 'fs';
import path from 'path';
import { resources, alphabet } from '../constants.js';
export = {};

const words = fs
    .readFileSync(path.join(resources, 'p042_words.txt'))
    .toString()
    .split(',')
    .map(word => word.replace(/"/g, '').toLowerCase());

const isTriangleNumber = (t: number) => {
    // One solution of the inverse triangle number formula
    const solution = (Math.sqrt(8 * t + 1) - 1) / 2;

    // This number must be an integer and greater than zero for it to be a triangle number
    return Number.isInteger(solution) && solution > 0;
};

let triangleWordCount = 0;

for (const word of words) {
    const letters = word.split('');
    let sum = 0;

    for (const letter of letters) {
        const value = alphabet.indexOf(letter) + 1;
        sum += value;
    }

    if (isTriangleNumber(sum)) triangleWordCount++;
}

// Output
console.log(`Out of nearly 2000 common English words, ${triangleWordCount} are triangle words!`);
