from flask import Flask, render_template, request

from db.crud_tareas import crear_tarea

app = Flask(__name__)

# Configuración básica

app.config['SECRET_KEY'] = '@#qwr$"'

# Rutas

@app.route('/')
def index():
    return render_template('index.html')

# Ruta /guardar las tareas

@app.route('/guardar', methods=['POST'])
def guardar():
    # Recuperar los datos del formulario
    datos = request.json
    print (request)
    # Crear la tarea con los datos
    resultado = crear_tarea(datos)
    # Añadir la tarea a la lista de tareas
    if resultado:
        return {'mensaje': resultado}
    else:
        return {'mensaje': 'Error al guardar la tarea'}, 500