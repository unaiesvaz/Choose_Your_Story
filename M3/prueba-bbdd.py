import requests
import mysql.connector
import time
import random
import string
import sys


def obtener_puerto():
    # URL RAW de vuestro repositorio
    url_base = "https://raw.githubusercontent.com/Choosestory/puerto/main/puerto.txt"
    # Cache buster para evitar leer el puerto viejo
    rand = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    url = f"{url_base}?v={rand}"

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return int(r.text.strip())
    except Exception as e:
        print(f"❌ Error al obtener el puerto de GitHub: {e}")
        return None


def conectar_db():
    print("=== COMPROBADOR DE CONEXIÓN PROYECTO ===")

    puerto = obtener_puerto()
    if not puerto:
        return

    print(f"📡 Intentando conectar al puerto: {puerto}...")

    try:
        # Configuración de vuestra base de datos
        conexion = mysql.connector.connect(
            host="bore.pub",
            port=puerto,
            user="aitor_admin",  # Cambia esto si usas otro
            password="aitor",  # Poned vuestra contraseña real aquí
            connect_timeout=10
        )

        if conexion.is_connected():
            print("\n" + "=" * 40)
            print("✅ ¡ÉXITO! Conexión establecida correctamente.")
            print(f"🖥️ Servidor: {conexion.server_info}")
            print("=" * 40)
            conexion.close()

    except Exception as e:
        print("\n" + "!" * 40)
        print(f"❌ ERROR DE CONEXIÓN: {e}")
        print("Sugerencia: Verifica que el túnel de Bore esté abierto en el servidor.")
        print("!" * 40)


if __name__ == "__main__":
    conectar_db()

    # ESTA ES LA PARTE CLAVE:
    # Evita que la ventana se cierre sola.
    print("\n" + "-" * 40)
    input("Presiona ENTER para cerrar esta ventana...")
    sys.exit()