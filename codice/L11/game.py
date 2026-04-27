"""Slot-Machine: un grande classico dei video games"""
import random
import time


def spin_row():
    symbols = ['🍒','🍋','💎','🍀','🔔']
    row = []

    for _ in range(3):
        simbolo = random.choice(symbols)
        row.append(simbolo)
    return row

def print_row(row):
    print()
    print("*" * 15)
    print(  " | ".join(row)  )
    print("*" * 15)
    print()
    
def calculate_win(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return 2 * bet
        elif row[0] == '🍋':
            return 3 * bet
        elif row[0] == '💎':
            return 5 * bet
        elif row[0] == '🍀':
            return 10 * bet
        elif row[0] == '🔔':
            return 20 * bet
    return 0

def main():
    credits = 100

    while credits > 0:
        print("\n" * 5)
        print("------------------------")
        print("Slot-Machine CyberSicura")
        print("🍒 🍋 💎 🍀 🔔")
        print("------------------------")

        bet = input("Quanto vuoi puntare? (1-100) ")

        if not bet.isdigit():
            print("Inserisci un numero tra 1 e 100")
            continue
        
        bet = int(bet)

        if bet <= 0:
            print("Inserisci un numero maggiore di 0")
            continue

        if bet > credits:
            print(f"Non puoi puntare {bet} perché hai solo {credits} crediti")
            continue

        credits -= bet
        print(f"Hai puntato {bet} crediti")
        
        print("Gira la ruota...")
        time.sleep(3)
        # faccio girare la slot-machine
        row = spin_row()
        
        #printo la riga uscita
        print_row(row)
        win = calculate_win(row, bet)

        credits += win

        if win > 0:
            print(f"HAI VINTO {win} crediti !!!!!!!!!!!!!!!!!!!!!!")
        else:
            print("Non hai vinto, ritenta!")


        print(f"Hai ancora {credits} crediti")
        
        if credits == 0:
            print("Hai finito i crediti, GAME OVER!")
            break

        play_again = input("Vuoi continuare? (Y/N)").upper()

        if play_again == 'Y':
            print("Grazie per aver giocato con noi!")
            break

    
    print("Game over!")


if __name__ == '__main__':
    main()
