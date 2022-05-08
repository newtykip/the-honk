from cmath import e, pi, sqrt, log
from _helpers import floatInput

i = sqrt(-1)

compute = lambda numerator, denominator: (numerator / denominator).real
computeInverse = lambda x: (-i * log(x, e)).real

sin = lambda x: compute(pow(e, i * x) - pow(e, -i * x), 2 * i)
cos = lambda x: compute(pow(e, i * x) + pow(e, -i * x), 2)
tan = lambda x: compute(pow(e, i * x) - pow(e, -i * x), i * (pow(e, i * x) + pow(e, -i * x)))
csc = lambda x: 1 / sin(x)
sec = lambda x: 1 / cos(x)
cot = lambda x: 1 / tan(x)

arcsin = lambda x: computeInverse((i * x) + sqrt(1 - pow(x, 2)))
arccos = lambda x: computeInverse(x + sqrt(pow(x, 2) - 1))
arctan = lambda x: computeInverse((i - x) / (i + x)) / 2
arccsc = lambda x: computeInverse((pow(x, -1) * i) + sqrt(1 - pow(x, -2)))
arcsec = lambda x: computeInverse((pow(x, -1)) + sqrt(pow(x, -2) - 1))
arccot = lambda x: computeInverse((x + i) / (x - i)) / 2

# todo: hyperbolic functions

# todo: hyperbolic inverse functions

# todo: hyperbolic reciprocal functions

# todo: hyperbolic inverse reciprocal functions

radians = floatInput("Please enter an amount of radians: ")

print(f"""
Trigometric functions

sin({radians}) = {sin(radians)}
cos({radians}) = {cos(radians)}
tan({radians}) = {tan(radians)}

Reciprocal trigometric functions

csc({radians}) = {csc(radians)}
sec({radians}) = {sec(radians)}
cot({radians}) = {cot(radians)}

Inverse trigometric functions 

arcsin({sin(radians)}) = {arcsin(sin(radians))}
arccos({cos(radians)}) = {arccos(cos(radians))}
arctan({tan(radians)}) = {arctan(tan(radians))}

Inverse reciprocal trigometric functions

arccsc({csc(radians)}) = {arccsc(csc(radians))}
arcsec({sec(radians)}) = {arcsec(sec(radians))}
arccot({cot(radians)}) = {arccot(cot(radians))}""")
