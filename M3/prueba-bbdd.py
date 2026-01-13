import mysql.connector

# CONFIGURACIÓN DEL PUENTE (Cámbialo por tus datos de Bore)
HOST_BORE = "bore.pub"
PUERTO_BORE = 38069  # <--- SUSTITUYE ESTO POR TU NÚMERO

def ejecutar_test():
    try:
        # 1. Intentar conectar
        print(f"Conectando a {HOST_BORE}:{PUERTO_BORE}...")
        db = mysql.connector.connect(
            host=HOST_BORE,
            port=PUERTO_BORE,
            user="ameragrajea",
            password="1234",
            database="minijuego_db"
        )
        cursor = db.cursor()
        print("✅ Conexión establecida con éxito.\n")

        # 2. PROBAR LECTURA: Ver personajes
        print("--- Leyendo personajes desde el servidor ---")
        cursor.execute("SELECT nombre, descripcion FROM personajes")
        personajes = cursor.fetchall()
        for p in personajes:
            print(f"• {p[0]}: {p[1]}")

        # 3. PROBAR ESCRITURA: Registrar una partida de prueba
        print("\n--- Guardando una partida de prueba ---")
        nombre_test = "Tester_Manual"
        id_guerrero = 1
        query_insert = "INSERT INTO historial_partidas (jugador, personaje_id) VALUES (%s, %s)"
        cursor.execute(query_insert, (nombre_test, id_guerrero))
        db.commit() # ¡Importante! Sin esto no se guardan los cambios
        print("✅ Partida guardada en el servidor.")

        # 4. VERIFICAR: Leer el historial
        print("\n--- Verificando historial actualizado ---")
        cursor.execute("SELECT jugador, fecha FROM historial_partidas")
        for h in cursor.fetchall():
            print(f"Jugador: {h[0]} | Fecha: {h[1]}")

        # Cerrar conexión
        cursor.close()
        db.close()
        print("\n--- Prueba finalizada correctamente ---")

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")

if __name__ == "__main__":
    ejecutar_test()
    input("\nPresiona Enter para cerrar...")