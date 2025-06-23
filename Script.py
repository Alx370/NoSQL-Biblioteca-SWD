import json
from pathlib import Path

output_dir = Path.home() / "Desktop" / "json_biblioteca"
output_dir.mkdir(exist_ok=True)

autori = [
  { "_id": "A1", "nome": "Umberto Eco", "data_nascita": "1932-01-05", "nazionalita": "Italiana" },
  { "_id": "A2", "nome": "J.K. Rowling", "data_nascita": "1965-07-31", "nazionalita": "Britannica" },
  { "_id": "A3", "nome": "George Orwell", "data_nascita": "1903-06-25", "nazionalita": "Britannica" },
  { "_id": "A4", "nome": "Italo Calvino", "data_nascita": "1923-10-15", "nazionalita": "Italiana" },
  { "_id": "A5", "nome": "Stephen King", "data_nascita": "1947-09-21", "nazionalita": "Americana" },
  { "_id": "A6", "nome": "Agatha Christie", "data_nascita": "1890-09-15", "nazionalita": "Britannica" },
  { "_id": "A7", "nome": "Isaac Asimov", "data_nascita": "1920-01-02", "nazionalita": "Americana" },
  { "_id": "A8", "nome": "Haruki Murakami", "data_nascita": "1949-01-12", "nazionalita": "Giapponese" },
  { "_id": "A9", "nome": "Jane Austen", "data_nascita": "1775-12-16", "nazionalita": "Britannica" },
  { "_id": "A10", "nome": "Franz Kafka", "data_nascita": "1883-07-03", "nazionalita": "Austro-Ungarica" }
]

libri = [
  { "_id": "L1", "titolo": "Il nome della rosa", "descrizione": "Giallo medievale", "anno_pubblicazione": 1980, "categoria": { "nome": "Giallo", "descrizione": "Romanzi polizieschi o investigativi" }, "autori": ["A1"], "copie_disponibili": 2 },
  { "_id": "L2", "titolo": "Harry Potter e la Pietra Filosofale", "descrizione": "Fantasy", "anno_pubblicazione": 1997, "categoria": { "nome": "Fantasy", "descrizione": "Narrativa ambientata in mondi immaginari con magia" }, "autori": ["A2"], "copie_disponibili": 5 },
  { "_id": "L3", "titolo": "1984", "descrizione": "Distopia totalitaria", "anno_pubblicazione": 1949, "categoria": { "nome": "Fantascienza", "descrizione": "Narrativa con elementi scientifici futuristici" }, "autori": ["A3"], "copie_disponibili": 3 },
  { "_id": "L4", "titolo": "Se una notte d’inverno un viaggiatore", "descrizione": "Metaromanzo", "anno_pubblicazione": 1979, "categoria": { "nome": "Narrativa", "descrizione": "Romanzi e racconti non di genere specifico" }, "autori": ["A4"], "copie_disponibili": 1 },
  { "_id": "L5", "titolo": "Shining", "descrizione": "Horror psicologico", "anno_pubblicazione": 1977, "categoria": { "nome": "Horror", "descrizione": "Storie concepite per spaventare o inquietare" }, "autori": ["A5"], "copie_disponibili": 4 },
  { "_id": "L6", "titolo": "Assassinio sull'Orient Express", "descrizione": "Giallo", "anno_pubblicazione": 1934, "categoria": { "nome": "Giallo", "descrizione": "Romanzi polizieschi o investigativi" }, "autori": ["A6"], "copie_disponibili": 2 },
  { "_id": "L7", "titolo": "Io, Robot", "descrizione": "Robotica e IA", "anno_pubblicazione": 1950, "categoria": { "nome": "Fantascienza", "descrizione": "Narrativa con elementi scientifici futuristici" }, "autori": ["A7"], "copie_disponibili": 3 },
  { "_id": "L8", "titolo": "Norwegian Wood", "descrizione": "Romantico e introspettivo", "anno_pubblicazione": 1987, "categoria": { "nome": "Narrativa", "descrizione": "Romanzi e racconti non di genere specifico" }, "autori": ["A8"], "copie_disponibili": 2 },
  { "_id": "L9", "titolo": "Orgoglio e Pregiudizio", "descrizione": "Amore e società", "anno_pubblicazione": 1813, "categoria": { "nome": "Classico", "descrizione": "Opere della letteratura considerate fondamentali" }, "autori": ["A9"], "copie_disponibili": 4 },
  { "_id": "L10", "titolo": "Il processo", "descrizione": "Surrealismo giudiziario", "anno_pubblicazione": 1925, "categoria": { "nome": "Classico", "descrizione": "Opere della letteratura considerate fondamentali" }, "autori": ["A10"], "copie_disponibili": 1 }
]

utenti = [
  { "_id": "U1", "nome": "Mario", "cognome": "Rossi", "email": "mario.rossi@example.com", "data_iscrizione": "2024-01-01" },
  { "_id": "U2", "nome": "Laura", "cognome": "Bianchi", "email": "laura.bianchi@example.com", "data_iscrizione": "2024-02-15" },
  { "_id": "U3", "nome": "Giulia", "cognome": "Verdi", "email": "giulia.verdi@example.com", "data_iscrizione": "2023-12-10" },
  { "_id": "U4", "nome": "Luca", "cognome": "Ferrari", "email": "luca.ferrari@example.com", "data_iscrizione": "2024-03-05" },
  { "_id": "U5", "nome": "Alessandro", "cognome": "Russo", "email": "ale.russo@example.com", "data_iscrizione": "2024-04-01" },
  { "_id": "U6", "nome": "Federica", "cognome": "Romano", "email": "federica.romano@example.com", "data_iscrizione": "2024-01-25" },
  { "_id": "U7", "nome": "Matteo", "cognome": "Conti", "email": "matteo.conti@example.com", "data_iscrizione": "2024-02-12" },
  { "_id": "U8", "nome": "Chiara", "cognome": "Costa", "email": "chiara.costa@example.com", "data_iscrizione": "2024-05-09" },
  { "_id": "U9", "nome": "Davide", "cognome": "Marino", "email": "davide.marino@example.com", "data_iscrizione": "2024-06-01" },
  { "_id": "U10", "nome": "Silvia", "cognome": "Martini", "email": "silvia.martini@example.com", "data_iscrizione": "2024-06-20" }
]

prestiti = [
  { "_id": "P1", "user_id": "U1", "book_id": "L1", "data_prestito": "2025-06-10", "data_restituzione": None, "stato": "attivo" },
  { "_id": "P2", "user_id": "U2", "book_id": "L3", "data_prestito": "2025-06-05", "data_restituzione": "2025-06-15", "stato": "restituito" },
  { "_id": "P3", "user_id": "U3", "book_id": "L5", "data_prestito": "2025-06-11", "data_restituzione": None, "stato": "attivo" },
  { "_id": "P4", "user_id": "U4", "book_id": "L2", "data_prestito": "2025-06-01", "data_restituzione": "2025-06-20", "stato": "restituito" },
  { "_id": "P5", "user_id": "U5", "book_id": "L4", "data_prestito": "2025-06-03", "data_restituzione": None, "stato": "attivo" },
  { "_id": "P6", "user_id": "U6", "book_id": "L6", "data_prestito": "2025-06-09", "data_restituzione": "2025-06-18", "stato": "restituito" },
  { "_id": "P7", "user_id": "U7", "book_id": "L7", "data_prestito": "2025-06-15", "data_restituzione": None, "stato": "attivo" },
  { "_id": "P8", "user_id": "U8", "book_id": "L8", "data_prestito": "2025-06-07", "data_restituzione": "2025-06-17", "stato": "restituito" },
  { "_id": "P9", "user_id": "U9", "book_id": "L9", "data_prestito": "2025-06-16", "data_restituzione": None, "stato": "attivo" },
  { "_id": "P10", "user_id": "U10", "book_id": "L10", "data_prestito": "2025-06-18", "data_restituzione": None, "stato": "attivo" }
]

# Salvataggio su file
files = {
    "autori.json": autori,
    "libri.json": libri,
    "utenti.json": utenti,
    "prestiti.json": prestiti
}

for filename, data in files.items():
    with open(output_dir / filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

output_dir.as_posix()

