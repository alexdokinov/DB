import sqlite3
from faker import Faker

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

imprt = Faker()

for _ in range(1000):
    first_name = imprt.first_name()
    last_name = imprt.last_name()

    cursor.execute("INSERT INTO Teachers (first_name, last_name) VALUES (?, ?)", (first_name, last_name))

conn.commit()
conn.close()