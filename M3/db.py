import requests
import mysql.connector
import random
import string


def obtener_conexion():
    try:
        # Cache busting genera 5 letrasnúmeros aleatorios
        v = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        url = f"https://raw.githubusercontent.com/Choosestory/puerto/main/puerto.txt?"

        # Obtener puerto y conectar
        puerto = int(requests.get(url, timeout=5).text.strip())

        return mysql.connector.connect(
            host="bore.pub",
            port=puerto,
            user="aitor_admin",
            password="aitor",
            database="choose_your_story"
        )
    except:
        return None





