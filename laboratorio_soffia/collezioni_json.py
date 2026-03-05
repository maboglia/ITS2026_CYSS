import json

dizionario = {
    "nome": "Alice",
    "eta": 30,
    "citta": "Roma"
}

# Converti il dizionario in una stringa JSON
#json_string = json.dumps(dizionario, indent=4)
#print(json_string)  # Output: {"nome": "Alice", "eta": 30, "citta": "Roma"}

with open("dizionario.json", "w", encoding="utf-8") as file:
    json.dump(dizionario, file, indent=4)
    print("Dizionario salvato in dizionario.json")