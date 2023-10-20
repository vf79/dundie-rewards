"""Sqlite DB Example."""
import sqlite3

conn = sqlite3.connect("sql_example.db")
conn.execute("PRAGMA foreign_keys = ON;")

instructions = """\
CREATE TABLE if not exists person (
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar NOT NULL,
    email varchar UNIQUE NOT NULL,
    dept varchar NOT NULL,
    role varchar NOT NULL
);
---
CREATE TABLE if not exists balance (
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer UNIQUE NOT NULL,
    value integer NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
---
CREATE TABLE if not exists movement (
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer NOT NULL,
    value integer NOT NULL,
    date datetime NOT NULL,
    actor varchar NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
---
CREATE TABLE if not exists user (
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer UNIQUE NOT NULL,
    password varchar NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
"""

for instruction in instructions.split("---"):
    conn.execute(instruction)

conn.close()
