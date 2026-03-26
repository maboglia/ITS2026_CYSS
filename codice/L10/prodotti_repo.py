import connessione

class ProdottiRepo:
    def __init__(self):
        self.conn = connessione.connect_to_database()
        self.cursor = self.conn.cursor()

    def get_prodotti(self):
        query = "SELECT * FROM Prodotti"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_prodotto_by_id(self, prodotto_id):
        query = "SELECT * FROM Prodotti WHERE id = %s"
        self.cursor.execute(query, (prodotto_id,))
        return self.cursor.fetchone()

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