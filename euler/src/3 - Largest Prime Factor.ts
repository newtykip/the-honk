let number = 600851475143;
let i = 2;

while (i * i <= number) {
    if (number % i) i += 1;
    else number = Math.floor(number / i);
}

console.log(number);
