import sqlite3

class DbManager:

    #Costruttore
    #Nel costruttore viene effettuata la connessione al database e viene chimata la funzione per creare le tabelle delle entita'
    def __init__(self,nome_db="openforce.db"):
        self.conn = sqlite3.connect(nome_db)
        self.creaTabelle()

    #Vengono effettuate delle query per la creazione delle tabelle delle entita'
    def creaTabelle(self):
        with self.conn:
            #Tabella autore
            self.conn.execute("CREATE TABLE IF NOT EXISTS autore(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome TEXT NOT NULL, data_nascita TEXT NOT NULL, email TEXT)")

            #Tabella libro
            self.conn.execute("CREATE TABLE IF NOT EXISTS libro(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,titolo TEXT NOT NULL, nome_autore TEXT NOT NULL, numero_pagine INTEGER NOT NULL, prezzo REAL NOT NULL, casa_editrice TEXT, autore_id INTEGER NOT NULL, FOREIGN KEY(autore_id) REFERENCES autore(id))")

            self.conn.commit()
