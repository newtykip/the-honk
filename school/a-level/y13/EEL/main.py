from __future__ import annotations
from typing import Tuple, Callable
from dataclasses import dataclass
from uuid import uuid4 as generate_id
from math import pi
import eel

FRIENDLY = {
    "gal": "imperial gallon",
    "gallon": "imperial gallon",
    "l": "litre",
    "in": "inch",
    "mm": "millimetre",
    "ac": "acre",
    "sq m": "square metre",
    "sq metre": "square metre",
    "square metre": "square metre",
    "square m": "square metre",
    "usd": "USD",
    "gbp": "GBP",
    "inr": "INR",
    "irr": "IRR",
    "day": "day",
    "min": "minute",
    "minute": "minute"
}

@dataclass
class Conversion:
    base: Tuple[str]
    target: Tuple[str]
    compute: Callable[[float], float]
    inverse: Callable[[float], float]

class NamePair:
    friendly: str
    acronym: str

    def __init__(self, acronym: str):
        self.acronym = acronym
        self.friendly = FRIENDLY.get(acronym)
    
    def __str__(self) -> str:
        return f"{self.friendly} ({self.acronym})"

GALLON_CONST = 3.786411784
INCH_CONST = 25.4
ACRE_CONST = 4046.85642
USD_CONST = 0.82
INR_CONST = 0.0099
IRR_CONST = 0.000019
DAY_CONST = 1440

UNIT_CONVERSIONS = [
    Conversion(("gal", "gallon"), ("l"), lambda gallons: gallons * GALLON_CONST, lambda litres: litres / GALLON_CONST),
    Conversion(("in"), ("mm"), lambda inches: inches * INCH_CONST, lambda mm: mm / INCH_CONST),
    Conversion(("ac"), ("sq m", "sq metre", "square metre", "square m"), lambda acres: acres * ACRE_CONST, lambda sq_m: sq_m / ACRE_CONST),
    Conversion(("usd"), ("gbp"), lambda usd: round(usd * USD_CONST, 2), lambda gbp: round(gbp / USD_CONST, 2)),
    Conversion(("inr"), ("gbp"), lambda inr: round(inr * INR_CONST, 2), lambda gbp: round(gbp / INR_CONST, 2)),
    Conversion(("irr"), ("gbp"), lambda irr: round(irr * IRR_CONST, 2), lambda gbp: round(gbp / IRR_CONST, 2)),
    Conversion(("day"), ("min", "minute"), lambda days: days * DAY_CONST, lambda minutes: minutes / DAY_CONST)
]

def parse_unit(unit: str) -> NamePair:
    # find acronym from friendly name
    if unit in FRIENDLY.values():
        for acronym in FRIENDLY.keys():
            if unit == FRIENDLY[acronym]:
                unit = acronym
                break

    return NamePair(unit)

@eel.expose
def convert_units(base: str, target: str, quantity: float) -> str:
    # singularise units
    if base.endswith("s"):
        base = base[0:len(base) - 1]
    if target.endswith("s"):
        target = target[0:len(target) - 1]

    # resolve friendly names and acronyms
    base = parse_unit(base)
    target = parse_unit(target)

    print(base, target)

    # resolve conversion
    calculate = None

    for conversion in UNIT_CONVERSIONS:
        if base.acronym in conversion.base and target.acronym in conversion.target:
            calculate = conversion.compute
            break
        elif target.acronym in conversion.base and base.acronym in conversion.target:
            calculate = conversion.inverse
            break

    if calculate == None:
        base_p = "es" if base.acronym == "in" else "s"
        target_p = "es" if target.acronym == "in" else "s"

        return f"Failed to convert {base.friendly}{base_p} to {target.friendly}{target_p}."

    # compute the result
    result = calculate(quantity)
    base_p = "es" if base.acronym == "in" else "s" if quantity > 1 else ""
    target_p = "es" if base.acronym == "in" else "s" if result > 1 else ""

    return f"{quantity} {base.friendly}{base_p} is {result} {target.friendly}{target_p}."

@eel.expose
def calculate_fuel(miles: float) -> str:
    gallons = miles / 17

    return f"You need {gallons} gallons of fuel to travel {miles} miles."

@eel.expose
def surface_area(diameter: float) -> str:
    area = pi * pow(diameter, 2) / 4

    return f"The surface area of a circular field with a diameter of {diameter} metres is {area} square metres."

@eel.expose
def save(response: str):
    id = generate_id()

    with open(f"out/{id}.txt", "w") as file:
        file.write(response)

    return id

eel.init("www")
eel.start("index.html")
