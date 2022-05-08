from cmath import e, sqrt, log
from _helpers import floatInput

i = sqrt(-1)

compute = lambda numerator, denominator: (numerator / denominator).real
ln = lambda x: log(x, e)

sin = lambda x: compute(pow(e, i * x) - pow(e, -i * x), 2 * i)
cos = lambda x: compute(pow(e, i * x) + pow(e, -i * x), 2)
tan = lambda x: compute(pow(e, i * x) - pow(e, -i * x), i * (pow(e, i * x) + pow(e, -i * x)))
csc = lambda x: 1 / sin(x)
sec = lambda x: 1 / cos(x)
cot = lambda x: 1 / tan(x)

arcsin = lambda x: (-i * ln((i * x) + sqrt(1 - pow(x, 2)))).real

# todo: finish arc functions
arccos = lambda x: None
arctan = lambda x: None
arccsc = lambda x: (-i * (ln((pow(x, -1) * i) + sqrt(1 - pow(x, -2))))).real
arcsec = lambda x: None
arccot = lambda x: None

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
