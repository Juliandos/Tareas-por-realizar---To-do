# Función para conexión a una basa Sqlite

import sqlite3


def connection():
    conn = None
    try:
        conn = sqlite3.connect('/db/Db_tareas_realizar.db')  # Crea una base de datos en memoria
        return conn
    except sqlite3.Error as e:
        return ''