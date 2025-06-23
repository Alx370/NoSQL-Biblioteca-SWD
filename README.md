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

**Struttura sulle Collezioni** :
- **libri**
- **autori**
- **categorie**
- **utenti**
- **prestiti**

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
