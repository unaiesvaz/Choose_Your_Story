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
        "Name": "El heroe",
        "Description":"Esta historia trata sobre un heroe",
        "characters": [1,2]
    }
}
id_by_steps = {
    101: {
        "Description": "Mientras caminas por un sendero del bosque, escuchas un llanto.\nEntre los árboles ves a un niño llorando, solo y asustado.\n¿Qué debería hacer el héroe?\n",
        "answers_in_step": (201, 202, 203),
        "Final_Step": 0
    },
    301: {
        "Description": "Has muerto. FIN.",
        "answers_in_step": (),
        "Final_Step": 1
    },
    302: {
        "Description": "Has salvado al niño. FIN.",
        "answers_in_step": (),
        "Final_Step": 1
    },
    103: {
        "Description": "Sigues caminando por el bosque...",
        "answers_in_step": (401,),
        "Final_Step": 0
    }
}


idAnswers_ByStep_Adventure = {
    201: {
        "Description": "Acercarse al niño para ayudarlo.",
        "Resolution_Answer": "Cuando te aproximas, el niño levanta la cabeza… y sonríe.\nDe repente, se transforma en una criatura oscura que te ataca por sorpresa.\nNo tienes tiempo de reaccionar.\nEra una trampa. El héroe cae en el bosque y su historia termina aquí.\n",
        "NextStep_Adventure": 0
    },
    202: {
        "Description": "Ignorar al niño y seguir el camino.",
        "Resolution_Answer": "Sigues caminando, pero el llanto se vuelve más fuerte.\nDe pronto, el suelo bajo tus pies cede y caes en un foso oculto.\nLa culpa te distrajo. El héroe queda atrapado sin salida.\n",
        "NextStep_Adventure": 0
    },
    203: {
        "Description": "Esconderse y observar desde la distancia.",
        "Resolution_Answer": "Notas algo extraño: el niño no deja huellas en el suelo.\nDecides no acercarte y rodeas la zona con cuidado.\nMás adelante, el camino se divide en tres.\n",
        "NextStep_Adventure": 103
    }
}

