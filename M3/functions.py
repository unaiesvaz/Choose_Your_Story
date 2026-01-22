import json
from M3.variables import ejecutar_query_insert
from db import obtener_conexion

#######FUNCIONES PARA DEVOLVER DICCIONARIOS#######
def get_answers_bystep_adventure():
    from variables import idAnswers_ByStep_Adventure
    return idAnswers_ByStep_Adventure
def get_adventures_with_chars():
    from variables import ADVENTURES
    return ADVENTURES
def get_id_bystep_adventure():
    from variables import id_by_steps
    return id_by_steps
def get_first_step_adventure(id_adventure):
    from variables import FIRST_STEP_BY_ADVENTURE
    return FIRST_STEP_BY_ADVENTURE[id_adventure]
def get_characters():
    from variables import CHARACTERS
    return CHARACTERS
def getReplayAdventures():
    from variables import GAMES
    return GAMES
def getUsers():
    from variables import USERS
    return USERS
#######FIN DE FUNCIONES PARA DEVOLVER DICCIONARIOS#######

def insertCurrentGame(idUser, idChar, idAdventure, stepsList): # Esta funcion nos sirve para insertar una partida en la base de datos para mas tarde, poder volver a jugarla (opcion de replay adventure)
    steps_json= json.dumps(stepsList)
    query = "INSERT INTO games (id_user, id_character, id_adventure, current_step, game_date) VALUES (%s, %s, %s, %s, NOW())"
    ejecutar_query_insert(obtener_conexion(),query,(idUser,idChar,idAdventure,steps_json))

def getUserIds(): # Esta funcion nos da una lista compuesta con los usernames y los ids de los usuarios
    lista_users = []
    lista_ids = list(getUsers().keys())
    for clave in lista_ids:
        lista_users.append(getUsers()[clave]["username"])
    return [lista_users]+[lista_ids]

def insertUser(username, password): # Esta funcion nos sirve para que, al crear un usuario, se guarde en la base de datos
    query = "INSERT INTO users (username, password, created_at) VALUES (%s, %s, NOW())"
    ejecutar_query_insert(obtener_conexion(),query,(username, password))


def userExists(user): # Sirve para comprobar si un usuario existe
    lista = getUserIds()
    if user not in lista[0]:
        return False
    else:
        return True

def checkUserbdd(user, password): # Sirve para confirmar que la contraseña
    var = userExists(user)
    if not var:
        return 0

    USERS = getUsers()
    id_user = 0
    for clave in USERS:
        if USERS[clave]["username"] == user:
            id_user = clave
            break

    if password != getUsers()[id_user]["password"]:
        return -1
    return 1


def getHeader(text,ancho): # Nos sirve para que nos de un header bonico
    header = "*".center(ancho,"*") + "\n" + text.center(ancho,"=") + "\n" + "*".center(ancho,"*") + "\n"
    return header

def getFormatedBodyColumns(tupla_texts, tupla_sizes, margin=0): # Nos sirve para tener formato correcto en algunos apartados como las respuestas mas usadas en informes
    columnas = []
    for i in range(len(tupla_texts)):
        texto = tupla_texts[i]
        ancho = tupla_sizes[i]

        palabras = texto.split()
        lineas = []
        linea_actual = ""

        for palabra in palabras:
            if len(linea_actual) + len(palabra) + 1 <= ancho:
                if linea_actual:
                    linea_actual += " " + palabra
                else:
                    linea_actual = palabra
            else:
                if linea_actual:
                    lineas.append(linea_actual)
                linea_actual = palabra

        if linea_actual:
            lineas.append(linea_actual)

        columnas.append(lineas)

    max_lineas = 0
    for col in columnas:
        if len(col) > max_lineas:
            max_lineas = len(col)

    for col in columnas:
        while len(col) < max_lineas:
            col.append("")

    resultado = ""
    for fila in range(max_lineas):
        for i in range(len(columnas)):
            texto_linea = columnas[i][fila].ljust(tupla_sizes[i])
            resultado += texto_linea

            if i < len(columnas) - 1:
                resultado += " " * margin

        resultado += "\n"

    return resultado

def getFormatedAdventures(adventures): # Nos sirve para tener un formato correcto de las aventuras
    texto = ""
    for id_adv in adventures:
        id_str = str(id_adv)
        nombre = adventures[id_adv]["Name"]
        descripcion = adventures[id_adv]["Description"]

        texto += getFormatedBodyColumns((id_str, nombre, descripcion),(12, 30, 48), margin=0)
    return texto

def getHeadeForTableFromTuples(t_name_columns, t_size_columns): # Esta funcion nos sirve para sacar cabeceras de tablas
    ancho_final = 0
    for ancho in t_size_columns:
        ancho_final += ancho
    texto = "=".center(ancho_final,"=") + "\n"

    for i in range(len(t_name_columns)):
        texto += t_name_columns[i].ljust(t_size_columns[i])
    texto += "\n"
    texto += "*".center(ancho_final,"*") + "\n"

    return texto

def getOpt(textOpts, inputOptText, rangeList, dictionary, exceptions): # Nos sirve para navegar por menus en general, le pasas una opcion y si esta en el rango de opciones correctas (rangelist) pues te devuelve la opcion para guardarla o para darle el uso que sea
    print(textOpts)
    while True:
        opcion = input(inputOptText)

        if opcion in exceptions:
            return opcion

        if opcion.isdigit():
            opcion = int(opcion)
            if opcion in rangeList:
                return opcion

        print("Invalid option")

def checkPassword(password): # Comprobacion del formato de la contrasena
    if len(password) <= 8 or len(password) >= 12:
        print("Length of password must be between 8 and 12 characters\n")
        return False
    if password.find(" ") != -1:
        print("Password cant have spaces\n")
        return False
    return True
def checkUser(user): # Comprobacion de formato al introducir el usuario
    if len(user) <= 6 or len(user) >= 10:
        print("Length of username must be between 6 and 10 characters\n")
        return False
    return True



