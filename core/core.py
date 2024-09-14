from database.db_manager import DbManager
from validazione import validazione
from datetime import datetime


#INSERIMENTO
def inserisciAutore(db):
    #Questo ciclo serve per far reinserire i dati all'utente nel caso l'autore sia già presente nel database
    while True:
        #Nel caso in cui il nome dell'autore sia vuoto, l'utente dovrà inserire di nuovo il dato
        while True:
            nome = input("Nome e cognome: ").lower()
            if nome == '':
                print("Il nome non è valido")
            else:
                break

        #Validazione della data; se la data non e' del giusto formato o è vuota, l'utente dovrà reinserirla
        while True:
            data_nascita = input("Data nascita (gg-mm-aaaa): ")
            if not validazione.validaData(data_nascita) or data_nascita == '':
                print("La data inserita non e' valida!")
            else:
                break

        #Validazione dell'email
        while True:
            email = input("Email: ")
            if not validazione.validaEmail(email) or email == '':
                print("L'email non è valida!")
            else:
                break

        #Se l'autore è già presente nel database, l'utente dovrà reinserire i dati
        if db.cercaAutorePerNome(nome):
            print("L'autore e' gia' presente nel database!")
            input("Premi un tasto per inserire di nuovo i dati. ")
        else:
            break
    #Nel caso in cui i dati siano corretti e l'autore non è già presente nel database, procedo con l'inserimento del nuovo record
    db.inserisciAutore(nome,data_nascita,email)
    print(chr(27) + "[2J")
    print("Autore aggiunto correttamente al database!")
    input("Premi un tasto per continuare.")


def inserisciLibro(db):
    while True:
        #Validazione titolo
        while True:
            titolo = input("Titolo: ").lower()
            if titolo == '':
                print("Il titolo non è valido")
            else:
                break

        #Validazione nome autore
        while True:
            nome_autore = input("Autore: ").lower()
            if nome_autore == '':
                print("L'autore non è valido")
            else:
                break

        #Validazione del numero di pagine e del prezzo;
        #Questi due valori devono essere rispettivamente intero e float, nel caso in cui siano diversi, l'utente dovrà reinserire i dati
        while True:
            numero_pagine = input("Numero delle pagine: ")
            if not validazione.validaInt(numero_pagine) or numero_pagine == '':
                print("Il numero delle pagine non e' valido!")
            else:
                break

        while True:
            prezzo = input("Prezzo (utilizza il punto per i valori decimali): ")
            if not validazione.validaFloat(prezzo) or prezzo == '' :
                print("Il prezzo non e' valido!")
            else:
                break

        #Validazione della casa editrice
        while True:
            casa_editrice = input("Casa editrice: ").lower()
            if casa_editrice == '':
                print("La casa editrice non è valida!")
            else:
                break

        #Nel caso in cui il libro sia già presente nel database, l'utente dovrà reinserire i dati
        if db.cercaLibroTitoloAutore(titolo,nome_autore):
            print("Il libro è già presente nel database")
            input("Premi un tasto per inserire di nuovo i dati.")

        #Se i dati sono corretti, cerco il nome dell'autore inserito dall'utente all'interno della tabella degli autori;
        #se trovo riscontro, il campo della chiave esterna del libro corrisponderà alla chiave primaria dell'autore trovato;
        #se non trovo l'autore, lascio il campo vuoto.
        else:
            autore_id = db.cercaAutorePerNome(nome_autore)
            if autore_id:
                autore_id = autore_id[0]
                break
            else:
                autore_id = ''
                #while True:
                #    autore_id = input("Id autore: ")
                #    if autore_id == '':
                    #        print("L'id dell'autore non è valido!")
                #    else:
                    #        break

    #Una volta memorizzati tutti i dati inseriti dall'utente, procedo con l'inserimento del nuovo libro all'interno del database
    db.inserisciLibro(titolo,nome_autore,numero_pagine,prezzo,casa_editrice,autore_id)
    print(chr(27) + "[2J")
    print("Libro aggiunto correttamente al database!")
    input("Premi un tasto per continuare.")



#MODIFICA
def modificaAutore(db):
    #Faccio cercare all'utente l'autore da modificare;
    #se l'autore non viene trovato, l'utente dovrà inserire un nuovo nome, altrimenti si va avanti con l'inserimento dei nuovi dati
    while True:
        nome_autore = input("Inserisci il nome dell'autore da modificare: ").lower()
        autore = db.cercaAutorePerNome(nome_autore)
        if not autore:
            print("L'autore non e' presente nel database!")
            input("Premi un tasto per continuare.")
        else:
            break

    #L'autore è stato trovato: visualizzo le informazioni sull'autore trovato e chiedo all' utente di inserire i nuovi dati per la modifica
    print("Autore trovato!")
    print("Dati relativi a " + str(nome_autore) +": ")
    print("Id: " + str(autore[0]) + "| Nome: " + str(autore[1]) + "| Data di nascita: " + str(autore[2]) + "| Email: " +str(autore[3]))
    print("Inserisci i nuovi dati")

    #Validazione del nome
    while True:
        nome = input("Nome e cognome: ")
        if nome == '':
             print("Il nome non puo' essere vuoto!")
        else:
            break

    #Validazione della data
    while True:
        data_nascita = input("Data nascita (gg-mm-aaaa): ")
        if not validazione.validaData(data_nascita) or data_nascita == '':
            print("La data inserita non e' valida!")
        else:
            break

    #Validazione dell'email
    while True:
        email = input("Email: ")
        if not validazione.validaEmail(email) or email == '':
            print("L'indirizzo email non e' corretto!")
        else:
            break

    #Se tutti i dati inseriti sono corretti, procedo con la modifica dell'autore scelto, notifico l'utente e torno al menu principale
    #Il campo "autore[0]" corrisponde all'id dell'autore trovato, necessario per modificare i dati di quello specifico record
    db.aggiornaAutore(nome,data_nascita,email,autore[0])
    print("Autore modificato correttamente")
    input("Premi un tasto per continuare.")



def modificaLibro(db):
    while True:
        #Faccio cercare all'utente il libro da modificare tramite titolo e nome dell'autore;
        #se il libro non viene trovato, l'utente dovrà inserire di nuovo i dati, altrimenti la funzione procede con l'inserimento dei nuovi attributi
        titolo = input("Inserisci il nome del libro da modificare: ")
        autore = input("Inserisci il nome dell'autore del libro: ")
        libro = db.cercaLibroTitoloAutore(titolo,autore)
        if not autore and not libro:
            print("Il libro non è presente nel database!")
            input("Premi un tasto per continuare.")
        else:
            break

    #Il libro è stato trovato: visualizzo le informazioni del libro e chiedo all' utente di inserire i nuovi dati per la modifica
    print("Libro trovato!")
    print("Dati relativi a " + str(titolo) +": ")
    print("Id: " + str(libro[0]) + "| Titolo: " + str(libro[1]) + "| Autore: " + str(libro[2]) + "| Numero pagine: " +str(libro[3]) + "| Prezzo: " +str(libro[4]) + "| Casa editrice: " +str(libro[5]) + "| Id autore: " +str(libro[6]))
    print("Inserisci i nuovi dati")

    #Validazione titolo
    while True:
        titolo = input("Titolo: ")
        if titolo == '':
             print("Il titolo non puo' essere vuoto!")
        else:
            break

    #Validazione nome dell'autore
    while True:
        autore = input("Autore: ")
        if autore == '':
            print("Il nome dell'autore non può essere vuoto!")
        else:
            break

    #Validazione del numero delle pagine
    while True:
        numero_pagine = input("Numero pagine: ")
        if not validazione.validaInt(numero_pagine) or numero_pagine == '':
            print("L'indirizzo email non e' corretto!")
        else:
            break

    #Validazione del prezzo
    while True:
        prezzo = input("Prezzo: ")
        if not validazione.validaFloat(prezzo) or prezzo == '':
            print("Il prezzo non e' valido!")
        else:
            break

    #Validazione della casa editrice
    while True:
        casa_editrice = input("Casa editrice: ")
        if casa_editrice == '':
            print("La casa editrice non e' valida!")
        else:
            break

    #Se i nuovi dati inseriti sono corretti, procedo con la modifica del record nel database
    #Il valore "libro[0]" corrisponde all'id del libro ricercato, necessario per modificare quello specifico libro
    db.aggiornaLibro(titolo,autore,numero_pagine,prezzo,casa_editrice,libro[0])
    print("Libro modificato correttamente")
    input("Premi un tasto per continuare.")
