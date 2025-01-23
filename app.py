from flask import Flask, jsonify, render_template, request

from db.crud_tareas import crear_tarea, eliminar_tarea, leer_tareas

app = Flask(__name__)

# Configuración básica

app.config['SECRET_KEY'] = '@#qwr$"'

# Rutas

@app.route('/')
def index():
    # Obtener todas las tareas
    tareas = leer_tareas()
    return render_template('index.html', tareas=tareas)

# Ruta /guardar las tareas
@app.route('/guardar', methods=['POST'])
def guardar():
    # Recuperar los datos del formulario
    datos = request.json
    # Crear la tarea con los datos
    resultado = crear_tarea(datos)
    # Añadir la tarea a la lista de tareas
    if resultado:
        return {'mensaje': resultado}
    else:
        return {'mensaje': 'Error al guardar la tarea'}, 500
    
# Ruta para eliminar una tarea

@app.route('/eliminar/<int:id_tarea>', methods=['DELETE'])
def eliminar(id_tarea):
    # Eliminar la tarea
    resultado = eliminar_tarea(id_tarea)
    # Añadir la tarea a la lista de tareas
    if resultado:
        return resultado
    else:
        return {'mensaje': 'Error al eliminar la tarea'}, 500