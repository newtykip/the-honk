from dataclasses import dataclass, field
from enum import Enum
from typing import List

toppings = {
    'special cheese': 0.75,
    'bacon': 1.25,
    'chicken': 1.99,
    'spicy beef': 1.25,
    'pepperoni': 1.25,
    'pineapple': 0.00,
    'cream egg': 0.99,
    'chillies': 0.50,

    'smelly cheese': 0.99,
    'organic meat': 2.99,
    'doner meat': 3.45,
    'olives': 1.99,

    'ham': 2.00
}

class Crust(Enum):
    Normal = 0
    Thin = 1

@dataclass
class Pizza:
    __slices: int
    __crust: Crust
    __toppings: List[str] = field(default_factory=list)

    def calculatePrice(self):
        # 1 slice for £1
        cost = self.__slices
        pizzaToppings = list(map(lambda x: x.lower(), self.__toppings))

        # Add the price of the toppings
        for topping in toppings.keys():
            if topping in pizzaToppings:
                cost += toppings[topping]

        return cost

    def updateSlices(self, newSlices: int):
        self.slice = newSlices

        return self

margherita = Pizza(10, Crust.Thin, ['tomato sauce', 'basic cheese'])
hawaiian = Pizza(17, Crust.Thin, ['tomato sauce', 'smelly cheese', 'pineapple', 'ham'])

print(margherita.calculatePrice(), hawaiian.calculatePrice())
