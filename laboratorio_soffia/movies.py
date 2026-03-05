import json

with open("best-movies-2023-rt.json", "r", encoding="utf-8") as file:
    movies = json.load(file)

# print(type(movies))  # Output: <class 'list'>
# print(type(movies[0]))  # Output: <class 'dict'>

query_tabella = """
CREATE TABLE movies (
    id int PRIMARY KEY AUTO_INCREMENT,
    titolo VARCHAR(255) NOT NULL,
    anno INT,
    rating FLOAT,
    regista VARCHAR(255)
);
"""
with open("query_movies.sql", "w", encoding="utf-8") as file:
    file.write(query_tabella)
    print("Query per la creazione della tabella salvata in query_movies.sql")

    for movie in movies:
        anno = movie.get("anno", "(0)").replace("(", "").replace(")", "")
        rating = movie.get("rating", "0.0%").replace("%", "")
        titolo = movie.get("titolo", "N/A").replace("'", "''")  # Gestisce eventuali apostrofi nel titolo
        regista = movie.get("regista", "N/A").replace("'", "''")  # Gestisce eventuali apostrofi nel nome del regista

        # stampa la query di inserimento per ogni film
        file.write(f"INSERT INTO movies (titolo, anno, rating, regista) VALUES ('{titolo}', {anno}, {rating}, '{regista}');\n")