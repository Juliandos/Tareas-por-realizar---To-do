from .conexion import connection

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
