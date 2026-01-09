# Adventures
menu = "1. Login\n2. Crear usuario\n3. Jugar aventura\n4. Repetir partida\n5. Informes\n6. Salir"

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
        print("login")
        login = False
        menu_principal = True
    while create_user:
        print("create user")
        create_user = False
        menu_principal = True
    while play_adventure:
        print("play adventure")
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