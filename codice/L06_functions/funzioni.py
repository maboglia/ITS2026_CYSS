""" Funzioni in Python """

def presentazione(nome, cognome, sport = "nessuno sport"):
    print(f"Ciao, mi chiamo {nome} {cognome} e pratico {sport}!")

presentazione(cognome = "rossi", nome = "giovanni", sport = "calcio") # Chiamata alla funzione
presentazione(cognome = "verdi", nome = "giuseppe") # Chiamata alla funzione
presentazione("gino", "latino") # Chiamata alla funzione


