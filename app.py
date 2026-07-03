import os
import time
import psycopg2

# Extraemos las credenciales que nos dará Docker Compose
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "mi_database")
DB_USER = os.environ.get("DB_USER", "usuario")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "secreto")

def conectar_db():
    #Las bases de datos tardan unos segundos en iniciar, reintentamos si falla
    for i in range(5):
        try:
            conexion = psycopg2.connect(
                host=DB_HOST, database=DB_NAME,user=DB_USER, password=DB_PASSWORD
            )
            return conexion
        except psycopg2.OperationalError:
            print("Esperando a que la base de datos esté lista...")
            time.sleep(2)
    raise Exception("No se pudo conectar a la base de datos.")

if __name__ == "__main__":
    conn = conectar_db()
    cursor = conn.cursor()

    #Crear una tabla de prueba
    cursor.execute("CREATE TABLE IF NOT EXISTS visitas (id SERIAL PRIMARY KEY, fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    
    #Insertar un registro
    cursor.execute("INSERT INTO visitas DEFAULT VALUES;")
    conn.commit()

    #Contar cuántas visitas van
    cursor.execute("SELECT COUNT(*) FROM visitas;")
    total = cursor.fetchone()[0]

    print(f"Conexión exitosa! Total de registros en la tabla 'visitas': {total}")

    cursor.close()
    conn.close()