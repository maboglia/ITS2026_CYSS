import sqlite3
import json

conn = sqlite3.connect('movies.db')
# Il cursore permette di scorrere il database e di eseguire query SQL
cursor = conn.cursor()

with open("best-movies-2023-rt.json", "r", encoding="utf-8") as file:
    movies = json.load(file)

query_tabella = """
CREATE TABLE if not EXISTS movies (
    id integer PRIMARY KEY AUTOINCREMENT,
    titolo text NOT NULL,
    anno INT,
    rating FLOAT,
    regista text
);
"""

cursor.execute(query_tabella)

for movie in movies:
    anno = movie.get("anno", "(0)").replace("(", "").replace(")", "")
    rating = movie.get("rating", "0.0%").replace("%", "")
    titolo = movie.get("titolo", "N/A").replace("'", "''")  # Gestisce eventuali apostrofi nel titolo
    regista = movie.get("regista", "N/A").replace("'", "''")  # Gestisce eventuali apostrofi nel nome del regista

    # stampa la query di inserimento per ogni film
    cursor.execute(f"INSERT INTO movies (titolo, anno, rating, regista) VALUES ('{titolo}', {anno}, {rating}, '{regista}');\n")
conn.commit()
conn.close()