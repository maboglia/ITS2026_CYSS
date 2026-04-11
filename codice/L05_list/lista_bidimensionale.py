""" Lista a due dimensioni """


matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for riga in matrice:
    for x in riga:
        print(x, end=" ")
    print()