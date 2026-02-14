from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta dinámica adaptada al negocio EcoSmart Energy
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"Bienvenido {nombre}, al sistema EcoSmart Energy. Aquí puedes consultar tu consumo eléctrico."

# Otra ruta dinámica útil para tu sistema
@app.route('/consumo/<cliente>')
def consumo(cliente):
    return f"Cliente: {cliente} – Consulta de consumo energético disponible."

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
