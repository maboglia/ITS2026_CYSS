import json

with open("dizionario.json", "r", encoding="utf-8") as file:
    dizionario_caricato = json.load(file)
    print(type(dizionario_caricato))  # Output: <class 'dict'>