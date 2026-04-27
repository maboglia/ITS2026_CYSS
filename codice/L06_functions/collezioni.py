import json

regioni = {
    "Piemonte": ["Torino", "Novara", "Cuneo", "Asti", "Alessandria"],
    "Lombardia": ["Milano", "Bergamo", "Brescia", "Como", "Varese"],
    "Veneto": ["Venezia", "Verona", "Padova", "Vicenza", "Treviso"],
    "Toscana": ["Firenze", "Pisa", "Siena", "Arezzo", "Lucca"]
}

chiavi = regioni.keys()
# print(chiavi) # dict_keys(['Piemonte', 'Lombardia', 'Veneto', 'Toscana'])

valori = regioni.values()
# print(valori) # dict_values([['Torino', 'Novara', 'Cuneo', 'Asti', 'Alessandria'], ['Milano', 'Bergamo', 'Brescia', 'Como', 'Varese'], ['Venezia', '


# for regione, lista_comuni in regioni.items():
#     print(f"La regione {regione} ha {len(lista_comuni)} comuni capoluogo: {lista_comuni}")


file_json = json.dumps(regioni, indent = 4)

print(help(json.dump))

with open('regioni.json', 'w', encoding = 'utf8') as f:
    json.dump(regioni, f, indent=4)
