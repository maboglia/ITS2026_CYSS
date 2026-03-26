

class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def __str__(self):
        return f"{self.nome}: {self.prezzo}€"
    
    def __repr__(self):
        return f"nome: {self.nome}, prezzo: {self.prezzo}€"