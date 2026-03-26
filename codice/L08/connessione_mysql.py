import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="cyss2026",
    password="cyss2026",
    database="biblioteca"
)


cursor = db.cursor()

cursor.execute("select id, Codice, Autore, Editore, Titolo, Classificazione from biblioteca")

libreria = cursor.fetchall()

cursor.close()
db.close()

