from magazzino_service import MagazzinoService
from flask import Flask, request, jsonify

app = Flask(__name__)
magazzino_service = MagazzinoService()

@app.route('/api/prodotti', methods=['GET'])
def visualizza_prodotti():
    prodotti = magazzino_service.visualizza_prodotti()
    return jsonify([{"nome": prodotto.nome, "prezzo": prodotto.prezzo} for prodotto in prodotti])

if __name__ == '__main__':
    app.run(debug=True)


