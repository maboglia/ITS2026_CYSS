""" Calcola la media dei voti di uno studente """

def calcola_media(*voti):
    somma = 0
    for voto in voti:
        somma += voto
    return somma / len(voti)

# voti_studente = [6, 7, 8, 9, 10]

media = calcola_media(6, 7, 8, 9, 10)
print(f"La media dei voti dello studente è: {media}")

media = calcola_media(6, 7, 8, 9, 10, 6, 7, 8, 9, 10, 6, 7, 8, 9, 10)
print(f"La media dei voti dello studente è: {media}")