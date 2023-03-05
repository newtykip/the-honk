from __future__ import annotations
from pickle import load, dump
from dataclasses import dataclass
from sys import path as sysPath
from os.path import join as pathJoin, exists as pathExists
from typing import List, Callable, TypeVar
from time import sleep

class ExistsError(Exception):
    pass

@dataclass
class Product:
    name: str
    price: float
    formatString = " {:^30} | {:^10} "
    currency = "£"

    @staticmethod
    def format(product: Product, currency: str) -> str:
        return Product.formatString.format(product.name, f"{currency}{product.price:.2f}")

class Products:
    def __init__(self, friendlyName: str, currency: str = "£"):
        self.__products: List[Product] = []
        self.__file = self.getPath(friendlyName)
        self.__currency = currency

    @staticmethod
    def getPath(friendlyName: str) -> str:
        return pathJoin(sysPath[0], f"{friendlyName}.products")

    @staticmethod
    def From(friendlyName: str, currency: str = "£"):
        path = Products.getPath(friendlyName)

        if not pathExists(path):
            return Products(friendlyName, currency)

        with open(path, "rb") as f:
            data = load(f)
            products = Products(friendlyName, data["currency"])

            for product in data["products"]:
                products.add(product)

            return products

    def __save(self) -> Products:
        """Save all of the products to a file."""
        with open(self.__file, "wb") as f:
            dump({
                "products": self.__products,
                "currency": self.__currency
            }, f)

        return self

    def exists(self, name: str) -> Product:
        """Checks if a product with that name already exists"""
        for product in self.__products:
            if product.name.lower() == name.lower():
                return product

        return None

    def setCurrency(self, currency: str) -> Products:
        self.__currency = currency
        return self.__save()

    def add(self, product: Product) -> Products:
        """Add a product to the list."""
        if self.exists(product.name):
            raise ExistsError(f"A product called {product.name} already exists!")

        self.__products.append(product)
        return self.__save()
    
    def remove(self, name: str) -> Products:
        """Remove a product from the list"""
        for i, product in enumerate(self.__products):
            if product.name.lower() == name.lower():
                del self.__products[i]
        
        return self.__save()

    def clear(self) -> Products:
        """Clear the list of products"""
        self.__products = []
        return self.__save()

    def __str__(self) -> str:
        header = Product.formatString.format("Name", "Price")
        divider = "-" * len(header)
        out = f"{header}\n{divider}"

        for product in self.__products:
            out += f"\n{Product.format(product, self.__currency)}"

        return out
    
    def __add__(self, product: Product) -> Products:
        return self.add(product)
            
    def __getitem__(self, index: int) -> Product:
        return self.__products[index]

    def __setitem__(self, index: int, product: Product):
        self.__products[index] = product
        self.__save()
    
    def __len__(self) -> int:
        return len(self.__products)

T = TypeVar("T")

def getInput(caster: Callable[[str], T], prompt: str, error: str, validator: Callable[[T], bool] = None) -> T:
    while True:
        try:
            value = caster(input(prompt))

            if validator and validator(value):
                raise ValueError

            return value
        except ValueError:
            print(error)

def getProduct() -> Product:
    name = input("Please enter a name for the product: ")
    price = getInput(float, "Please enter a price for the product: ", "Please ensure that your input was a valid float!", lambda x: x <= 0)

    return Product(name, price)

def clear():
    print('\n' * 50)

if __name__ == "__main__":
    # Load a product list
    name = input("Please enter the name of a list of products: ")
    products = Products.From(name.lower())
    
    if len(products) == 0:
        print(f"Created new products list \"{name}\"")
    else:
        print(f"Loaded pre-existing product list \"{name}\"")

    # Main menu loop
    while True:
        clear()
        print("""1) View the list of products
2) Add a product
3) Remove a product
4) Update currency
5) Clear the list of products
6) Exit
""")

        choice = getInput(int, "What would you like to do? (1-5): ", "Please choose a valid option.", lambda x: x < 1 or x > 6)
        print()
        
        if choice == 1:
            print(products)
        elif choice == 2:
            while True:
                try:
                    product = getProduct()
                    products.add(product)
                    break
                except ExistsError:
                    print("Please make sure the product's name is unique!")

            print(f"Added product {product}")
        elif choice == 3:
            while True:
                name = input("Please enter the name of a product to remove: ")
                product = products.exists(name)

                if product:
                    break

                print("Make sure you enter the name of a valid product!")
            
            products.remove(name)
            print(f"Removed product {product}")
        elif choice == 4:
            currency = input("Please enter a new currency symbol: ")
            products.setCurrency(currency)
            print(f"Currency symbol updated to {currency}")
        elif choice == 5:
            products.clear()
            print("Cleared list of products.")
        elif choice == 6:
            exit()

        sleep(1)
