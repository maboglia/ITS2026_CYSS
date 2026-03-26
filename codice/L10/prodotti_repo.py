import connessione

class ProdottiRepo:
    def __init__(self):
        self.conn = connessione.Connessione()

    def get_prodotti(self):
        query = "SELECT * FROM prodotti"
        return self.conn.execute_query(query)

    def get_prodotto_by_id(self, prodotto_id):
        query = "SELECT * FROM prodotti WHERE id = %s"
        return self.conn.execute_query(query, (prodotto_id,))

    def add_prodotto(self, nome, prezzo):
        query = "INSERT INTO prodotti (nome, prezzo) VALUES (%s, %s)"
        self.conn.execute_query(query, (nome, prezzo))

    def update_prodotto(self, prodotto_id, nome, prezzo):
        query = "UPDATE prodotti SET nome = %s, prezzo = %s WHERE id = %s"
        self.conn.execute_query(query, (nome, prezzo, prodotto_id))

    def delete_prodotto(self, prodotto_id):
        query = "DELETE FROM prodotti WHERE id = %s"
        self.conn.execute_query(query, (prodotto_id,))