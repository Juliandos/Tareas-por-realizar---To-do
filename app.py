from flask import Flask

app = Flask(__name__)

# Configuración básica

app.config['SECRET_KEY'] = '@#qwr$"'

# Rutas

@app.route('/')
def index():
    return 'Página principal'
