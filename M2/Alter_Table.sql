USE choose_your_story;

-- 1. Definir PKs i AutoIncrement (Així evitem l'error 1075)
ALTER TABLE users MODIFY id_users INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE characters MODIFY id_characters INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE adventures MODIFY id_adventures INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE adventure_characters MODIFY id_adventure_characters INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE adventure_steps MODIFY id_adventure_steps INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE step_answers MODIFY id_step_answers INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE games MODIFY id_games INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;
ALTER TABLE game_choices MODIFY id_game_choices INT UNSIGNED AUTO_INCREMENT PRIMARY KEY;

-- 2. Restriccions NOT NULL i DEFAULT per auditoria
ALTER TABLE users 
    MODIFY username VARCHAR(10) NOT NULL UNIQUE,
    MODIFY password VARCHAR(45) NOT NULL,
    MODIFY data_alta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    MODIFY usuari_alta VARCHAR(50) NOT NULL;

ALTER TABLE characters 
    MODIFY characterName VARCHAR(45) NOT NULL UNIQUE,
    MODIFY description VARCHAR(2000) NOT NULL,
    MODIFY data_alta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    MODIFY usuari_alta VARCHAR(50) NOT NULL;

ALTER TABLE adventures 
    MODIFY name VARCHAR(100) NOT NULL,
    MODIFY data_alta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    MODIFY usuari_alta VARCHAR(50) NOT NULL;

ALTER TABLE adventure_steps 
    MODIFY data_alta DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    MODIFY usuari_alta VARCHAR(50) NOT NULL,
    MODIFY isFinal TINYINT DEFAULT 0;

-- 3. Definir FKs (Nomenclatura: fk_taula1_taula2)
ALTER TABLE adventure_characters 
    ADD CONSTRAINT fk_adventure_characters_adventures FOREIGN KEY (id_adventures) REFERENCES adventures(id_adventures),
    ADD CONSTRAINT fk_adventure_characters_characters FOREIGN KEY (id_characters) REFERENCES characters(id_characters);

ALTER TABLE adventure_steps 
    ADD CONSTRAINT fk_adventure_steps_adventures FOREIGN KEY (id_adventures) REFERENCES adventures(id_adventures);

ALTER TABLE step_answers 
    ADD CONSTRAINT fk_step_answers_adventure_steps FOREIGN KEY (id_adventure_steps) REFERENCES adventure_steps(id_adventure_steps),
    ADD CONSTRAINT fk_step_answers_adventure_steps_next FOREIGN KEY (id_next_step) REFERENCES adventure_steps(id_adventure_steps);

ALTER TABLE games 
    ADD CONSTRAINT fk_games_users FOREIGN KEY (id_users) REFERENCES users(id_users),
    ADD CONSTRAINT fk_games_characters FOREIGN KEY (id_characters) REFERENCES characters(id_characters),
    ADD CONSTRAINT fk_games_adventures FOREIGN KEY (id_adventures) REFERENCES adventures(id_adventures);

ALTER TABLE game_choices 
    ADD CONSTRAINT fk_game_choices_games FOREIGN KEY (id_games) REFERENCES games(id_games),
    ADD CONSTRAINT fk_game_choices_adventure_steps FOREIGN KEY (id_adventure_steps) REFERENCES adventure_steps(id_adventure_steps),
    ADD CONSTRAINT fk_game_choices_step_answers FOREIGN KEY (id_step_answers) REFERENCES step_answers(id_step_answers);
