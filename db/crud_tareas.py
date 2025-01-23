from .conexion import connection

# Función para leer todas las tareas

def leer_tareas():
    try:
        conn = connection()
        cursor = conn.cursor()
        query = "SELECT * FROM tareas"
        cursor.execute(query)
        tareas = cursor.fetchall()
        conn.close()
        return tareas
    except Exception as e:
        return {"message": "Error al leer las tareas", "error": str(e)}

def crear_tarea(tarea):
    print(tarea, tarea['titulo'], tarea['fecha'], tarea['terminada'])
    try:
        # Conectarse a la base de datos
        conn = connection()
        
        # Crear una nueva tarea
        cursor = conn.cursor()
        query = """
        INSERT INTO tareas (Titulo, Fecha, Terminada) 
        VALUES (?, ?, ?)
        """
        # values = ("Tarea de prueba", "2025-01-20", 0)  # Fecha de ejemplo y Terminada = 0 (no terminada)
        cursor.execute(query, (tarea['titulo'], tarea['fecha'], tarea['terminada']))
        
        # Obtener el ID de la tarea insertada
        cursor.execute("SELECT LAST_INSERT_ROWID()")
        id_tarea = cursor.fetchone()[0]
        
        # Cerrar la conexión
        conn.commit()
        cursor.close()
        conn.close()
        
        return {"message": "Tarea creada con éxito", "id_tarea": id_tarea}
    
    except Exception as e:
        # Rollback en caso de error
        # conn.rollback()
        return {"message": "Error al crear la tarea", "error": str(e)}

def eliminar_tarea(id_tarea):
    try:
        # Conectarse a la base de datos
        conn = connection()
        
        # Eliminar la tarea
        cursor = conn.cursor()
        query = "DELETE FROM tareas WHERE ID = ?"
        cursor.execute(query, (id_tarea,))
        
        # Cerrar la conexión
        conn.commit()
        cursor.close()
        conn.close()
        
        return {"message": "Tarea eliminada con éxito"}
    
    except Exception as e:
        # Rollback en caso de error
        # conn.rollback()
        return {"message": "Error al eliminar la tarea", "error": str(e)}
    
# Función para traer el id de una tarea
