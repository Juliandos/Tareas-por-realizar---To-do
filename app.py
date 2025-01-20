from flask import Flask, render_template, request

app = Flask(__name__)

# Configuración básica

app.config['SECRET_KEY'] = '@#qwr$"'

# Rutas

@app.route('/')
def index():
    return render_template('index.html')

# Ruta /guardar las tareas

@app.route('/guardar', methods=['POST'])
def guardar_tareas():
    # Recuperar los datos del formulario
    datos = request.json
    # Añadir la tarea a la lista de tareas
    return {'mensaje': 'Tarea guardada'}
    # print (datos)