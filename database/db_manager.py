import sqlite3

class DbManager:

    #Costruttore
    #Nel costruttore viene effettuata la connessione al database e viene chimata la funzione per creare le tabelle delle entita'
    def __init__(self,nome_db="openforce.db"):
        self.conn = sqlite3.connect(nome_db)
        self.creaTabelle()

    #Query per la creazione delle tabelle delle entita'
    def creaTabelle(self):
        with self.conn:
            #Tabella autore
            self.conn.execute("CREATE TABLE IF NOT EXISTS autore(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL, data_nascita TEXT NOT NULL, email TEXT)")

            #Tabella libro
            self.conn.execute("CREATE TABLE IF NOT EXISTS libro(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,titolo TEXT NOT NULL, nome_autore TEXT NOT NULL, numero_pagine INTEGER NOT NULL, prezzo REAL NOT NULL, casa_editrice TEXT, autore_id INTEGER NOT NULL, FOREIGN KEY(autore_id) REFERENCES autore(id))")

            self.conn.commit()


    #INSERIMENTO
    #Query di inserimento autore
    def inserisciAutore(self,nome,data_nascita,email):
        with self.conn:
            self.conn.execute("INSERT INTO autore (nome,data_nascita,email) VALUES (?,?,?)",(nome,data_nascita,email))
            self.conn.commit()

    #Query di inserimento libro
    def inserisciLibro(self,titolo,nome_autore,numero_pagine,prezzo,casa_editrice,autore_id):
        with self.conn:
            self.conn.execute("INSERT INTO libro (titolo,nome_autore,numero_pagine,prezzo,casa_editrice,autore_id) VALUES (?,?,?,?,?,?)",(titolo,nome_autore,numero_pagine,prezzo,casa_editrice,autore_id))
            self.conn.commit()

    #VISUALIZZAZIONE
    def visualizzaAutore(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM autore")
            return cur.fetchall()

    def visualizzaLibro(self):
            with self.conn:
                cur = self.conn.cursor()
                cur.execute("SELECT * FROM libro")
                return cur.fetchall()

    #RICERCA
    #Query per cercare un determinato autore dal nome
    def cercaAutorePerNome(self,nome):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM autore WHERE nome = ?",(nome,))
            return cur.fetchone()

    #Query per cercare un determinato libro dal titolo e dal nome dell'autore
    def cercaLibroTitoloAutore(self,titolo,nome_autore):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM libro WHERE titolo = ? AND nome_autore = ?",(titolo,nome_autore,))
            return cur.fetchone()


    #MODIFICA
    #Query per la modifica di un autore
    def aggiornaAutore(self,nome_autore,data_nascita,email,autore_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("""
                UPDATE Autore
                SET nome = ?, data_nascita = ?, email = ?
                WHERE id = ?
                """, (nome_autore, data_nascita, email, autore_id))

    #Query per la modifica di un libro
    def aggiornaLibro(self,titolo,nome_autore,numero_pagine,prezzo,casa_editrice,id):
        with self.conn:
            cur = self.conn.cursor();
            cur.execute("""
               UPDATE Libro
               SET titolo = ?,nome_autore = ?,numero_pagine = ?, prezzo = ?, casa_editrice = ?
               WHERE id = ?""", (titolo,nome_autore,numero_pagine,prezzo,casa_editrice,id))
