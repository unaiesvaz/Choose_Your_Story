from db import obtener_conexion
conexion = obtener_conexion()

def ejecutar_query(conexion, sql, params=None):
    cursor = conexion.cursor(dictionary=True)
    try:
        cursor.execute(sql, params or ())
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al ejecutar SELECT: {e}")
        return []
    finally:
        cursor.close()

# def ejecutar_query(conexion, sql, params=None):
#     cursor = conexion.cursor(dictionary=True)
#     try:
#         # Ejecutamos la query pasando los parámetros de forma segura
#         cursor.execute(sql, params or ())
#         resultados = cursor.fetchall()
#         return resultados
#     except Exception as e:
#         print(f"Error al ejecutar la query: {e}")
#         return []
#     finally:
#         cursor.close()
def ejecutar_query_insert(conexion, sql, params=None):
    cursor = conexion.cursor()
    try:
        cursor.execute(sql, params or ())
        conexion.commit()
    except Exception as e:
        print(f"Error al ejecutar modificación: {e}")
        conexion.rollback()
    finally:
        cursor.close()

# def ejecutar_query_insert(conexion, sql, params=None):
#     cursor = conexion.cursor(dictionary=True)
#     try:
#         cursor.execute(sql, params or ())
#
#         conexion.commit()
#
#         # Solo los SELECT devuelven resultados
#         if cursor.description:
#             return cursor.fetchall()
#         else:
#             return []
#     except Exception as e:
#         print(f"Error al ejecutar la query: {e}")
#         conexion.rollback()
#         return []
#     finally:
#         cursor.close()


FIRST_STEP_BY_ADVENTURE = {
    1: 101,
    2: 301
}

resultado = ejecutar_query(obtener_conexion(),"SELECT id_user, username, password, created_at FROM users")

USERS = {}
for fila in resultado:
    id_user = fila["id_user"]
    username = fila["username"]
    password = fila["password"]
    fecha = fila["created_at"]

    USERS[id_user] = {
        "id_user": id_user,
        "username": username,
        "password": password,
        "date": str(fecha)
    }


# USERS = {
#     1: {
#         "username": "Unai",
#         "password":"1234",
#         "date": fecha de creacion del usuario
#     }
# }


resultado = ejecutar_query(obtener_conexion(), "SELECT id_character, name FROM characters")
CHARACTERS = {}
for fila in resultado:
    id_char = fila["id_character"]
    nombre = fila["name"]
    CHARACTERS[id_char] = nombre

# ADVENTURES = {
#     1: {
#         "Name": "El héroe y su espada",
#         "Description":"Esta historia trata sobre un héroe en busca de una antigua espada.\nPara encontrarla, deberá adentrarse en un misterioso bosque.",
#         "characters": [1,2]
#     }
# }
resultado = ejecutar_query(obtener_conexion(),
"SELECT a.id_adventure, a.name, a.description, ac.id_character FROM adventures a JOIN adventure_characters ac ON a.id_adventure = ac.id_adventure ORDER BY a.id_adventure ") # Esto nos devuelve la consulta de la query tal cual

ADVENTURES = {}

for fila in resultado: # Esta parte es para cambiar el formato de como lo devuelve la base de datos a un formato adecuado para nuestro codigo
    id_adv = fila["id_adventure"]
    if id_adv not in ADVENTURES:
        ADVENTURES[id_adv] = {
            "Name": fila["name"],
            "Description": fila["description"],
            "characters": []
        }
    ADVENTURES[id_adv]["characters"].append(fila["id_character"])


resultado = ejecutar_query(obtener_conexion(),
    "SELECT s.id_step, s.description, s.is_final_step, a.id_answer FROM adventure_steps s LEFT JOIN step_answers a ON s.id_step = a.id_current_step ORDER BY s.id_step, a.id_answer")

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

# id_by_steps = {
#     101: {
#         "Description": "Mientras caminas por un sendero del bosque, escuchas un llanto.\nEntre los árboles ves a un niño llorando, solo y asustado.\n¿Qué debería hacer el héroe?\n",
#         "answers_in_step": (201, 202, 203),
#         "Final_Step": False
#     },
#     102: {
#         "Description":"Llegas a una encrucijada:",
#         "answers_in_step":(204,205,206),
#         "Final_Step": False
#     },
#     103: {
#         "Description": "Dentro de la cueva encuentras un antiguo cofre.\n¿Qué deberías hacer?",
#         "answers_in_step": (207,208,209),
#         "Final_Step": False
#     },
#     701: {
#         "Description": "Has muerto. FIN.",
#         "answers_in_step": (),
#         "Final_Step": True
#     },
#     702: {
#         "Description": "Tu historia acaba aquí.\nNo has encontrado la espada pero sigues con vida\n",
#         "answers_in_step": (),
#         "Final_Step": True
#     },
#     703: {
#         "Description": "Consigues salir del bosque con la espada.\nHas conseguido tu objetivo y salido con vida\nFelicidades!\n",
#         "answers_in_step": (),
#         "Final_Step": True
#     }
# }

resultado = ejecutar_query(
    obtener_conexion(),
    "SELECT id_answer, id_current_step, answer_text, resolution_text, id_next_step FROM step_answers ORDER BY id_current_step, id_answer")

idAnswers_ByStep_Adventure = {}

for fila in resultado:
    clave = (fila["id_answer"], fila["id_current_step"])

    idAnswers_ByStep_Adventure[clave] = {
        "Description": fila["answer_text"],
        "Resolution_Answer": fila["resolution_text"],
        "NextStep_Adventure": fila["id_next_step"]
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

# idAnswers_ByStep_Adventure = {
#     (201,101): {
#         "Description": "Acercarse al niño para ayudarlo.",
#         "Resolution_Answer": "Cuando te aproximas, el niño levanta la cabeza… y sonríe.\nDe repente, se transforma en una criatura oscura que te ataca por sorpresa.\nNo tienes tiempo de reaccionar.\nEra una trampa. El héroe cae en el bosque y su historia termina aquí.\n",
#         "NextStep_Adventure": 701
#     },
#     (202,101): {
#         "Description": "Ignorar al niño y seguir el camino.",
#         "Resolution_Answer": "Sigues caminando, pero el llanto se vuelve más fuerte.\nDe pronto, el suelo bajo tus pies cede y caes en un foso oculto.\nLa culpa te distrajo. El héroe queda atrapado sin salida.\n",
#         "NextStep_Adventure": 701
#     },
#     (203,101): {
#         "Description": "Esconderse y observar desde la distancia.",
#         "Resolution_Answer": "Notas algo extraño: el niño no deja huellas en el suelo.\nDecides no acercarte y rodeas la zona con cuidado.\nMás adelante, el camino se divide en tres.\n",
#         "NextStep_Adventure": 102
#     },
#     (204,102): {
#         "Description": "Tomar el camino de la montaña.",
#         "Resolution_Answer": "El camino es peligroso y resbaladizo. Una tormenta comienza de repente.\nUn rayo cae cerca y pierdes el equilibrio.\nEl héroe cae por el acantilado.\n",
#         "NextStep_Adventure": 701
#     },
#     (205, 102): {
#         "Description": "Entrar en una cueva oscura.",
#         "Resolution_Answer": "Al entrar a la cueva, te encuentras un antiguo cofre\n¿Qué deberías hacer?\n",
#         "NextStep_Adventure": 103
#     },
#     (206, 102): {
#         "Description": "Seguir el sendero que baja hacia un pueblo.",
#         "Resolution_Answer": "El pueblo parece tranquilo, pero demasiado silencioso.\nAl entrar, las puertas se cierran de golpe.\nFinalmente, te das cuenta de que es una trampa y el héroe cae derrotado\n",
#         "NextStep_Adventure": 701
#     },
#     (207, 103): {
#         "Description": "Abrir el cofre.",
#         "Resolution_Answer": "Abres el cofre y resulta estar maldito,\nEl cofre cobra vida y acaba con el héroe\n",
#         "NextStep_Adventure": 701
#     },
#     (208, 103): {
#         "Description": "Ignorarlo y seguir avanzando.",
#         "Resolution_Answer": "Más adelante, encuentras una espada antigua que te protege de la oscuridad.\nDe esta manera, consigues tu objetivo y sales victorioso de la cueva\n",
#         "NextStep_Adventure": 703
#     },
#     (209, 103): {
#         "Description": "Salir de la cueva inmediatamente.",
#         "Resolution_Answer": "Al intentar salir de la cueva, te pierdes en el bosque.\nNo consigues encontrar el camino de vuelta al bosque.\nHas fracasado en tu misión y no has encontrado la espada\n",
#         "NextStep_Adventure": 702
#     }
# }

