from functions import *
from db import obtener_conexion

menu_logeado = "\n1. Logout\n2. Play\n3. Replay Adventure\n4. Reports\n5. Exit\n"
menu_sin_logear = "\n1. Login\n2. Create User\n3. Replay Adventure\n4. Reports\n5. Exit\n"


salir = False
menu_principal = True

login = False
create_user = False
play_adventure = False
replay_adventure = False
informes = False
correct_login = False

user_id = 0

if obtener_conexion() == None: # En el caso de que no conecete con la base de datos el programa no se ejecuta
    salir = True
    print("No se pudo conectar a la base de datos\n")

while not salir:
    while menu_principal:
        if not correct_login:
            opcion = getOpt(menu_sin_logear, "->Option: ", [1, 2, 3, 4, 5],{},[])
            if opcion == 1:
                login = True
                menu_principal = False
            elif opcion == 2:
                create_user = True
                menu_principal = False
            elif opcion == 3:
                replay_adventure = True
                menu_principal = False
            elif opcion == 4:
                informes = True
                menu_principal = False
            elif opcion == 5:
                salir = True
                menu_principal = False
        else:
            opcion = getOpt(menu_logeado, "->Option: ", [1, 2, 3, 4, 5], {}, [])
            if opcion == 1:
                correct_login = False
                print("Has cerrado sesion")
                input("Enter to Continue")
            elif opcion == 2:
                menu_principal = False
                play_adventure = True
            elif opcion == 3:
                replay_adventure = True
                menu_principal = False
            elif opcion == 4:
                informes = True
                menu_principal = False
            elif opcion == 5:
                salir = True
                menu_principal = False
    while login:
        username = input("Escribe tu nombre de usuario\n")
        password = input("Escribe la contraseña\n")
        val = checkUserbdd(username,password)
        if val == 0:
            print("User NOT FOUND")
        elif val == -1:
            print("Incorrect Password")
        else:
            print("Correct User")
            lista = getUserIds()
            for i in range(len(lista[0])):
                if lista[0][i] == username:
                    user_id = lista[1][i]
            correct_login = True
            login = False
            menu_principal = True

        input("Enter to Continue")
        login = False
        menu_principal = True
    while create_user:
        username = input("Username:\n")
        lista = getUserIds()
        while username in lista[0] or not checkUser(username):
            print("Invalid User")
            username = input("Username:\n")
        val = False
        password = ""
        while not val:
            password = input("Password:\n")
            val = checkPassword(password)
        print("Correct password format")
        insertUser(username,password)
        lista = getUserIds()
        user_id = len(lista[1])+2
        correct_login = True

        create_user = False
        menu_principal = True
    while play_adventure:
        datos = ""
        datos_aventura = ""
        datos_characters = ""
        aventuras = get_adventures_with_chars()

        opcion_aventura = getOpt(getHeader("Adventures",100)+getFormatedAdventures(aventuras), "->Option: (0 to go back)\n", aventuras.keys(),aventuras,["0"])
        opcion_aventura = int(opcion_aventura)
        if opcion_aventura == 0:
            play_adventure = False
            menu_principal = True
            break

        nombre = aventuras[opcion_aventura]["Name"]
        descripcion = aventuras[opcion_aventura]["Description"]
        datos_aventura = getFormatedBodyColumns((nombre, descripcion), (30, 70), margin=2)

        print(getHeader(aventuras[opcion_aventura]["Name"],100)+getHeadeForTableFromTuples(("Adventure","Description"),(30,70))+datos_aventura)
        input("Enter to Continue")

        characters = get_characters()
        for clave in characters.keys():
            if clave in aventuras[opcion_aventura]["characters"]:
                datos_characters += str(clave) + ")" + characters[clave] + "\n"

        char_datos = getHeader("Characters",30) + datos_characters
        print(aventuras[opcion_aventura]["characters"])
        opcion_char = getOpt(char_datos, "->Option: ", aventuras[opcion_aventura]["characters"],characters,[])

        id_adventure = get_id_bystep_adventure()
        first_step = get_first_step_adventure(opcion_aventura)
        answers_by_step = get_answers_bystep_adventure()

        lista_steps = []
        while True:
            datos_rutas = ""
            cabecera_historia = getHeader(aventuras[opcion_aventura]["Name"],80)
            if id_adventure[first_step]["Final_Step"]:
                print(id_adventure[first_step]["Description"])
                input("Enter to Continue")
                # AQUI SE GUARDARA LA PARTIDA
                id_user = user_id
                id_char = opcion_char
                id_adv = opcion_aventura
                insertCurrentGame(id_user,id_char,id_adv,lista_steps)
                break
            else:
                print(id_adventure[first_step]["Description"])

            for rutas in id_adventure[first_step]["answers_in_step"]:
                key = (rutas, first_step)
                if key in answers_by_step:
                    datos_rutas += str(rutas) + ")" + answers_by_step[key]["Description"] + "\n"

            valid_answers = id_adventure[first_step]["answers_in_step"]
            opcion_eleccion = getOpt(datos_rutas, "->Option: ", id_adventure[first_step]["answers_in_step"],id_adventure,[])

            ejecutar_query_insert(obtener_conexion(),"UPDATE step_answers SET times_reached = times_reached + 1 WHERE id_answer = %s",(opcion_eleccion,))

            lista_steps.append(opcion_eleccion)

            respuesta = answers_by_step[(opcion_eleccion, first_step)]

            print(respuesta["Resolution_Answer"])
            first_step = respuesta["NextStep_Adventure"]

    while replay_adventure:
        datos_partidas = ""
        partidas = getReplayAdventures()
        for clave in partidas.keys():
            datos_partidas += getFormatedBodyColumns((str(clave),getUsers()[partidas[clave]["idUser"]]["username"],get_adventures_with_chars()[partidas[clave]["idAdventure"]]["Name"],get_characters()[partidas[clave]["idCharacter"]],str(partidas[clave]["date"])),(10,15,30,25,20))

        opcion_replay = getOpt(getHeader("Replay Adventures",100) + getHeadeForTableFromTuples(("Id","Username","Name","CharacterName","date"),(10,15,30,25,20))+datos_partidas, "->(0 to go Back) Option: ", partidas.keys(),partidas,["0"])
        opcion_replay = int(opcion_replay)
        if opcion_replay == 0:
            replay_adventure = False
            menu_principal = True
            break

        choices = partidas[opcion_replay]["steps"]
        id_adventure = partidas[opcion_replay]["idAdventure"]
        id_by_steps = get_id_bystep_adventure()
        answers_by_step = get_answers_bystep_adventure()
        current_step = get_first_step_adventure(id_adventure)

        print(getHeader(get_adventures_with_chars()[id_adventure]["Name"],100))
        for choice in choices:

            print(id_by_steps[current_step]["Description"])

            for opt in id_by_steps[current_step]["answers_in_step"]:
                texto = answers_by_step[(opt, current_step)]["Description"]
                print("{}) {}".format(opt,texto))

            input("Enter to continue")
            print("Option {} selected".format(choice))
            print(answers_by_step[(choice, current_step)]["Resolution_Answer"])

            input("Enter to continue")

            current_step = answers_by_step[(choice, current_step)]["NextStep_Adventure"]

        replay_adventure = False
        menu_principal = True

    while informes:
        opcion = getOpt("1)Respuestas más usadas\n2)Jugador con más partidas\n3)Partidas jugadas por usuario\n4)Exit","->Option: ", [1, 2, 3, 4], {}, [])

        if opcion == 1:
            dicc_adventures = get_adventures_with_chars()
            dicc_adventures_steps = get_id_bystep_adventure()
            dicc_step_answer = get_answers_bystep_adventure()
            lista_answer = []

            for id in dicc_step_answer:
                lista_answer.append(id)

            for pasada in range(len(lista_answer) - 1):
                for i in range(len(lista_answer) - 1 - pasada):
                    if dicc_step_answer[lista_answer[i]]["times_reached"] < dicc_step_answer[lista_answer[i + 1]]["times_reached"]:
                        lista_answer[i], lista_answer[i + 1] = lista_answer[i + 1], lista_answer[i]
            lista_answer = lista_answer[:5]

            cabecera_informes = getHeader("Informes",169) + getHeadeForTableFromTuples(("Id Aventura","Nombre","Id Paso", "Descripcion","Id Respuesta", "Descripcion","Times selected"),(14,30,10,42,15,42,16))
            datos = ""
            id_aventura = 0
            for id in lista_answer:
                if id[1] > 99 and id[1] < 199:
                    id_aventura = 1
                elif id[1] > 299 and id[1] < 399:
                    id_aventura = 2
                elif id[1] > 499 and id[1] < 599:
                    id_aventura = 3

                datos += getFormatedBodyColumns((str(id_aventura),dicc_adventures[id_aventura]["Name"],str(id[1]),dicc_adventures_steps[id[1]]["Description"],str(id[0]), dicc_step_answer[id]["Description"],str(dicc_step_answer[id]["times_reached"])),(12,28,8,40,13,40,14),margin=2)

            print(cabecera_informes+datos)

            input("Enter to continue")
            informes = False
            menu_principal = True
        elif opcion == 2:
            dicc_users = getUsers()
            player_more_games = ""
            for id in dicc_users:
                jug_actual = dicc_users[id]
                if player_more_games == "" or jug_actual["games_played"] > player_more_games["games_played"]:
                    player_more_games = jug_actual

            print("El jugador con más partidas es {} con {} partidas jugadas en total".format(player_more_games["username"],player_more_games["games_played"]))
            input("Enter to continue")
            informes = False
            menu_principal = True
        elif opcion == 3:
            user = input("Usuario a buscar: ")
            val = userExists(user)
            while not val:
                print("Not existing user")
                user = input("Usuario a buscar: ")
                val = userExists(user)

            dicc_users = getUsers()
            dicc_games = getReplayAdventures()
            dicc_adventures = get_adventures_with_chars()
            id_usuario = ""
            for id in dicc_users:
                if user == dicc_users[id]["username"]:
                    id_usuario = id
            dicc_juegos_usuario = {}
            id_aventuras_lista = []
            datos = ""
            cabecera_last_games = getHeader("Games played by {}".format(user),70)+getHeadeForTableFromTuples(("Id Adventure","Adventure Name","date"),(20,30,20))
            for id in dicc_games:
                if id_usuario == dicc_games[id]["idUser"]:
                    datos += getFormatedBodyColumns((str(dicc_games[id]["idAdventure"]),dicc_adventures[dicc_games[id]["idAdventure"]]["Name"],str(dicc_games[id]["date"])),(20,30,20))

            print(cabecera_last_games+datos)

            input("Enter to continue")
            informes = False
            menu_principal = True
        elif opcion == 4:
            informes = False
            menu_principal = True