from prodotti_repo import ProdottiRepo

class MagazzinoService:
    def __init__(self):
        self.prodotti_repo = ProdottiRepo()

    def visualizza_prodotti(self):
        return self.prodotti_repo.get_prodotti()

    def aggiungi_prodotto(self, nome, prezzo):
        self.prodotti_repo.add_prodotto(nome, prezzo)

    def aggiorna_prodotto(self, prodotto_id, nome, prezzo):
        self.prodotti_repo.update_prodotto(prodotto_id, nome, prezzo)

    def elimina_prodotto(self, prodotto_id):
        self.prodotti_repo.delete_prodotto(prodotto_id)