class Libro:

    #Costruttore
    def __init__(self,id,titolo,nome_autore,numero_pagine,prezzo,casa_editrice,autore_id):
        self._id = id
        self._titolo = titolo
        self._nome_autore = nome_autore
        self._numero_pagine = numero_pagine
        self._prezzo = prezzo
        self._casa_editrice = casa_editrice
        self._autore_id = autore_id

    #Getters
    def getId(self):
        return self._id

    def getTitolo(self):
        return self._titolo

    def getNomeAutore(self):
        return self._nome_autore

    def getNumeroPagine(self):
        return self._numero_pagine

    def getPrezzo(self):
            return self._prezzo

    def getCasaEditrice(self):
            return self._casa_editrice

    def getAutoreId(self):
            return self._autore_id


    #Setters
    def setId(self,id):
        self._titolo = id

    def setTitolo(self,titolo):
        self._titolo = titolo

    def setNomeAutore(self,nome_autore):
        self._nome_autore = nome_autore

    def setNumeroPagine(self,numero_pagine):
        self._numero_pagine = numero_pagine

    def setPrezzo(self,prezzo):
            self._prezzo = prezzo

    def setCasaEditrice(self,casa_editrice):
            self._casa_editrice = casa_editrice

    def setAutoreId(self,autore_id):
            self._autore_id = autore_id
