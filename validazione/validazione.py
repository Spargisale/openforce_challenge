from datetime import datetime
import re

#VALIDAZIONE DELLE VARIABILI


#Il nome dell'autore ammette parole multiple, lettere accentate, trattino e punto
#E.g. "Josè Garcìa Márquez", "Anne-Marie Jenson"
def validaNome(nome):
    pattern_nome = r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[-\s][A-Za-zÀ-ÖØ-öø-ÿ]+)+(?:\s(?:[A-Za-zÀ-ÖØ-öø-ÿ]+\.))?$"
    try:
        if re.match(pattern_nome,nome):
            return True
    except ValueError:
        return False

#La data deve essere del formato gg-mm-aaaa o gg-m-aaaa e non ammette giorni oltre la fine del mese (e.g. 30 febbraio)
def validaData(data):
    try:
        data = datetime.strptime(data, "%d-%m-%Y")
        return True
    except ValueError:
        return False

#Questo pattern per la validazione dell'email non ammette i punti all'inizio oppure punti multipli alla fine ad esempio, ma valida correttamente una classica email ben formattata
def validaEmail(email):
    pattern_email = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
    try:
        if re.match(pattern_email,email):
            return True
    except ValueError:
        return False


#Il titolo del libro ammette spazi multipli tra le parole che lo compongono, lettere accentate e i punti
def validaTitolo(titolo):
    pattern_titolo = r"^[A-Za-zÀ-ÖØ-öø-ÿ' ]+([.][A-Za-zÀ-ÖØ-öø-ÿ' ]+)*$"
    try:
        if re.match(pattern_titolo,titolo):
            return True
    except ValueError:
        return False


#Casting a int di un valore (utilizzato per il numero delle pagine del libro)
def validaInt(a):
    try:
        a = int(a)
        return True
    except ValueError:
        return False

#Casting a float di un valore (utilizzato per il prezzo del libro)
def validaFloat(a):
    try:
        a = float(a)
        return True
    except ValueError:
        return False



#Funzione di ordine superiore
#Questa funzione serve per chiedere valori in input all'utente; è strutturata in modo tale che
#ogni input viene fatto diventare tutto minuscolo e se non "passa" il controllo di validazione
#(la funzione di validazione cambia a seconda del valore da inserire), restituisce un messaggio di errore diverso
#a seconda del valore e chiede di reinserire il valore.
def chiediInputUtente(messaggio,funzione_validazione,messaggio_errore):
    while True:
        input_utente = input(messaggio).lower()
        if funzione_validazione(input_utente):
            return input_utente
        else:
            print(messaggio_errore)
