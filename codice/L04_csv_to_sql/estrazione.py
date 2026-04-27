""" Estrazione di dati da un file e generazione di query SQL per l'inserimento in un database. """

automobili = [] # ho costruito una list vuota

with open("auto.csv", "r", encoding="utf-8") as f:
    i = 0
    for line in f:
        if i > 0:  # Salta la prima riga (intestazione)
            marca, modello, cilindrata, prezzo = line.strip().split(",")
            automobili.append([marca.replace('"', ''), modello.replace('"', ''), cilindrata, prezzo])
#            print(f"INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('{marca.replace('"', '')}', '{modello.replace('"', '')}', {cilindrata}, {prezzo});")
        i += 1

with open("auto.sql", "w", encoding="utf-8") as output:

    output.write("USE cyss2026;\n\n")

    output.write("CREATE TABLE IF NOT EXISTS auto (\n")
    output.write("    id INT AUTO_INCREMENT PRIMARY KEY,\n")
    output.write("    marca VARCHAR(255) NOT NULL,\n")
    output.write("    modello VARCHAR(255) NOT NULL,\n")
    output.write("    cilindrata INT NOT NULL,\n")
    output.write("    prezzo DECIMAL(10, 2) NOT NULL\n")
    output.write(");\n\n")  

    for auto in automobili:
        marca = auto[0]
        modello = auto[1]
        cilindrata = auto[2]
        prezzo = auto[3]
        output.write(f"INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('{marca}', '{modello}', {cilindrata}, {prezzo});")
        output.write("\n")