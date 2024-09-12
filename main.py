import sqlite3

#Creo la connessione al database sqlite
con = sqlite3.connect("openforce.db")
cur = con.cursor()

#Creazione delle tabelle nel database
def creaTabellaLibri():
    cur.execute("CREATE TABLE IF NOT EXISTS libro(id INTEGER NOT NULL PRIMARY KEY,titolo TEXT, nome_autore TEXT, numero_pagine INTEGER, prezzo REAL, casa_editrice TEXT, codice_autore INTEGER)")
    con.commit()

def creaTabellaAutori():
    cur.execute("CREATE TABLE IF NOT EXISTS autore(id INTEGER NOT NULL PRIMARY KEY,nome TEXT, data_nascita TEXT, email TEXT)")
    con.commit()



#Visualizzo le tabelle tramite query
def visualizzaTabellaLibri():
    cur.execute("SELECT * FROM libro")
    print(cur.fetchall())


def visualizzaTabellaAutori():
    cur.execute("SELECT * FROM autore")
    print(cur.fetchall())


cur.execute("""INSERT INTO autore VALUES (
    '11023','George Orwell','25-06-1903','georgeorwell@openforce.it')
    """)

con.commit()

creaTabellaLibri()
creaTabellaAutori()
visualizzaTabellaAutori()
