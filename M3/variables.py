from db import obtener_conexion
conexion = obtener_conexion()

def ejecutar_query(conexion, sql, params=None): # Esta funcion es para ejecutar querys en la base de datos, por ejemplo (mas abajo) lo usamos para sacar cada diccionario directamente de la base de datos
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute(sql, params or ())
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al ejecutar SELECT: {e}")
        return []
    finally:
        cursor.close()


def ejecutar_query_insert(conexion, sql, params=None): # Esta funcion es para ejecutar querys de tipo insert, para cuando quieras crear un usuario o guardar una partida en la base de datos
    cursor = conexion.cursor()
    try:
        cursor.execute(sql, params or ())
        conexion.commit()
    except Exception as e:
        print(f"Error al ejecutar modificación: {e}")
        conexion.rollback()
    finally:
        cursor.close()


FIRST_STEP_BY_ADVENTURE = { # Este diccionario es para saber por donde empieza cada aventura, siendo 1 el id de la aventura y 101 el primer paso de la misma
    1: 101,
    2: 301,
    3: 501
}

resultado = ejecutar_query(obtener_conexion(),"SELECT id_user, username, password, created_at, games_played FROM users") # Con resultado sacamos toda la informacion de la base de datos

USERS = {} # Despues, creamos la variables USERS de tipo diccionario y tratamos el resultado de la query para que nos quede en formato diccionario
for fila in resultado:
    id_user = fila["id_user"]
    username = fila["username"]
    password = fila["password"]
    fecha = fila["created_at"]
    games_played = fila["games_played"]

    USERS[id_user] = {
        "id_user": id_user,
        "username": username,
        "password": password,
        "date": str(fecha),
        "games_played":games_played
    }


resultado = ejecutar_query(obtener_conexion(), "SELECT id_character, name FROM characters")
CHARACTERS = {}
for fila in resultado:
    id_char = fila["id_character"]
    nombre = fila["name"]
    CHARACTERS[id_char] = nombre



resultado = ejecutar_query(obtener_conexion(),"SELECT a.id_adventure, a.name, a.description, ac.id_character FROM adventures a JOIN adventure_characters ac ON a.id_adventure = ac.id_adventure ORDER BY a.id_adventure ")
ADVENTURES = {}

for fila in resultado:
    id_adv = fila["id_adventure"]
    if id_adv not in ADVENTURES:
        ADVENTURES[id_adv] = {
            "Name": fila["name"],
            "Description": fila["description"],
            "characters": []
        }
    ADVENTURES[id_adv]["characters"].append(fila["id_character"])


resultado = ejecutar_query(obtener_conexion(),"SELECT s.id_step, s.description, s.is_final_step, a.id_answer FROM adventure_steps s LEFT JOIN step_answers a ON s.id_step = a.id_current_step ORDER BY s.id_step, a.id_answer")

id_by_steps = {}
for fila in resultado:
    step_id = fila["id_step"]

    if step_id not in id_by_steps:
        id_by_steps[step_id] = {
            "Description": fila["description"],
            "answers_in_step": [],
            "Final_Step": bool(fila["is_final_step"])
        }

    if fila["id_answer"] is not None:
        id_by_steps[step_id]["answers_in_step"].append(fila["id_answer"])


resultado = ejecutar_query(
    obtener_conexion(),
    "SELECT id_answer, id_current_step, answer_text, resolution_text, id_next_step, times_reached FROM step_answers ORDER BY id_current_step, id_answer")

idAnswers_ByStep_Adventure = {}

for fila in resultado:
    clave = (fila["id_answer"], fila["id_current_step"])

    idAnswers_ByStep_Adventure[clave] = {
        "Description": fila["answer_text"],
        "Resolution_Answer": fila["resolution_text"],
        "NextStep_Adventure": fila["id_next_step"],
        "times_reached": fila["times_reached"]
    }

resultado = ejecutar_query(obtener_conexion(),"SELECT id_game,id_user,id_character,id_adventure,current_step,game_date FROM games ORDER BY id_game")
GAMES = {}

for fila in resultado:
    id_game = fila["id_game"]

    steps = fila["current_step"].strip("[]").split(",")
    steps = [int(x) for x in steps]

    GAMES[id_game] = {
        "idUser": fila["id_user"],
        "idAdventure": fila["id_adventure"],
        "idCharacter": fila["id_character"],
        "steps": steps,
        "date": fila["game_date"]
    }

