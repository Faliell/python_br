import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# APAGAR todos os dados da tabela (sem WHERE)
cursor.execute(
    f"DELETE FROM {TABLE_NAME}"
)

# ZERAR os ids das Tabelas
cursor.execute(
    f"DELETE FROM sqlite_sequence WHERE name='{TABLE_NAME}'"
)

# Criar tabela
cursor.execute(
    f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
    "("
    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "name TEXT,"
    "weight REAL"
    ")"
)

connection.commit()

# Inserir dados

# cursor.execute(
#     f"INSERT INTO {TABLE_NAME} (id, name, weight)"
#     "VALUES"
#     "(NULL, 'Fabio', 9.9),(NULL, 'Giuliana', 6.9)"
# )

# # Com cuidado com SQL injection
# sql = (f"INSERT INTO {TABLE_NAME} (name, weight)"
#        "VALUES"
#        "(?,?)"
#        )
#
# # cursor.execute(sql, ["Ana", 7])
# cursor.executemany(sql, (["Ana", 7], ["Maria", 3], ["Beto", 4]))


# Com cuidado com SQL injection - Dict
sql = (f"INSERT INTO {TABLE_NAME} (name, weight)"
       "VALUES"
       "(:nome,:peso)"
       )

# cursor.execute(sql, {"nome": "Ana", "peso": 4})
cursor.executemany(sql, (
    {"nome": "Ana", "peso": 4},
    {"nome": "Maria", "peso": 2},
    {"nome": "Zé", "peso": 5}
))


connection.commit()

if __name__ == "__main__":
    print(sql)

    cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE ID = 2")

    cursor.execute(f"SELECT * FROM {TABLE_NAME}")

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.execute(f"UPDATE {TABLE_NAME} SET name='Outro' WHERE ID = 1")

    cursor.execute(f"SELECT * FROM {TABLE_NAME}")

    print("------")
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
