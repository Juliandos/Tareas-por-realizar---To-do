from flask import Flask, render_template

app = Flask(__name__)

# Configuración básica

app.config['SECRET_KEY'] = '@#qwr$"'

# Rutas

@app.route('/')
def index():
    return render_template('index.html')
