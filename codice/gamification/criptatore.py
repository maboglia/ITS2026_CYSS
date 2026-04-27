""""criptatore e decriptatore di una frase"""
import string
import random

caratteri =  " " + string.ascii_letters + string.digits + string.punctuation 
caratteri = list(caratteri) #costruttore  di lista, converte la stringa in una lista di caratteri


chiavi = caratteri.copy() #copia della lista dei caratteri, per creare la chiave di decriptazione
random.shuffle(chiavi) #mescola la lista dei caratteri, per creare la chiave di decriptazione
#print(caratteri)
print(chiavi)

testo = input("Inserisci il testo da criptare: ")
testo_criptato = "" #stringa vuota, che conterrà il testo criptato
for carattere in testo:
    indice = caratteri.index(carattere)
    testo_criptato += chiavi[indice]
    
print (f"Testo originale {testo}")
print (f"Testo criptato {testo_criptato}")

testo_cifrato = input ("Inserisci il testo da decriptare: ")
testo_decriptato = ""
for carattere in testo_cifrato:
    indice = chiavi.index(carattere)
    testo_decriptato += caratteri[indice]

print (f"Testo cifrato {testo_cifrato}")
print (f"Testo decriptato {testo_decriptato}")