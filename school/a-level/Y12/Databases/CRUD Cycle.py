import sqlite3
import os
import csv
from typing import Tuple
from dataclasses import dataclass, fields

@dataclass
class Person:
    male: bool
    age: int
    height: int
    weight: int
    bmi: float
    vo2: float

    def __iter__(self):
        for field in fields(self):
            yield getattr(self, field.name)

# C
def create_person(data: Person):
    cur.execute("INSERT INTO people(male, age, height, weight, bmi, vo2) VALUES(?, ?, ?, ?, ?, ?)", list(data))

# R
def read_person(id: int) -> Tuple[bool, int, int, float, float]:
    res = cur.execute("SELECT * FROM people WHERE id = ?", [id])
    return res.fetchone()

# U
def update_person(id: int, data: Person):
    set_query = []
    parameters = []

    if data.male is not None:
        set_query.append("male = ?")
        parameters.append(data.male)
    if data.age is not None:
        set_query.append("age = ?")
        parameters.append(data.age)
    if data.height is not None:
        set_query.append("height = ?")
        parameters.append(data.height)
    if data.weight is not None:
        set_query.append("weight = ?")
        parameters.append(data.height)
    if data.bmi is not None:
        set_query.append("bmi = ?")
        parameters.append(data.bmi)
    if data.vo2 is not None:
        set_query.append("vo2 = ?")
        parameters.append(data.vo2)

    cur.execute(f"UPDATE people SET {', '.join(set_query)} WHERE id = ?", [*parameters, id])

# D
def delete_person(id: int):
    cur.execute("DELETE FROM people WHERE id = ?", [id])

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

db = sqlite3.connect(f"{SCRIPT_DIR}\\sports.sqlite")
cur = db.cursor()

# create table
PEOPLE_SCHEMA = """CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    male BOOL,
    age INT,
    height INT,
    weight INT,
    bmi FLOAT,
    vo2 FLOAT,
    UNIQUE(male, age, height, weight, bmi, vo2)
)"""

cur.execute(PEOPLE_SCHEMA)

# populate with default data if it is not there
def populate():
    with open(f"{SCRIPT_DIR}\\sports_data.csv") as f:
        reader = csv.reader(f)
        next(reader) # get rid of the headers

        for row in reader:
            create_person(Person(*row))

# save
db.commit()
