import fs from 'fs';
import path from 'path';
import { resources } from '../constants';

export {};

const maximumPathSum = (triangle: number[][]) => {
    let row = triangle.length - 1;

    while (row--) {
        for (let col = 0; col <= row; col++) {
            triangle[row][col] =
                triangle[row][col] + Math.max(triangle[row + 1][col], triangle[row + 1][col + 1]);
        }
    }

    return triangle[0][0];
};

const data = fs
    .readFileSync(path.join(resources, 'p067_triangle.txt'))
    .toString()
    .split('\n')
    .map(row => {
        const values = row.split(' ');
        return values.map(v => parseInt(v));
    });

console.log(maximumPathSum(data));
