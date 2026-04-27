
# istruzioni in sequenza

# print("Quando l'acqua bolle aggiungi la pasta")
# print("Metti l'acqua nella pentola")
# print("Metti la pentola sul fuoco")
# print("Quando la pasta è cotta scola la pasta")

# selezione - scelta

# logged = False

# if logged:
#     print("è vero")
# else:
#     print("è falso")


# iterazione - ripetizione

gira = True
volte = 100

while gira:
    print("finché la barca va, lasciala andare", volte)
    # volte = volte - 1
    volte -= 1

    if volte == 0:
        break