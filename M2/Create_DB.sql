CREATE DATABASE IF NOT EXISTS choose_your_story;
USE choose_your_story;

CREATE TABLE users (
    id_users INT UNSIGNED,
    username VARCHAR(10),
    password VARCHAR(45),
    data_alta DATETIME,
    usuari_alta VARCHAR(50),
    data_mod DATETIME,
    usuari_mod VARCHAR(50)
);

CREATE TABLE characters (
    id_characters INT UNSIGNED,
    characterName VARCHAR(45),
    description VARCHAR(2000),
    data_alta DATETIME,
    usuari_alta VARCHAR(50),
    data_mod DATETIME,
    usuari_mod VARCHAR(50)
);

CREATE TABLE adventures (
    id_adventures INT UNSIGNED,
    name VARCHAR(100),
    description VARCHAR(2000),
    data_alta DATETIME,
    usuari_alta VARCHAR(50),
    data_mod DATETIME,
    usuari_mod VARCHAR(50)
);

CREATE TABLE adventure_characters (
    id_adventure_characters INT UNSIGNED,
    id_adventures INT UNSIGNED,
    id_characters INT UNSIGNED,
    data_alta DATETIME,
    usuari_alta VARCHAR(50),
    data_mod DATETIME,
    usuari_mod VARCHAR(50)
);

CREATE TABLE adventure_steps (
    id_adventure_steps INT UNSIGNED,
    id_adventures INT UNSIGNED,
    description VARCHAR(4000),
    isFinal TINYINT,
    data_alta DATETIME,
    usuari_alta VARCHAR(50),
    data_mod DATETIME,
    usuari_mod VARCHAR(50)
);

CREATE TABLE step_answers (
    id_step_answers INT UNSIGNED,
    id_adventure_steps INT UNSIGNED,
    answerText VARCHAR(2000),
    id_next_step INT UNSIGNED,
    data_alta DATETIME,
    usuari_alta VARCHAR(50),
    data_mod DATETIME,
    usuari_mod VARCHAR(50)
);

CREATE TABLE games (
    id_games INT UNSIGNED,
    id_users INT UNSIGNED,
    id_characters INT UNSIGNED,
    id_adventures INT UNSIGNED,
    gameDate DATETIME,
    data_alta DATETIME,
    usuari_alta VARCHAR(50),
    data_mod DATETIME,
    usuari_mod VARCHAR(50)
);

CREATE TABLE game_choices (
    id_game_choices INT UNSIGNED,
    id_games INT UNSIGNED,
    id_adventure_steps INT UNSIGNED,
    id_step_answers INT UNSIGNED,
    data_alta DATETIME,
    usuari_alta VARCHAR(50),
    data_mod DATETIME,
    usuari_mod VARCHAR(50)
);
