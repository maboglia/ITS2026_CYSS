"""  Modulo per sperimentare con i dadi le probabilità di uscita di un numero da 1 a 6. """

import random as rnd
import time

facce = 6
NUM_LANCI = 10_000_000
vittorie = 0

start_time = time.time()
for i in range(NUM_LANCI):
    dado1 = rnd.randint(1, facce)
    dado2 = rnd.randint(1, facce)
#    print(f"Dado 1: {dado1}, Dado 2: {dado2}")

    if dado1 == dado2:
#        print("Hai fatto doppio!")
        vittorie += 1

end_time = time.time()

print(f"Hai vinto {vittorie} volte su {NUM_LANCI} lanci.")
print(f"Probabilità di fare doppio: {vittorie / NUM_LANCI * 100:.2f}%")
print(f"Tempo impiegato: {end_time - start_time:.2f} secondi.")
