import requests
import mysql.connector
import random
import string

def obtener_puerto(): # Esta funcion la usamos para conectarnos al puerto del server y asi poder sacar la informacion de la bbdd
    url = "https://raw.githubusercontent.com/Choosestory/puerto/main/puerto.txt"
    return int(requests.get(url, timeout=2).text.strip())

PUERTO = obtener_puerto()
CONEXION = mysql.connector.connect(
    host="bore.pub",
    port=PUERTO,
    user="aitor_admin",
    password="aitor",
    database="choose_your_story",
    connection_timeout=3
)
def obtener_conexion():
    return CONEXION





