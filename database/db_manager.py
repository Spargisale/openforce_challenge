import sqlite3
from prettytable import from_db_cursor

class DbManager:

    #Costruttore
    #Nel costruttore viene effettuata la connessione al database e viene chiamata la funzione per creare le tabelle delle entita'
    def __init__(self,nome_db="openforce.db"):
        self.conn = sqlite3.connect(nome_db)
        #Gestione delle chiavi esterne da parte di sqlite
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.creaTabelle()

    #Query per la creazione delle tabelle delle entita'
    def creaTabelle(self):
        with self.conn:
            #Tabella autore
            self.conn.execute("CREATE TABLE IF NOT EXISTS autore(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL, data_nascita TEXT NOT NULL, email TEXT)")

            #Tabella libro
            self.conn.execute("CREATE TABLE IF NOT EXISTS libro(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,titolo TEXT NOT NULL, nome_autore TEXT NOT NULL, numero_pagine INTEGER NOT NULL, prezzo REAL NOT NULL, casa_editrice TEXT, autore_id INTEGER NOT NULL, FOREIGN KEY(autore_id) REFERENCES autore(id) ON DELETE RESTRICT)")

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
    #Visualizzazione delle tabelle a schermo tramite la libreria PrettyTable
    def visualizzaAutori(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, nome, data_nascita, email FROM autore")
            autori = from_db_cursor(cur)
            return autori

    def visualizzaLibri(self):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT id, titolo, nome_autore, numero_pagine, prezzo, casa_editrice, autore_id FROM libro")
            libri = from_db_cursor(cur)
            return libri

    #Visualizzazione del singolo record tramite PrettyTable
    def visualizzaAutore(self,nome):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM autore WHERE nome = ?",(nome,))
            autore = from_db_cursor(cur)
            return autore

    def visualizzaLibro(self, titolo, nome_autore):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM libro WHERE titolo = ? AND nome_autore = ?",(titolo,nome_autore,))
            libro = from_db_cursor(cur)
            return libro

    #Visualizzazione a schermo di tutti i libri associati ad un autore tramite PrettyTable
    def visualizzaLibriPerAutore(self, autore_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("""
                SELECT * FROM libro
                WHERE autore_id = ?""", (autore_id,))
            libri_associati = from_db_cursor(cur)
            return libri_associati

    #RICERCA
    #Cerca e restituisce l'autore
    def cercaAutorePerNome(self,nome):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM autore WHERE nome = ?",(nome,))
            return cur.fetchone()

    #Cerca e restituisce il libro
    def cercaLibroTitoloAutore(self,titolo,nome_autore):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("SELECT * FROM libro WHERE titolo = ? AND nome_autore = ?",(titolo,nome_autore,))
            return cur.fetchone()

    #Cerca e restituisce tutti i libri associati ad un determinato autore
    def cercaLibriPerAutore(self,autore_id):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("""
                SELECT * FROM libro
                WHERE autore_id = ?""", (autore_id,))
            return cur.fetchall()


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
            self.conn.commit()

    #Query per la modifica di un libro
    def aggiornaLibro(self,titolo,nome_autore,numero_pagine,prezzo,casa_editrice,id):
        with self.conn:
            cur = self.conn.cursor();
            cur.execute("""
               UPDATE Libro
               SET titolo = ?,nome_autore = ?,numero_pagine = ?, prezzo = ?, casa_editrice = ?
               WHERE id = ?""", (titolo,nome_autore,numero_pagine,prezzo,casa_editrice,id))
            self.conn.commit()


    #ELIMINAZIONE
    def eliminaLibro(self,titolo,nome_autore):
        with self.conn:
            cur = self.conn.cursor();
            cur.execute("""
                DELETE FROM libro
                WHERE titolo = ? AND nome_autore = ?""", (titolo,nome_autore))
            self.conn.commit()

    def eliminaAutore(self,nome):
        with self.conn:
            cur = self.conn.cursor()
            cur.execute("""
                DELETE FROM autore
                WHERE nome = ?""", (nome,))
            self.conn.commit()
