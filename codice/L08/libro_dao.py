from libro import Libro
from connessione_mysql import libreria

class LibroDAO:

    def __init__(self):
        self.libri = libreria
        self.processa_libri()


    def trasforma_in_libro(self, record) -> Libro:

        # id, Codice, Autore, Editore, Titolo, Classificazione

        id, codice, autore, editore, titolo, classificazione = record
        return Libro(id, codice, autore, editore, titolo, classificazione)
    
    def processa_libri(self):
        self.libri = [self.trasforma_in_libro(record) for record in self.libri]

    def aggiungi_libro(self, libro: Libro):
        self.libri.append(libro)

    def rimuovi_libro(self, id: int):
        self.libri = [libro for libro in self.libri if libro.id != id]

    def trova_libro_per_id(self, id: int) -> Libro:
        for libro in self.libri:
            if libro.id == id:
                return libro
        return None

    def trova_libri_per_autore(self, autore: str) -> list:
        return [libro for libro in self.libri if libro.autore == autore]
    
    def trova_libri(self):
        return self.libri