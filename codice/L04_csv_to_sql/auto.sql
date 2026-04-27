USE cyss2026;

CREATE TABLE IF NOT EXISTS auto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(255) NOT NULL,
    modello VARCHAR(255) NOT NULL,
    cilindrata INT NOT NULL,
    prezzo DECIMAL(10, 2) NOT NULL
);

INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Fiat', 'Punto', "1200", "9500");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Ford', 'Focus', "1600", "18000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Volkswagen', 'Golf', "2000", "24000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Toyota', 'Yaris', "1500", "17000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('BMW', 'Serie 3', "2000", "35000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Audi', 'A4', "2500", "42000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Mercedes', 'Classe A', "1600", "33000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Peugeot', '208', "1200", "14500");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Renault', 'Clio', "1400", "15500");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Hyundai', 'i20', "1400", "16000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Honda', 'Civic', "1800", "22000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Skoda', 'Octavia', "1600", "21000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Opel', 'Corsa', "1300", "14000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Tesla', 'Model 3', "0 (elettrica)", "48000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Nissan', 'Qashqai', "1600", "25000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Jeep', 'Renegade', "1400", "26000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Alfa Romeo', 'Giulia', "2000", "40000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Citroen', 'C3', "1200", "13500");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Kia', 'Sportage', "1600", "23000");
INSERT INTO auto (marca, modello, cilindrata, prezzo) VALUES ('Subaru', 'Impreza', "2000", "27000");
