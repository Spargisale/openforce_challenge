from database.db_manager import DbManager
from validazione import validazione
from datetime import datetime
import csv
import time
import re

#INSERIMENTO
def inserisciAutore(db):
    print(chr(27) + "[2J")

    #L'utente inserisce il nome dell'autore che viene validato, poi cerca se l'autore è presente nel database:
    #se è già presente, l'utente dovrà inserire di nuovo un nuovo nome.
    while True:
        nome = validazione.chiediInputUtente("Nome e cognome dell'autore: ",validazione.validaNome, "Il nome dell'autore inserito non è valido!")
        nome = re.sub(r'[^\w\s]', '', nome) #Rimuovo i caratteri speciali dalla stringa
        if db.cercaAutorePerNome(nome):
            print("L'autore è già presente nel database e non può essere inserito di nuovo!")
        else:
            break

    #La funzione prosegue chiedendo all'utente le altre informazioni relative all'utente che vengono validate
    data_nascita = validazione.chiediInputUtente("Data di nascita (gg-m-aaaa): ",validazione.validaData,"La data inserita non è valida!")
    email = validazione.chiediInputUtente("Email dell'autore: ", validazione.validaEmail,"L'email inserita non è valida!")

    #A questo punto viene creato un nuovo record tramite query al database
    db.inserisciAutore(nome,data_nascita,email)
    print(chr(27) + "[2J")
    print("Autore aggiunto correttamente al database!")
    input("Premi invio per continuare.")


def inserisciLibro(db):
    print(chr(27) + "[2J")
    #L'utente inserisce il nome e titolo del libro che vengono validati, poi cerca se il libro è presente nel database:
    #se è già presente, l'utente dovrà inserire nuovi dati.
    while True:
        titolo = validazione.chiediInputUtente("Titolo del libro: ",validazione.validaTitolo,"Il titolo inserito non è valido!")
        nome_autore = validazione.chiediInputUtente("Autore: ",validazione.validaNome,"Il nome inserito non è valido!")
        titolo = re.sub(r'[^\w\s]', '', titolo)
        nome_autore = re.sub(r'[^\w\s]', '', nome_autore)

        if db.cercaLibroTitoloAutore(titolo,nome_autore):
            print("Il libro è già presente nel database e non può essere inserito di nuovo!")
            input("Premi invio per inserire di nuovo i dati")
        else:
            break

    #A questo punto l'utente inserisce le informazioni aggiuntive del libro che vengono validate
    numero_pagine = validazione.chiediInputUtente("Numero delle pagine: ",validazione.validaInt,"Il numero delle pagine non è valido!")
    prezzo = validazione.chiediInputUtente("Prezzo (i decimali vanno inseriti con il punto e.g. 12.50): ",validazione.validaFloat,"Il prezzo inserito non è valido!")
    casa_editrice = validazione.chiediInputUtente("Casa editrice: ", validazione.validaTitolo,"La casa editrice inserita non è valida!")

    #Tramite il nome del autore appena inserito, viene effettuata una ricerca nel database per reperire (se presente) il suo id
    #e associarlo al libro appena creato.
    #TODO: funzione di inserimento nel caso l'autore non esista
    autore_id = db.cercaAutorePerNome(nome_autore)
    if autore_id:
        autore_id = autore_id[0]
        db.inserisciLibro(titolo,nome_autore,numero_pagine,prezzo,casa_editrice,autore_id)
        print(chr(27) + "[2J")
        print("Libro aggiunto correttamente al database!")
        input("Premi invio per continuare.")
    else:
        print("L'autore del libro non è stato trovato, inserisci prima le informazioni relative all'autore!")
        input("Premi invio per continuare.")




#MODIFICA
def modificaAutore(db):
    print(chr(27) + "[2J")

    #L'utente inserisce il nome dell'autore da modificare che viene validato, poi cerca se l'autore è presente nel database:
    #se non è presente, l'utente dovrà inserire di nuovo un nuovo nome.
    while True:
        nome = validazione.chiediInputUtente("Nome dell'autore da modificare: ",validazione.validaNome,"Il nome inserito non è valido")
        nome = re.sub(r'[^\w\s]', '', nome)
        autore = db.cercaAutorePerNome(nome)
        if not autore:
            print("L'autore non e' presente nel database!")
            input("Premi invio per inserire un nuovo nome.")
        else:
            break

    #L'autore è stato trovato: visualizzo le informazioni sull'autore trovato e chiedo all' utente di inserire nuovi dati per la modifica del record
    print(chr(27) + "[2J")
    print("Autore trovato!")
    print(db.visualizzaAutore(nome))
    print("Inserisci i nuovi dati dell'autore: ")

    nome = validazione.chiediInputUtente("Nome: ",validazione.validaNome,"Il nome inserito non è valido!")
    nome = re.sub(r'[^\w\s]', '', nome)
    data_nascita = validazione.chiediInputUtente("Data di nascita (gg-m-aaaa): ",validazione.validaData,"La data inserita non è valida!")
    email = validazione.chiediInputUtente("Email: ", validazione.validaEmail, "L'email inserita non è valida!")

    #Se tutti i dati inseriti sono corretti, la funzione procede con la modifica dell'autore scelto tramite query di modifica,
    #notifica l'utente e torna al menu principale
    #Il campo "autore[0]" corrisponde all'id dell'autore trovato, necessario per modificare i dati di quello specifico record
    db.aggiornaAutore(nome,data_nascita,email,autore[0])

    #Essendo il nome dell'autore presente anche nella tabella dei libri, se quest'ultimo viene modificato,
    #è necessario aggiornare anche la colonna con il nuovo nome dell'autore nei record dei libri ad esso associati
    db.aggiornaLibroConNuovoAutore(autore[0])
    print("Autore modificato correttamente")
    input("Premi invio per continuare.")



def modificaLibro(db):
    print(chr(27) + "[2J")
    while True:
        #Faccio cercare all'utente il libro da modificare tramite titolo e nome dell'autore;
        #se il libro non viene trovato, l'utente dovrà inserire di nuovo i dati, altrimenti la funzione procede con l'inserimento dei nuovi attributi
        titolo = validazione.chiediInputUtente("Inserisci il titolo del libro da modificare: ",validazione.validaTitolo,"Il titolo inserito non è valido!")
        titolo = re.sub(r'[^\w\s]', '', titolo)
        nome_autore = validazione.chiediInputUtente("Inserisci l'autore del libro: ",validazione.validaNome,"Il nome inserito non è valido!")
        nome_autore = re.sub(r'[^\w\s]', '', nome_autore)
        libro = db.cercaLibroTitoloAutore(titolo,nome_autore)
        if not libro:
            print("Il libro non è presente nel database!")
            input("Premi invio per continuare.")
        else:
            break

    #Il libro è stato trovato: visualizzo le informazioni del libro e chiedo all' utente di inserire i nuovi dati per la modifica
    print(chr(27) + "[2J")
    print("Libro trovato!")
    print(db.visualizzaLibro(titolo,nome_autore))
    print("Inserisci i nuovi dati del libro: ")

    titolo = validazione.chiediInputUtente("Titolo: ",validazione.validaTitolo,"Il titolo inserito non è valido!")
    titolo = re.sub(r'[^\w\s]', '', titolo)
    nome_autore = validazione.chiediInputUtente("Autore: ",validazione.validaNome,"Il nome inserito non è valido!")
    nome_autore = re.sub(r'[^\w\s]', '', nome_autore)
    numero_pagine = validazione.chiediInputUtente("Numero pagine: ",validazione.validaInt,"Il valore inserito non è valido!")
    prezzo = validazione.chiediInputUtente("Prezzo (i decimali vanno inseriti con il punto e.g. 12.50): ",validazione.validaFloat,"Il valore inserito non è valido!")
    casa_editrice = validazione.chiediInputUtente("Casa editrice: ",validazione.validaTitolo,"Il nome inserito non è valido!")

    #Se i nuovi dati inseriti sono corretti, procedo con la modifica del record nel database
    #Il valore "libro[0]" corrisponde all'id del libro ricercato, necessario per modificare quello specifico libro
    db.aggiornaLibro(titolo,nome_autore,numero_pagine,prezzo,casa_editrice,libro[0])
    print("Libro modificato correttamente")
    input("Premi invio per continuare.")


#ELIMINAZIONE
def eliminaLibro(db):
    print(chr(27) + "[2J")
    while True:
        #Faccio cercare all'utente il libro da eliminare tramite titolo e nome dell'autore;
        #se il libro non viene trovato, l'utente dovrà inserire di nuovo i dati
        titolo = validazione.chiediInputUtente("Inserisci il titolo del libro da eliminare: ",validazione.validaTitolo,"Il titolo inserito non è valido!")
        titolo = re.sub(r'[^\w\s]', '', titolo)
        nome_autore = validazione.chiediInputUtente("Inserisci l'autore del libro: ",validazione.validaNome,"Il nome inserito non è valido!")
        nome_autore = re.sub(r'[^\w\s]', '', nome_autore)

        libro = db.cercaLibroTitoloAutore(titolo,nome_autore)
        if not libro:
            print("Il libro non è presente nel database!")
            input("Premi invio per continuare.")
        else:
            break

    #Il libro è stato trovato: visualizzo le informazioni del libro
    print("Libro trovato!")
    print(db.visualizzaLibro(titolo,nome_autore))

    #Chiedo conferma all'utente sull'effettiva eliminazione del record
    while True:
        opz = input("Vuoi eliminare questo libro? (s|n) ").lower()
        if opz == 's':
            db.eliminaLibro(titolo,nome_autore)
            print("Libro eliminato correttamente.")
            input("Premi invio per continuare.")
            break
        else:
            print("Eliminazione annullata.")
            input("Premi invio per continuare.")
            break



def eliminaAutore(db):
    print(chr(27) + "[2J")
    #Faccio cercare all'utente l'autore da eliminare tramite il nome;
    #se l'autore non viene trovato, l'utente dovrà inserire di nuovo i dati
    while True:
        nome = validazione.chiediInputUtente("Nome dell'autore da modificare: ",validazione.validaNome,"Il nome inserito non è valido")
        nome = re.sub(r'[^\w\s]', '', nome)

        autore = db.cercaAutorePerNome(nome)
        if not autore:
            print("L'autore non e' presente nel database!")
            input("Premi invio per inserire un nuovo nome.")
        else:
            break

    #L'autore è stato trovato, ne visualizzo i dati
    print(chr(27) + "[2J")
    print("Autore trovato!")
    print(db.visualizzaAutore(nome))

    #Se ci sono dei libri associati all'autore, l'eliminazione viene gestita tramite clausola "ON DELETE RESTRICT",
    #di conseguenza non sarà possibile eliminare quell'autore finchè non verranno eliminati tutti i libri associati.
    if db.cercaLibriPerAutore(autore[0]):
        print("ATTENZIONE!")
        print("Ci sono dei libri associati a questo autore attualmente e non è possibile eliminarlo!")
        print(db.visualizzaLibriPerAutore(autore[0]))
        print("Se vuoi eliminare l'autore devi prima eliminare i libri associati!")
        input("Premi invio per continuare.")
    else:
        while True:
            opz = input("Vuoi eliminare questo autore? (s|n) ").lower()
            if opz == 's':
                db.eliminaAutore(nome)
                print("Autore eliminato correttamente!")
                input("Premi invio per continuare.")
                break
            else:
                print("Eliminazione annullata.")
                input("Premi invio per continuare.")
                break



#FILE CSV
def importaAutori(db,file):
    #Apro e leggo il file CSV degli autori
    with open(file, newline='',encoding='utf-8') as file_csv:
        reader = csv.DictReader(file_csv)

        for row in reader:
            print("Aggiungendo " + row['nome'])
            #Se l'autore è gia' presente nel database, non lo aggiungo
            if db.cercaAutorePerNome(row['nome']):
                print("Autore già presente!")
                print("")
                time.sleep(0.2)
            else:
                db.inserisciAutore(row['nome'],row['data_nascita'],row['email'])
                print("Autore inserito!")
                print("")
                time.sleep(0.2)
        print("Dati degli autori importati con successo.")
        input("Premi invio per continuare")


def importaLibri(db,file):
    #Apro e leggo il file CSV dei libri
    with open(file, newline='',encoding='utf-8') as file_csv:
        reader = csv.DictReader(file_csv)

        for row in reader:
            print("Aggiungendo " + row['titolo'])
            #Se il libro è già presente nel database, non lo aggiungo
            if db.cercaLibroTitoloAutore(row['titolo'],row['nome_autore']):
                print("Libro già presente!")
                print("")
                time.sleep(0.2)
            else:
                #Se il libro non è già presente, verifico se l'autore si trova nel database in modo da associarlo al libro
                autore = db.cercaAutorePerNome(row['nome_autore'])
                #Se l'autore è presente, associo il libro con il suo identificativo, altrimenti non inserisco il libro.
                #TODO: inserire anche dati relativi all'autore nel momento dell'inserimento del libro
                if autore:
                    db.inserisciLibro(row['titolo'],row['nome_autore'],row['numero_pagine'],row['prezzo'],row['casa_editrice'],autore[0])
                    print("Libro inserito!")
                    print("")
                    time.sleep(0.2)
                else:
                    print("Impossibile associare questo libro, l'autore non esiste nel database.")
        print("Dati dei libri importati con successo.")
        input("Premi invio per continuare")
