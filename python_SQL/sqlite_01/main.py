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

# Com cuidado com SQL injection
sql = (f"INSERT INTO {TABLE_NAME} (name, weight)"
       "VALUES"
       "(?,?)"
       )

# cursor.execute(sql, ["Ana", 7])
cursor.executemany(sql, (["Ana", 7], ["Maria", 3], ["Beto", 4]))

connection.commit()

cursor.close()
connection.close()
