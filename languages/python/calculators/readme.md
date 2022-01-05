# calculators

Some extra information on the more complex topics (:

## Karatsuba Algorithm

### Useful Links

-   [Wikipedia](https://en.wikipedia.org/wiki/Karatsuba_algorithm)
-   [An amazing video on the topic](https://youtu.be/cCKOl5li6YM)

### The Pseudocode

```
function karatsuba (num1, num2)
    if (num1 < 10) or (num2 < 10)
        return num1 × num2 /* fall back to traditional multiplication */

    /* Calculates the size of the numbers. */
    m = min (size_base10(num1), size_base10(num2))
    m2 = floor (m / 2)
    /* m2 = ceil (m / 2) will also work */

    /* Split the digit sequences in the middle. */
    high1, low1 = split_at (num1, m2)
    high2, low2 = split_at (num2, m2)

    /* 3 recursive calls made to numbers approximately half the size. */
    z0 = karatsuba (low1, low2)
    z1 = karatsuba (low1 + high1, low2 + high2)
    z2 = karatsuba (high1, high2)

    return (z2 × 10 ^ (m2 × 2)) + ((z1 - z2 - z0) × 10 ^ m2) + z0
```
