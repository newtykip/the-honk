const largestPallidromeNumber = (lowerBound: number, upperBound: number) => {
    // Work out all of the products of 3 digit numbers
    const products: number[] = [];

    for (let i = lowerBound; i < upperBound + 1; i++) {
        for (let j = lowerBound; j < upperBound + 1; j++) {
            products.push(i * j);
        }
    }

    // Filter for palindromic numbers
    const palindromic = products.filter(
        x => x.toString() === x.toString().split('').reverse().join('')
    );

    // Find the biggest palindrome number
    const sorted = palindromic.sort((a, b) => b - a);
    return sorted[0];
};

console.log(largestPallidromeNumber(100, 999));
