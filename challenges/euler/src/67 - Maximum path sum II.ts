// By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
//    3
//   7 4
//  2 4 6
// 8 5 9 3
// That is, 3 + 7 + 4 + 9 = 23.
// Find the maximum total from top to bottom in p067_triangle.txt, a 15K text file containing a triangle with one-hundred rows.

import fs from 'fs';
import path from 'path';
import { resources } from '../constants';
export {};

// Same method as 18 - Maximum path sum I
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

// Output
const data = fs
    .readFileSync(path.join(resources, 'p067_triangle.txt')) // https://github.com/newtykins/the-honk/tree/main/challenges/euler/resources/p067_triangle.txt
    .toString()
    .split('\n')
    .map(row => {
        const values = row.split(' ');
        return values.map(v => parseInt(v));
    });
const maximumSum = maximumPathSum(data);

console.log(maximumSum);
