from database.db_manager import DbManager
from core import core

#Viene creato l'oggetto per la gestione del database
db = DbManager()

def visualizzaMenu():
    print(chr(27) + "[2J")
    print("0- Esci")
    print("1- Aggiungi autore/libro")
    print("2- Visualizza autori/libri")
    print("3- Modifica autore/libro")
    print("4- Elimina autore/libro")
    print("5- Importa autori/libri da CSV")

def sottoMenu():
    print(chr(27) + "[2J")
    print("1- Autore")
    print("2- Libro")
    print("0- Torna indietro al menu")


while True:
    visualizzaMenu()
    opz = input("Opzione: ")

    #Esci
    if opz == '0':
        break

    #Menu inserimento
    if opz == '1':
        sottoMenu()
        choice = input("Opzione: ")
        if choice == '0':
            visualizzaMenu()
        if choice == '1':
            core.inserisciAutore(db)
        if choice == '2':
            core.inserisciLibro(db)

    #Menu visualizzazione
    if opz == '2':
        sottoMenu()
        choice = input("Opzione: ")
        if choice == '0':
            visualizzaMenu()
        if choice == '1':
            #TODO: visualizzazione autore
            print(db.visualizzaAutore())
            input("Premi un tasto per continuare")
        if choice == '2':
            print(db.visualizzaLibro())
            input("Premi un tasto per continuare")
            #TODO: visualizzazione libro

    #Menu modifica
    if opz == '3':
            sottoMenu()
            choice = input("Opzione: ")
            if choice == '0':
                visualizzaMenu()
            if choice == '1':
                #TODO: modifica autore
                pass
            if choice == '2':
                #TODO: modifica libro
                pass

    #Menu eliminazione
    if opz == '4':
                sottoMenu()
                choice = input("Opzione: ")
                if choice == '0':
                    visualizzaMenu()
                if choice == '1':
                    #TODO: elimina autore
                    pass
                if choice == '2':
                    #TODO: elimina libro
                    pass

    #Menu import CSV
    if opz == '5':
                    sottoMenu()
                    choice = input("Opzione: ")
                    if choice == '0':
                        visualizzaMenu()
                    if choice == '1':
                        #TODO: importa autore
                        pass
                    if choice == '2':
                        #TODO: importa libro
                        pass
