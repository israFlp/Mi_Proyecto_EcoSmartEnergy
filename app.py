import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Bienvenido a EcoSmart Energy – Sistema de monitoreo de consumo eléctrico"

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"Bienvenido {nombre}, a EcoSmart Energy. Consulta tu consumo aquí."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
