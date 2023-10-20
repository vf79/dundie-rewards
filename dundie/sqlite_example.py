import sqlite3

con = sqlite3.connect("sql_example.db")
con.execute("PRAGMA foreign_keys = ON;")

# instruction ="""\
# INSERT INTO person (name, dept, role, email)
# VALUES ('Dwight Schrute', 'Sales', 'Manager', 'schrute@dundlermifflin.example.com');
# """
#
# con.execute(instruction)
# con.commit()

# instruction = """\
# SELECT id, name, email, dept, role
# FROM person
# WHERE dept = 'Sales';
# """
#
# cur = con.cursor()
# result = cur.execute(instruction)
# for row in result:
#     print(row)
instruction = """\
SELECT id, 500 FROM person WHERE dept = 'Sales';
"""

cur = con.cursor()
result = cur.execute(instruction)
for row in result:
    # instruction = "INSERT INTO balance (person, value) VALUES (?, ?);"
    # con.execute(instruction, row)
    print(row)

#con.commit()