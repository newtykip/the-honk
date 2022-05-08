from cmath import e, sqrt
from _helpers import floatInput

i = sqrt(-1)

compute = lambda numerator, denominator: (numerator / denominator).real
sin = lambda x: compute(pow(e, i * x) - pow(e, -i * x), 2 * i)
cos = lambda x: compute(pow(e, i * x) + pow(e, -i * x), 2)
tan = lambda x: compute(pow(e, i * x) - pow(e, -i * x), i * (pow(e, i * x) + pow(e, -i * x)))
radians = floatInput("Please enter an amount of radians: ")

print(f"""
sin({radians}) = {sin(radians)})
cos({radians}) = {cos(radians)}
tan({radians}) = {tan(radians)}

csc({radians}) = {1 / sin(radians)}
sec({radians}) = {1 / cos(radians)}
cot({radians}) = {1 / tan(radians)}""")
