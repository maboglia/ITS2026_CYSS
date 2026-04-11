""" giochiamo a sasso carta forbice """


import random

scelte = ["sasso", "carta", "forbice"]

while True:
    print(f"Gioca a {scelte}")
    umano = input(f"Scegli tra: {scelte}. Premi q per uscire ")

    if umano.lower() == 'q':
        break

    macchina = random.choice(scelte)

    print(f"Umano ha scelto {umano}")
    print(f"Macchina ha scelto {macchina}")

    if umano == macchina:
        print("Pareggio!")
    elif (umano == "sasso" and macchina == "forbice") or (umano == "carta" and macchina == "sasso") or (umano == "forbice" and macchina == "carta"):
        print("Ha vinto umano!")
    else:
        print("Hai vinto macchina!")


print("Game over")
print("Grazie per aver giocato con noi!")
