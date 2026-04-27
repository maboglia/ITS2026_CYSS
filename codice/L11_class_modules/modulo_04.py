# importare con pip install requests
import requests
import csv

richiesta_auto = "https://raw.githubusercontent.com/maboglia/ProgrammingResources/refs/heads/master/tabelle/csv/auto.csv"
richiesta_moto = "https://raw.githubusercontent.com/maboglia/ProgrammingResources/refs/heads/master/tabelle/csv/moto.csv"

risposta_auto = requests.get(richiesta_auto)
risposta_moto = requests.get(richiesta_moto)

def produci_csv(file_name, risposta_http):
    with open(file_name, 'w', encoding='utf-8',newline='\n') as f:
        f.write(risposta_http.text)

    with open(file_name, mode="r", newline="", encoding="utf-8") as f:
        return [riga for riga in  csv.DictReader(f)  ]
        

auto = produci_csv('auto.csv', risposta_auto)
moto = produci_csv('moto.csv', risposta_moto)

for automobile in auto:
    print(automobile.get('Marca'))
