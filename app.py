#hoy creamos una pagina web (local) con un flask
from flask import Flask,render_template #importacion
import casas
app= Flask(__name__) #crea el objeto app, instancia la clase flask, el parametro __name__ indica que esta en el "script principal"

@app.route("/") #este es el index
def indice():
    datos = casas.casas() #llamado a la funcion casas
    return render_template('index2.html',datos = datos)
#Esta es la rpta del servidor


if __name__ == "__main__":
    app.run()
    #esto se ejecuta solamente si es el archivo principal
#set FLASK_APP=app.py #(export en linux en vez de export) Se escribe esto en la terminal para agregar al path
#flask run #hace correr el servidor localmente
