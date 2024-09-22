from database.db_manager import DbManager
from core import core
from api.api import app
from threading import Thread

#Viene creato l'oggetto per la gestione del database
db = DbManager()

#Funzione per l'avvio dell'API
def startFlaskApp():
    app.run(debug=True, use_reloader=False)

def visualizzaMenu():
    print(chr(27) + "[2J")
    print("0- Esci")
    print("1- Aggiungi autore/libro")
    print("2- Visualizza tabella autori/libri")
    print("3- Modifica autore/libro")
    print("4- Elimina autore/libro")
    print("5- Importa autori/libri da CSV")
    print("6- Avvia server per le richieste API")

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
            print(chr(27) + "[2J")
            print(db.visualizzaAutori())
            input("Premi invio per continuare")
        if choice == '2':
            print(chr(27) + "[2J")
            print(db.visualizzaLibri())
            input("Premi invio per continuare")

    #Menu modifica
    if opz == '3':
            sottoMenu()
            choice = input("Opzione: ")
            if choice == '0':
                visualizzaMenu()
            if choice == '1':
                core.modificaAutore(db)
            if choice == '2':
                core.modificaLibro(db)

    #Menu eliminazione
    if opz == '4':
                sottoMenu()
                choice = input("Opzione: ")
                if choice == '0':
                    visualizzaMenu()
                if choice == '1':
                    core.eliminaAutore(db)
                if choice == '2':
                    core.eliminaLibro(db)


    #Menu import CSV
    if opz == '5':
                    sottoMenu()
                    choice = input("Opzione: ")
                    if choice == '0':
                        visualizzaMenu()
                    if choice == '1':
                        core.importaAutori(db,'autori.csv')
                    if choice == '2':
                        core.importaLibri(db,'libri.csv')


    if opz == '6':
        if __name__ == "__main__":
            flask_thread = Thread(target=startFlaskApp)
            flask_thread.start()
