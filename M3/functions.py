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

# getChoices()
# getIdGames()

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

# get_table(query)
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

# setIdGame() SEGURAMENTE NO SE USE PARA NADA
# insertCurrentChoice(idGame, actual_id_step, id_answer)
#def formatText(text, lenLine, split):

def getHeader(text): # Nos sirve para que nos de un header bonico
    header = "*".center(80,"*") + "\n" + text.center(80,"=") + "\n" + "*".center(80,"*") + "\n"
    return header
# getFormatedBodyColumns(tupla_texts, tupla_sizes, margin=0)
def getFormatedAdventures(adventures):
    datos = ""
    cabecera = ("Adventures".center(90,"=") + "\n\n" +
                "{:<10}{:<30}{:<50}\n".format("Id","Adventure","Description") +
                "*".center(90,"*") + "\n\n")
    for clave in adventures:
        datos += "{:<10}{:<30}{:<50}".format(clave,adventures[clave]["Name"],adventures[clave]["Description"])
    return cabecera+datos
#def getFormatedAnswers(idAnswer, text, lenLine, leftMargin):

#def getHeadeForTableFromTuples(t_name_columns, t_size_columns,title)
# getTableFromDict(tuple_of_keys, weigth_of_columns, dict_of_data)
def getOpt(textOpts, inputOptText, rangeList, dictionary, exceptions): # Nos sirve para navegar por menus en general, le pasas una opcion y si esta en el rango de opciones correctas (rangelist) pues te devuelve la opcion para guardarla o para darle el uso que sea
    # Mostrar texto del menú
    if textOpts != "":
        print(textOpts)

    while True:
        opcion = input(inputOptText)

        if opcion in exceptions:
            return opcion

        if opcion.isdigit():
            opcion_int = int(opcion)
            if opcion_int in rangeList:
                return opcion_int

        print("Invalid option")

# getFormatedTable(queryTable, title="")
def checkPassword(password): # Falta la comprobacion de minimo una mayus y una minus
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
# replay(choices)


