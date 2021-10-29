const biggest = 999;
const smallest = 100;

// Work out all of the products of 3 digit numbers
const products: number[] = [];

for (let i = smallest; i < biggest + 1; i++) {
    for (let j = smallest; j < biggest + 1; j++) {
        products.push(i * j);
    }
}

// Filter for palindromic numbers
const palindromic = products.filter(
    x => x.toString() === x.toString().split('').reverse().join('')
);

// Find the biggest palindrome number
const sorted = palindromic.sort((a, b) => b - a);
const largest = sorted[0];

console.log(largest);
