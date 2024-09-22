from flask import Flask, jsonify
import re
from database.db_manager import DbManager


app = Flask("Openforce")

@app.route('/<nome_autore>', methods=['GET'])
def visualizzaLibriPerAutore(nome_autore):
    db = DbManager()

    nome_autore = nome_autore.replace("_"," ") #Sostituisco gli underscore con gli spazi
    nome_autore = re.sub(r'[^\w\s]', '', nome_autore) #Rimuovo tutti gli eventuali caratteri speciali dalla stringa

    libri = db.libriPerAutoreAPI(nome_autore) #Recupero la lista dei libri associati ad un autore

    #Se la lista è vuota, ritorno un errore
    if not libri:
        return jsonify({"errore": "Nessun libro trovato per questo autore"}), 404

    #Creo una lista che conterrà le informazioni relative ai libri da mostrare poi in formato JSON
    lista_libri = []
    for libro in libri:
        lista_libri.append({
            "titolo": libro["titolo"],
            "nome_autore": libro["nome_autore"],
            "numero_pagine": libro["numero_pagine"],
            "prezzo": libro["prezzo"],
            "casa_editrice": libro["casa_editrice"]
        })

    return jsonify({"libri per ": nome_autore, "libri": lista_libri})

    if __name__ == '__main__':
        app.run(debug=True)
