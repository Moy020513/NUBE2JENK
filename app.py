import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv 

#Cargar las variables de entorno
load_dotenv()

#crear instancia
app =  Flask(__name__)

#Ruta raiz
@app.route('/')
def index():
    return 'Hola Mundo, esto es una prueba 2 contenedor, contenedor automatico cada minuto'

if __name__ == '__main__':
    app.run(debug=True)