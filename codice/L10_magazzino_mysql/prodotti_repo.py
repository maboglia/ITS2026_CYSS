import connessione
from prodotto import Prodotto

class ProdottiRepo:
    def __init__(self):
        self.conn = connessione.connect_to_database()
        self.cursor = self.conn.cursor()

    def get_prodotti(self):
        query = "SELECT nome, prezzo_unitario FROM Prodotti"
        self.cursor.execute(query)
        prodottiDB = self.cursor.fetchall()
        return [Prodotto(nome, prezzo_unitario) for nome, prezzo_unitario in prodottiDB]

    def get_prodotto_by_id(self, prodotto_id):
        query = "SELECT * FROM Prodotti WHERE id = %s"
        self.cursor.execute(query, (prodotto_id,))
        row = self.cursor.fetchone()
        if row:
            return Prodotto(row[1], row[2])
        return None

    def add_prodotto(self, nome, prezzo):
        query = "INSERT INTO Prodotti (nome, prezzo) VALUES (%s, %s)"
        self.cursor.execute(query, (nome, prezzo))
        self.conn.commit()

    def update_prodotto(self, prodotto_id, nome, prezzo):
        query = "UPDATE Prodotti SET nome = %s, prezzo = %s WHERE id = %s"
        self.cursor.execute(query, (nome, prezzo, prodotto_id))
        self.conn.commit()

    def delete_prodotto(self, prodotto_id):
        query = "DELETE FROM Prodotti WHERE id = %s"
        self.cursor.execute(query, (prodotto_id,))
        self.conn.commit()