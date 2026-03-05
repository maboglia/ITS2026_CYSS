# Ognugno crei una folder laboratorio_cognome e al suo interno strutture_dati.py

lista_voti = [7, 8, 9, 10, 6, 5]
lista_voti2 = list([7, 8, 9, 10, 6, 5]) 

# non possono contenere duplicati, non sono ordinati
set_voti = {7, 8, 9, 10, 9, 10}
print(set_voti)  # Output: {5, 6, 7, 8, 9, 10}
#print(type(set_voti))  # Output: <class 'set'>
#print(dir(set_voti))

#immutabili
tuple_voti = (7, 8, 9, 10, 6, 5)
print(tuple_voti)  # Output: (7, 8, 9, 10, 6, 5)
print(type(tuple_voti))  # Output: <class 'tuple'>

# Key uniche e values
dizionario_voti = {
    "Matematica": 7,
    "Italiano": 8,
    "Storia": 9,
    "Scienze": 10,
}

for materia, voto in dizionario_voti.items():
    print(f"{materia}: {voto}")  # Output: Matematica: 7, Italiano: 8, Storia: 9, Scienze: 10