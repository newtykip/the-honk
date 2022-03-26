// Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
// For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
// What is the total of all the name scores in the file?
export = {};

import fs from 'fs';
import path, { parse } from 'path';
import { resources } from '../constants';

const parseNames = () =>
    fs
        .readFileSync(path.join(resources, 'p022_names.txt'))
        .toString()
        .split(',')
        .map(name => name.replace(/"/g, '').toLowerCase())
        .sort((a, b) => a.localeCompare(b));

const nameScore = (name: string, position: number) => {
    let letterSum = 0;

    for (let i = 0; i < name.length; i++) {
        letterSum += name.charCodeAt(i) - 96; // use char codes to easily find the alphabetical location
    }

    return letterSum * position;
};

const nameScoreTotal = (names: string[]) => {
    let total = 0;

    names.forEach((name, i) => {
        total += nameScore(name, i + 1);
    });

    return total;
};

// Output
const names = parseNames();
console.log(nameScoreTotal(names));
