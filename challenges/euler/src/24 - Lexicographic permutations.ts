// A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
// 012   021   102   120   201   210
// What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
export = {};

const getPermutations = <T>(array: T[]) => {
    const permutations: T[][] = [];

    if (array.length === 0) return [];
    if (array.length === 1) return [array];

    for (let i = 0; i < array.length; i++) {
        const currentValue = array[i];
        const remainingValues = [...array.slice(0, i), ...array.slice(i + 1)];
        const permutedRemains = getPermutations(remainingValues);

        for (let j = 0; j < permutedRemains.length; j++) {
            const permutedArray = [currentValue, ...permutedRemains[j]];
            permutations.push(permutedArray);
        }
    }

    return permutations;
};

const orderLexicographically = (permutations: number[][]) => {
    return permutations.sort((a, b) => {
        const parsedA = parseInt(a.map(v => v.toString()).join(''));
        const parsedB = parseInt(b.map(v => v.toString()).join(''));

        return parsedA > parsedB ? 1 : -1;
    });
};

const nthLexographicPermutation = (numbers: number[], n: number) => {
    const permutations = orderLexicographically(getPermutations(numbers));
    return parseInt(permutations[n - 1].map(v => v.toString()).join(''));
};

console.log(nthLexographicPermutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000));
