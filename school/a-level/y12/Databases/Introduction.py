from __future__ import annotations
import sqlite3
from sqlite3 import Connection, Cursor
from typing import Dict, List, Tuple
import os
import csv

class Modifiers:
    """
    Supported datatypes and their sqlite mappings.
    """
    PrimaryKey = 2 ** 0
    Integer = 2 ** 1
    Text = 2 ** 2
    Float = 2 ** 3
    Boolean = 2 ** 4

    def __init__(self):
        self.value = 0

    def has(self, modifier: Modifiers):
        return self.value & modifier != 0

    def __str__(self):
        """
        Get a string representation of the type associated with the modifier
        """
        if self.has(Modifiers.Integer):
            return "INT"
        elif self.has(Modifiers.Text):
            return "TEXT"
        elif self.has(Modifiers.Float):
            return "FLOAT"
        elif self.has(Modifiers.Boolean):
            return "BOOL"

    def __add__(self, modifier: Modifiers):
        # remove any type modifiers that might've already been there
        if self.has(Modifiers.Integer):
            self -= Modifiers.Integer
        elif self.has(Modifiers.Text):
            self -= Modifiers.Text
        elif self.has(Modifiers.Float):
            self -= Modifiers.Float
        elif self.has(Modifiers.Boolean):
            self -= Modifiers.Boolean
        
        self.value |= modifier
        return self

    def __iadd__(self, modifier: Modifiers):
        return self.__add__(modifier)

    def __sub__(self, modifier: Modifiers):
        self.value &= ~modifier
        return self

    def __isub__(self, modifier: Modifiers):
        return self.__sub__(modifier)

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

def determine_type(values: List[str]) -> Modifiers:
    modifier = Modifiers()

    """
    Predict the best type to store a given set of values in an sqlite database.
    """
    if values[0].lower() in ["true", "false"]:
        modifier += Modifiers.Boolean
        return modifier

    isNumeric = False

    for value in values:
        digits = [char.isnumeric() for char in value if char != "."]

        if digits.count(True) == len(digits):
            isNumeric = True
            value = float(value)

            if value % 1 != 0:
                modifier += Modifiers.Float
                return modifier

    if isNumeric:
        modifier += Modifiers.Integer
        return modifier
    else:
        modifier += Modifiers.Text
        return modifier

# todo: refactor output to pair up data values and their types
def read_csv(file_name: str) -> Tuple[List[str], List[Modifiers], List[List[str]]]:
    """
    Read a CSV file into a tuple of headers, predicted data types, and entries.
    """
    with open(f"{SCRIPT_DIR}\\{file_name}.csv") as f:
        reader = csv.reader(f)
        headers = [header.lower().strip() for header in next(reader)]
        data = list(reader)
        columns = list(zip(*data))
        types = [determine_type(columns[i]) for i in range(len(columns))]

    return (headers, types, data)

def connect(db_name: str) -> Connection:
    """
    Connect to a sqlite database given the name of the file.
    NOTE: the file extension is assumed to be db
    """
    return sqlite3.connect(f"{SCRIPT_DIR}\\{db_name}.db")

def create_table(name: str, columns: Dict[str, Modifiers], cursor: Cursor) -> Cursor:
    # generate columns definition
    columns = ', '.join(map(lambda col: f"{col[0]} {col[1]}", columns.items()))
    print(columns)

    # # drop table if it already exists
    # cursor.execute(f"DROP TABLE IF EXISTS {name}")

    # # create the table
    # return cursor.execute(f"CREATE TABLE {name} ({columns}\n)")

file_name = "sports_data"
headers, modifiers, data = read_csv(file_name)

# todo: add way to choose primary key

db = connect('test')
cur = db.cursor()
create_table(file_name, { header: type for header, type in zip(headers, modifiers) }, cur)
# # db.commit()

v = Modifiers()
v += Modifiers.Boolean
print(v.has(Modifiers.Boolean))
v += Modifiers.Text
print(v.has(Modifiers.Boolean))