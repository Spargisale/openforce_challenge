from datetime import datetime

#Funzioni di validazione delle variabili
def validaData(data):
    try:
        data = datetime.strptime(data, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def validaInt(a):
    try:
        a = int(a)
        return True
    except ValueError:
        return False


def validaFloat(a):
    try:
        a = float(a)
        return True
    except ValueError:
        return False


#TODO: utilizzare regex
def validaEmail(email):
    try:
        if '@' in email and '.' in email:
            return True
    except ValueError:
        return False
