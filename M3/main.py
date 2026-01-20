from functions import *
from db import obtener_conexion

menu_sin_logear = "1. Login\n2. Crear usuario\n3. Jugar aventura\n4. Repetir partida\n5. Informes\n6. Salir"
menu_logeado = "1. Logout\n2. Play\n3. Replay Adventure\n4. Reports\n5. Exit"


salir = False
menu_principal = True

login = False
create_user = False
play_adventure = False
replay_adventure = False
informes = False
correct_login = False

if obtener_conexion() == None:
    salir = True
    print("No se pudo conectar a la base de datos\n")

while not salir:
    while menu_principal:
        if not correct_login:
            opcion = getOpt(menu_sin_logear, "->Option: ", [1, 2, 3, 4, 5, 6],{},{})
            if opcion == 1:
                login = True
                menu_principal = False
            elif opcion == 2:
                create_user = True
                menu_principal = False
            elif opcion == 3:
                play_adventure = True
                menu_principal = False
            elif opcion == 4:
                replay_adventure = True
                menu_principal = False
            elif opcion == 5:
                informes = True
                menu_principal = False
            elif opcion == 6:
                salir = True
                menu_principal = False
        else:
            opcion = getOpt(menu_logeado, "->Option: ", [1, 2, 3, 4, 5], {}, {})
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
            login = False
            menu_principal = True

        input("Enter to Continue")
        correct_login = True
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
        print("Correct password")
        insertUser(username,password)

        create_user = False
        menu_principal = True
    while play_adventure:
        datos = ""
        datos_aventura = ""
        datos_characters = ""
        aventuras = get_adventures_with_chars()
        print(aventuras)

        opcion_aventura = getOpt(getFormatedAdventures(aventuras), "->Option: (0 to go back)\n", aventuras.keys(),aventuras,["0"])
        opcion_aventura = int(opcion_aventura)
        if opcion_aventura == 0:
            play_adventure = False
            menu_principal = True
            break

        datos_aventura = "{}{}\n\n{}{}\n\n".format("Adventure:".ljust(15),aventuras[opcion_aventura]["Name"].ljust(65),"Description:".ljust(15),aventuras[opcion_aventura]["Description"].ljust(65))
        print(getHeader(aventuras[opcion_aventura]["Name"])+datos_aventura)
        input("Enter to Continue")

        characters = get_characters()
        for clave in characters.keys():
            if clave in aventuras[opcion_aventura]["characters"]:
                datos_characters += str(clave) + ")" + characters[clave] + "\n"

        char_datos = "Characters".center(30, "=") + "\n" + datos_characters

        opcion_char = getOpt(char_datos, "->Option: ", aventuras[opcion_aventura]["characters"],characters,[])

        id_adventure = get_id_bystep_adventure()
        first_step = get_first_step_adventure(opcion_aventura)
        answers_by_step = get_answers_bystep_adventure()

        while True:
            datos_rutas = ""
            cabecera_historia = getHeader(aventuras[opcion_aventura]["Name"])
            if id_adventure[first_step]["Final_Step"]:
                print(id_adventure[first_step]["Description"])
                input("Enter to Continue")
                break
            else:
                print(id_adventure[first_step]["Description"])

            for rutas in id_adventure[first_step]["answers_in_step"]:
                key = (rutas, first_step)
                if key in answers_by_step:
                    datos_rutas += str(rutas) + ")" + answers_by_step[key]["Description"] + "\n"

            valid_answers = id_adventure[first_step]["answers_in_step"]
            opcion_eleccion = getOpt(datos_rutas, "->Option: ", id_adventure[first_step]["answers_in_step"],id_adventure,[])

            respuesta = answers_by_step[(opcion_eleccion, first_step)]

            print(respuesta["Resolution_Answer"])
            first_step = respuesta["NextStep_Adventure"]

    while replay_adventure:
        print("replay adventure")
        replay_adventure = False
        menu_principal = True
    while informes:
        print("informes")
        informes = False
        menu_principal = True