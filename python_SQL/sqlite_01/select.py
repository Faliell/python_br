import sqlite3
from main import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f"SELECT * FROM {TABLE_NAME}")

for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)


cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE ID = 2")

row1 = cursor.fetchone()
print(row1)


cursor.close()
connection.close()