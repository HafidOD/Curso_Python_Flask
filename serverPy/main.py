from flask import Flask
from flask import render_template, request

app = Flask(__name__) #contexto main

#callbacks
@app.before_request
def before_request():
   print("Antes de la peticion")

@app.after_request
def after_request(respose):
   print("Despues de la peticion")
   return respose

@app.route('/')
def index():
   name = 'Hafid'
   course = 'Python web'
   premium= True
   courses = ['python', 'go', 'php']
   return render_template('index.html', userName = name,
                                        course = course,
                                        premium = premium,
                                        courses = courses ) #flask buscara en la carpeta templates por defecto por eso se omite

#params se reciben como strings, se define otro tipo anteponiendo el tipo de dato
@app.route('/usuario/<username>/<int:age>') #para pasar parametros se escribe entre <>
def usuario(username, age): # se paran los parametros
   return 'Hola ' + username + ' ' + str(age)

@app.route('/query')
def datos():
   #se tiene que importar
   # from flask import request
   nombre = request.args.get('nombre', ' ') # se recibe query como diccionarios, si no existe el segundo arg es el default
   return 'Datos: ' + nombre
   # http://localhost:3000/query?nombre=hafid

@app.route('/about')
def about():
   print("Estoy en una peticion")
   return render_template('about.html')

if __name__ == "__main__": #si el contexto es igual a main ejecutar server
    app.run(debug=True, port=3000) # modo debugg activado