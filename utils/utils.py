from database.db_manager import DbManager
from datetime import datetime
db = DbManager()


#INSERIMENTO
def inserisciAutore():
    #Questo ciclo serve a far reinserire i dati qualora siano sbagliati
    while True:
        nome = input("Nome e cognome: ")

        #Validazione della data; se la data non e' del giusto formato, reinserisco i dati
        while True:
            data_nascita = input("Data nascita (gg-mm-aaaa): ")
            try:
                data_nascita = datetime.strptime(data_nascita, "%d-%m-%Y")
                break
            except ValueError:
                print("La data inserita non e' valida!")

        email = input("Email: ")

        #Se la data di nascita o il nome dell'autore sono vuoti, reinserisco i dati
        if nome == '' or data_nascita == '':
            print("Il nome e la data di nascita dell'autore non possono essere vuoti")
            input("Premi un tasto per inserire di nuovo i dati. ")
        #Se i dati sono validi, controllo che l'autore inserito non sia gia' presente all'interno del database
        elif db.cercaAutorePerNome(nome):
            print("L'autore e' gia' presente nel database!")
            input("Premi un tasto per inserire di nuovo i dati. ")
        else:
            break
    #Nel caso in cui i dati siano corretti, inserisco l'autore all'interno del database
    db.inserisciAutore(nome,data_nascita,email)
    print(chr(27) + "[2J")
    print("Autore aggiunto correttamente al database!")
    input("Premi un tasto per continuare.")


def inserisciLibro():
    #TODO: controllo sul codice dell'autore
    #TODO: non far inserire all'utente il codice dell'autore ma recuperarlo dal database tramite il nome;
    #se l'autore non e' presente nel database e i campi sono corretti, allora
    #far inserire il nuovo autore
    while True:
        #dati = input("Inserisci i dati del libro (titolo, nome_autore, numero_pagine, prezzo, casa_editrice, autore_id): ")
        #titolo, nome_autore, numero_pagine, prezzo, casa_editrice, autore_id = [val.strip() for val in dati.split(",")]

        titolo = input("Titolo: ")
        nome_autore = input("Autore: ")

        #Validazione del numero di pagine e del prezzo;
        #Questi due valori devono essere rispettivamente intero e float, nel caso in cui siano diversi, reinserisco i dati
        while True:
            try:
                numero_pagine = input("Numero delle pagine: ")
                numero_pagine = int(numero_pagine)
                break
            except ValueError:
                print("Il numero delle pagine non e' valido!")

        while True:
                    try:
                        prezzo = input("Prezzo (utilizza il punto per i valori decimali): ")
                        prezzo = float(prezzo)
                        break
                    except ValueError:
                        print("Il prezzo non e' valido!")

        casa_editrice = input("Casa editrice: ")
        autore_id = input("Id autore: ")

        #Se questi valori sono vuoti, reinserisco i dati
        if titolo == '' or nome_autore == '' or prezzo == '' or casa_editrice == '' or autore_id == '':
            print("I campi non possono essere vuoti")
            input("Premi un tasto per inserire di nuovo i dati. ")
        #Se i dati sono corretti, controllo che l'autore non sia gia' presente nel database
        elif db.cercaLibroTitoloAutore(titolo,nome_autore):
            print("Il libro e' gia' presente nel database!")
            input("Premi un tasto per inserire di nuovo i dati. ")
        else:
            break
    #Nel caso in cui i dati siano corretti, inserisco il libro all'interno del database
    db.inserisciLibro(titolo,nome_autore,numero_pagine,prezzo,casa_editrice,autore_id)
    print(chr(27) + "[2J")
    print("Libro aggiunto correttamente al database!")
    input("Premi un tasto per continuare.")
