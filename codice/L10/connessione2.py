import mysql.connector
from flask import Flask, jsonify

db = mysql.connector.connect(
    host = 'localhost',
    user = 'cyss2026',
    password = 'cyss2026',
    database = 'magazzino'
)

cursore = db.cursor(dictionary=True)

cursore.execute("SELECT * FROM Prodotti")

records = cursore.fetchall()

# for record in records:
#     print(record.get('nome'))

app = Flask(__name__)

@app.get('/api/prodotti')
def prodotti():
    response = jsonify(records)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



app.run()
