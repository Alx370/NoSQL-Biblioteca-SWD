# NoSQL-Biblioteca-SWD
database biblioteca

Richiesta l'Utente vuole creare un applicazione per una Libreria che il DB abbia le feature MongoDB:
Feature utili per la Biblioteca : 
- **Flexible schema(document-oriented)**  
    Puoi gestire libri, utenti, prestiti, categorie anche se hanno strutture leggermente diverse.
- **Query avanzate (`find`, `aggregate`)**  
    Per cercare libri, contare prestiti e ottenere “i più letti”
- **Indici personalizzabili**  
    Indici su `titolo`, `autore`, `categorie`, `prestiti.data_inizio`
    query rapide anche su database grandi.
- **Full-text search**  
    Ricerca su titoli, autori, categorie.  
    → esempio: `db.libri.createIndex({ descrizione: "text" })`
- **Referencing ed embedding**  
	Per gestire :
    - utenti ↔ prestiti
    - libri ↔ autori
    - libri ↔ categorie
- **Shard & replica (scalabilità)**  
    per scalare facilmente orizzontalmente o garantire alta disponibilità.

# Creazione database NoSQL per una biblioteca
1. Setup dell’ambiente per lavorare con un database NoSQL abbiamo scelto MongoDB, un database documentale che salva i dati in formato JSON-like (BSON).
2. Registrarsi su MongoDB Atlas, Creare un cluster gratuito , Creare un database chiamato biblioteca, Usare le credenziali per connettersi da applicazioni esterne (es. app web)

**Struttura sulle Collezioni** :
- **libri**
- **autori**
- **categorie**
- **utenti**
- **prestiti**

Relazioni :

LIBRI (1:N) ← PRESTITI
LIBRI (N:N) → AUTORI  
LIBRI (N:1) → CATEGORIE  
LIBRI (1:N) → UTENTI  

-- Libro 
Libro → Autori (many-to-many)→ Referencing ho scelto questo per queste ragioni:
- Un autore può scrivere **molti libri**.
- Un libro può avere **più autori**.
- Immagino che la categoria è solo una stringa, e può essere embeddato direttamente nel documento libro.
- Evitare la duplicazione se uso embedding, pechè senno ogni volta che un autore scrive un nuovo libro, devo duplicare i suoi dati in più punti.
- Gli autori possono avere biografie, premi quindi documenti pesanti.
- Referencing ti consente di **modificare un autore una sola volta** e visto perché i prestiti crescono nel tempo e ogni libro può essere prestato centinaia di volte embeddarli renderebbe il documento troppo grande e ingestibile, meglio salvare i prestiti in una collezione separata.

-- Utente
utente → prestiti (one-to-many): referencing  ho scelto questo per ragioni:
- Ogni utente può avere **molti prestiti**, e questi possono contenere:
    - data prestito, restituzione, stato
    - riferimenti al libro
- Embedding porterebbe a un documento utente troppo grande.
- Inoltre i prestiti vanno analizzati anche **indipendentemente** (es. report mensili)

-- Prestito
prestito → libro / utente (many-to-one): referencing ho scelto questo per ragioni:
- Il prestito si riferisce a un solo libro e un solo utente → semplice relazione many-to-one.
- I dati del libro o utente **possono cambiare**, ma il prestito vuole **fotografare il riferimento originale**.
- Non ha senso embeddare tutto il libro/utente ogni volta troppa duplicazione.

# Script 
Lo script usa una libreria chiamata pymongo per connettersi a MongoDB.
Serve indicare l’indirizzo del server (es. mongodb://localhost:27017) e il nome del database.
All’interno dello script ci sono liste di dati per ogni collezione:
- autori
- libri
- utenti
- prestiti
Per ogni lista, lo script crea la collezione corrispondente (se non esiste già) e inserisce i documenti con i dati.

Perché usare questo script?
- Evita di inserire manualmente i dati uno a uno
- Serve a popolare velocemente il database con dati di prova
- Puoi modificarlo per aggiungere altri dati o cambiare i campi

Cosa ti serve per usarlo?
- Avere MongoDB installato e in esecuzione
- Installare la libreria Python pymongo (comando: pip install pymongo)
- Avere Python installato sul computer

Come utilizzarlo :
- Apri il terminale o prompt dei comandi, vai nella cartella dove hai salvato il file, esempio: cd C:\Users\TUO_NOME_UTENTE\Desktop
- Poi esegui: python script.py


# Script per importare i dati su MongoDB
Assicurati che MongoDB sia in esecuzione, poi apri il terminale o prompt dei comandi e usa:

```bash
mongoimport --db biblioteca --collection autori --file "$HOME/Desktop/json_biblioteca/autori.json" --jsonArray
mongoimport --db biblioteca --collection libri --file "$HOME/Desktop/json_biblioteca/libri.json" --jsonArray
mongoimport --db biblioteca --collection utenti --file "$HOME/Desktop/json_biblioteca/utenti.json" --jsonArray
mongoimport --db biblioteca --collection prestiti --file "$HOME/Desktop/json_biblioteca/prestiti.json" --jsonArray
```
su Windows : 
```cmd
mongoimport --db biblioteca --collection autori --file "%USERPROFILE%\Desktop\json_biblioteca\autori.json" --jsonArray
mongoimport --db biblioteca --collection libri --file "%USERPROFILE%\Desktop\json_biblioteca\libri.json" --jsonArray
mongoimport --db biblioteca --collection utenti --file "%USERPROFILE%\Desktop\json_biblioteca\utenti.json" --jsonArray
mongoimport --db biblioteca --collection prestiti --file "%USERPROFILE%\Desktop\json_biblioteca\prestiti.json" --jsonArray
```