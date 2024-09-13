class Autore:

    #Costruttore
    def __init__(self,id_autore,nome,data_nascita,email):
        self._id_autore = id_autore
        self._nome = nome
        self._data_nascita = data_nascita
        self._email = email

    #Getters
    def getId(self):
        return self._id_autore

    def getNome(self):
        return self._nome

    def getDataNascita(self):
        return self._data_nascita

    def getEmail(self):
        return self._email


    #Setters
    def setId(self,id_autore):
        self._id_autore = id_autore

    def setNome(self,nome):
        self._nome = nome

    def setDataNascita(self,data_nascita):
        self._data_nascita = data_nascita

    def setEmail(self,email):
        self._email = email
