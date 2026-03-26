
class Libro:

    def __init__(self, id: int, Codice: str, Autore, Editore, Titolo, Classificazione):
        self.id = id
        self.codice = Codice
        self.autore = Autore
        self.editore = Editore
        self.titolo = Titolo
        self.classificazione = Classificazione

    def __str__(self):
        return f"{self.titolo} di {self.autore} ({self.classificazione})"

    def toHtml(self):
        return f"""
        <article>
        <h3>{self.titolo}</h3>
        <p><strong>Autore:</strong> {self.autore}</p>
        <p><strong>Classificazione:</strong> {self.classificazione}</p>
        </article>
        """