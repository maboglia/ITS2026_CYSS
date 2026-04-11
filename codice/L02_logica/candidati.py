studenti = list(
    [['Davide ','Alfonso'],
    ['Lorenzo','Bracco'],
    ['Francesco','Burac'],
    ['Fabio','Di Vincenzo'],
    ['Andrea','Finocchielli'],
    ['Atef','Jmai'],
    ['Samuel Renato','Li Vigni'],
    ['Paolo','Moccia'],
    ['Tommaso','Molino'],
    ['Umberto','Nesta'],
    ['Cristian','Passiatore'],
    ['robert','pentiuc'],
    ['Marco','Prinzi'],
    ['Lorenzo','Raccis'],
    ['Marco Giacomo','Regaldo'],
    ['Flavio','Romanu'],
    ['Gabriele','Rosso'],
    ['Marco','Soffia'],
    ['Vincenzo','Tassone'],
    ['Ivan','Viarengo'],
    ['Abdelrahman','Zaher'],
    ['Alessandro','Valenza'],
    ['Alessio','Ordazzo'],
    ['erik','mocanu'],
    ['giovanni','verilio'],
    ['Enrico Guido','d\'Onofrio'],
    ['Christian','Torchia']]
)

risposte = [] # list inizialmente list()

candidati = [ ['Davide','Alfonso'], ['Andrea','Finocchielli'], ['Atef','Jmai'], ['Paolo','Moccia'], ['Cristian','Passiatore'], ['Marco','Regaldo'	], ['Flavio','Romanu'] ]

# 1) per ogni studente della collezione (list) di studenti
for s in studenti:
    # 2) presento all'utente un elenco di candidati
    print(f"{s[0]} {s[1]} scegli uno dei seguenti candidati:")
    # 3 scorro l'elenco dei candidati
    for c in candidati:
        # 4 stampo il cognome del candidato
        print(f"Il nome del candidato: {c[0]} e il cognome da scrivere {c[1]} ")
    # 5 registro la risposta dell'utente    
    risposta = input("Scrivi il cognome del candidato che vuoi votare")
    # 6 aggiungo la risposta all'elenco di risposte
    risposte.append(risposta)
    # 7 ripeto i punti da 2 a 6 (TODO: mettere questa logica in una funzione)
       # 2) presento all'utente un elenco di candidati
    print("Scegli uno dei seguenti candidati:")
    # 3 scorro l'elenco dei candidati
    for c in candidati:
        # 4 stampo il cognome del candidato
        print(f"Il nome del candidato: {c[0]} e il cognome da scrivere {c[1]} ")
    # 5 registro la risposta dell'utente    
    risposta = input("Scrivi il cognome del candidato che vuoi votare")
    # 6 aggiungo la risposta all'elenco di risposte
    risposte.append(risposta)
# 13 cicla le risposte
for r in risposte:
    # 14 stampa ogni risposta
    print(r)







