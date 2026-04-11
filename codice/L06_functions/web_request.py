import urllib.request
import json

sito = 'https://raw.githubusercontent.com/maboglia/ProgrammingResources/refs/heads/master/tabelle/film/best-free-yt-movies-rt.json'

with urllib.request.urlopen(sito) as risposta:
    corpo_pagine_bytes = risposta.read()
    testo_finale = corpo_pagine_bytes.decode("utf-8")

movies = json.loads(testo_finale)

inserimenti = []

for movie in movies:
    titolo = movie.get('titolo', 'XYZ')
    rating = movie.get('rating', 'XYZ')
    rating = str(rating).replace('%', '')
    anno = movie.get('anno', 'XYZ')
    anno = str(anno).replace('(','').replace(')', '')
    regista = movie.get('regista', 'XYZ')
    query = f"INSERT INTO movies (titolo, anno, rating, regista) VALUES ('{titolo}', {anno}, {rating}, '{regista}');\n"
    inserimenti.append(query)

with open('database_movies.sql', 'w', encoding='utf-8') as f:
    creazione = f"""
        DROP TABLE IF EXISTS movies;
        CREATE TABLE movies(
            movie_id INT PRIMARY KEY AUTO_INCREMENT,
            titolo VARCHAR(100),
            anno INT NOT NULL default 0,
            rating int not null default 0,
            regista VARCHAR(100)
        
        );
    """
    f.write(creazione)

    for insert in inserimenti:
        f.write(insert)



