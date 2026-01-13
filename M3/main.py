from functions import *
menu = "1. Login\n2. Crear usuario\n3. Jugar aventura\n4. Repetir partida\n5. Informes\n6. Salir"
menu_seleccion_historia = "Adventures".center(100,"=") + "\n\n" + "Id".ljust(3) + "Adventure".ljust(40) + "Description".ljust(57) + "\n" + "*".center(100,"*") + "\n"

salir = False
menu_principal = True

login = False
create_user = False
play_adventure = False
replay_adventure = False
informes = False


while not salir:
    while menu_principal:
        print(menu)
        opcion = input("->Option: ")
        if not opcion.isdigit() or not (int(opcion) in range(1, 7)):
            input("Invalid Option")
        else:
            opcion = int(opcion)
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
        username = ""
        password = ""
        print(getUserIds())
        login = False
        menu_principal = True
    while create_user:
        print("create user")
        create_user = False
        menu_principal = True
    while play_adventure:
        datos = ""
        datos_aventura = ""
        datos_characters = ""
        datos_rutas = ""
        aventuras = get_adventures_with_chars()
        for clave in aventuras:
            datos += str(clave).ljust(3) + aventuras[clave]["Name"].ljust(40) + aventuras[clave]["Description"].ljust(57) + "\n"
        print(menu_seleccion_historia+datos)

        opcion_aventura = input("->Option: ")
        while not opcion_aventura.isdigit() or int(opcion_aventura) not in aventuras.keys():
            input("Invalid Option")
            opcion_aventura = input("->Option: ")
        opcion_aventura = int(opcion_aventura)
        datos_aventura = "{}{}\n\n{}{}\n\n".format("Adventure:".ljust(15),aventuras[opcion_aventura]["Name"].ljust(65),"Description:".ljust(15),aventuras[opcion_aventura]["Description"].ljust(65))
        print(getHeader(aventuras[opcion_aventura]["Name"])+datos_aventura)
        input("Enter to Continue")

        characters = get_characters()
        for clave in characters:
            if clave in aventuras[opcion_aventura]["characters"]:
                datos_characters += str(clave) + ")" + characters[clave] + "\n"

        print("Characters".center(30, "=") + "\n" + datos_characters)
        opcion_char = input("->Option: ")
        while not opcion_char.isdigit() or int(opcion_char) not in characters.keys():
            print("Invalid Option\n" + "Characters".center(30, "=") + "\n" + datos_characters)
            opcion_char = input("->Option: ")
        opcion_char = int(opcion_char)


        id_adventure = get_id_bystep_adventure()
        first_step = get_first_step_adventure(opcion_aventura)
        answers_by_step = get_answers_bystep_adventure()
        print(id_adventure[first_step]["Description"])

        for rutas in id_adventure[first_step]["answers_in_step"]:
            if rutas in answers_by_step.keys():
                datos_rutas += str(rutas) + ")" + answers_by_step[rutas]["Description"] + "\n"
        print(datos_rutas)

        opcion_eleccion = input("->Option: ")
        while not opcion_eleccion.isdigit() or int(opcion_eleccion) not in answers_by_step.keys():
            input("Invalid Option")
            opcion_eleccion = input("->Option: ")
        opcion_eleccion = int(opcion_eleccion)
        if answers_by_step[opcion_eleccion]["NextStep_Adventure"] == 0:
            print(answers_by_step[opcion_eleccion]["Resolution_Answer"])
            input("Enter to Continue")
            break
        else:
            print(answers_by_step[opcion_eleccion]["Resolution_Answer"])
            input("Enter to Continue")


        play_adventure = False
        menu_principal = True
    while replay_adventure:
        print("replay adventure")
        replay_adventure = False
        menu_principal = True
    while informes:
        print("informes")
        informes = False
        menu_principal = True