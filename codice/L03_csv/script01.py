# base: int = 7
# altezza: int = 5
# area: float = (base * altezza) / 2
# print("L'area del triangolo è:", area)


libri = [
    ['1984', 150, 10.50, 3],
    ['500 ricette di piatti unici', 150, 22, 3],
    ['Il Giudizio di Salomone', 250, 18, 3],
    ['Alice\'s Adventures in Wonderland', 10, 30.50, 3],
    ['Annus horribilis', 100, 8.50, 3],
    ['C# 2005 Guida per lo sviluppatore', 80, 10.00, 3],
    ['Camminando. Incontri di un viandante', 200, 20.50, 3],
    ['Come disegnare la figura vestita', 10, 15.50, 3]
]

for libro in libri:
    titolo = libro[0]
    pagine = libro[1]
    prezzo = libro[2]
    editore_id = libro[3]
    print(f"INSERT INTO libri SET titolo='{titolo}', pagine= {pagine}, prezzo= {prezzo}, editore_id= {editore_id};")