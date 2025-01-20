# Función para conexión a una basa Sqlite

import os
import sqlite3


def connection():
    conn = None
    try:
        # Usar una ruta relativa basada en el directorio actual
        db_path = os.path.join(os.path.dirname(__file__), 'Db_tareas_realizar.db')
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        return ''