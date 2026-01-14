FIRST_STEP_BY_ADVENTURE = { # Este diccionario simula la BBDD hay que borrarlo, es para pruebas
    1: 101,
    2: 201
}

USERS = {
    "rafa": {"password": "1234", "idUser": 1},
    "jordi": {"password": "abcd", "idUser": 2}
}

CHARACTERS = {
    1: "Joselito",
    2: "Juan el superheroe"
}

ADVENTURES = {
    1: {
        "Name": "El héroe y su espada",
        "Description":"Esta historia trata sobre un héroe en busca de una antigua espada.\nPara encontrarla, deberá adentrarse en un misterioso bosque.",
        "characters": [1,2]
    }
}
id_by_steps = {
    101: {
        "Description": "Mientras caminas por un sendero del bosque, escuchas un llanto.\nEntre los árboles ves a un niño llorando, solo y asustado.\n¿Qué debería hacer el héroe?\n",
        "answers_in_step": (201, 202, 203),
        "Final_Step": False
    },
    102: {
        "Description":"Llegas a una encrucijada:",
        "answers_in_step":(204,205,206),
        "Final_Step": False
    },
    103: {
        "Description": "Dentro de la cueva encuentras un antiguo cofre.\n¿Qué deberías hacer?",
        "answers_in_step": (207,208,209),
        "Final_Step": False
    },
    701: {
        "Description": "Has muerto. FIN.",
        "answers_in_step": (),
        "Final_Step": True
    },
    702: {
        "Description": "Tu historia acaba aquí.\nNo has encontrado la espada pero sigues con vida\n",
        "answers_in_step": (),
        "Final_Step": True
    },
    703: {
        "Description": "Consigues salir del bosque con la espada.\nHas conseguido tu objetivo y salido con vida\nFelicidades!\n",
        "answers_in_step": (),
        "Final_Step": True
    }
}


idAnswers_ByStep_Adventure = {
    (201,101): {
        "Description": "Acercarse al niño para ayudarlo.",
        "Resolution_Answer": "Cuando te aproximas, el niño levanta la cabeza… y sonríe.\nDe repente, se transforma en una criatura oscura que te ataca por sorpresa.\nNo tienes tiempo de reaccionar.\nEra una trampa. El héroe cae en el bosque y su historia termina aquí.\n",
        "NextStep_Adventure": 701
    },
    (202,101): {
        "Description": "Ignorar al niño y seguir el camino.",
        "Resolution_Answer": "Sigues caminando, pero el llanto se vuelve más fuerte.\nDe pronto, el suelo bajo tus pies cede y caes en un foso oculto.\nLa culpa te distrajo. El héroe queda atrapado sin salida.\n",
        "NextStep_Adventure": 701
    },
    (203,101): {
        "Description": "Esconderse y observar desde la distancia.",
        "Resolution_Answer": "Notas algo extraño: el niño no deja huellas en el suelo.\nDecides no acercarte y rodeas la zona con cuidado.\nMás adelante, el camino se divide en tres.\n",
        "NextStep_Adventure": 102
    },
    (204,102): {
        "Description": "Tomar el camino de la montaña.",
        "Resolution_Answer": "El camino es peligroso y resbaladizo. Una tormenta comienza de repente.\nUn rayo cae cerca y pierdes el equilibrio.\nEl héroe cae por el acantilado.\n",
        "NextStep_Adventure": 701
    },
    (205, 102): {
        "Description": "Entrar en una cueva oscura.",
        "Resolution_Answer": "Al entrar a la cueva, te encuentras un antiguo cofre\n¿Qué deberías hacer?\n",
        "NextStep_Adventure": 103
    },
    (206, 102): {
        "Description": "Seguir el sendero que baja hacia un pueblo.",
        "Resolution_Answer": "El pueblo parece tranquilo, pero demasiado silencioso.\nAl entrar, las puertas se cierran de golpe.\nFinalmente, te das cuenta de que es una trampa y el héroe cae derrotado\n",
        "NextStep_Adventure": 701
    },
    (207, 103): {
        "Description": "Abrir el cofre.",
        "Resolution_Answer": "Abres el cofre y resulta estar maldito,\nEl cofre cobra vida y acaba con el héroe\n",
        "NextStep_Adventure": 701
    },
    (208, 103): {
        "Description": "Ignorarlo y seguir avanzando.",
        "Resolution_Answer": "Más adelante, encuentras una espada antigua que te protege de la oscuridad.\nDe esta manera, consigues tu objetivo y sales victorioso de la cueva\n",
        "NextStep_Adventure": 703
    },
    (209, 103): {
        "Description": "Salir de la cueva inmediatamente.",
        "Resolution_Answer": "Al intentar salir de la cueva, te pierdes en el bosque.\nNo consigues encontrar el camino de vuelta al bosque.\nHas fracasado en tu misión y no has encontrado la espada\n",
        "NextStep_Adventure": 702
    }
}

