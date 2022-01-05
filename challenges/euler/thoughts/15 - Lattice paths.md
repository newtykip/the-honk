For a lattice with dimensions m x n, all paths will have m + n segments. m segments go down, n segments go right. To count m + n slots, count the ways to pick m downward moves - the rest will be rightward moves.

![](assets/15.svg)

### LaTeX

```
{m + n \choose m} = {m + n \choose n} = \frac{(m+n)!}{m!n!}
```
