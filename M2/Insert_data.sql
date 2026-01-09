USE choose_your_story;

-- Usuari
INSERT INTO users (username, password, usuari_alta) VALUES ('Rafa', '1234', 'SISTEMA');

-- Personatges
INSERT INTO characters (characterName, description, usuari_alta) VALUES 
('Beowulf', 'Heroi llegendari gauta.', 'SISTEMA'),
('Pato Lucas', 'Ànec amb molta mala sort.', 'SISTEMA');

-- Aventures
INSERT INTO adventures (name, description, usuari_alta) VALUES 
('La matanza de Texas', 'Terror en estat pur.', 'SISTEMA');

-- Relació Personatge-Aventura (N:M)
INSERT INTO adventure_characters (id_adventures, id_characters, usuari_alta) VALUES (1, 1, 'SISTEMA'), (1, 2, 'SISTEMA');

-- Passos
INSERT INTO adventure_steps (id_adventures, description, isFinal, usuari_alta) VALUES 
(1, 'Entres al bosc i veus una cabana. Què fas?', 0, 'SISTEMA'), -- ID 1
(1, 'Dins la cabana hi ha un boig. Has mort.', 1, 'SISTEMA'),    -- ID 2
(1, 'Fuges del bosc i sobrevius.', 1, 'SISTEMA');               -- ID 3

-- Respostes
INSERT INTO step_answers (id_adventure_steps, answerText, id_next_step, usuari_alta) VALUES 
(1, 'Entrar a la cabana', 2, 'SISTEMA'),
(1, 'Sortir corrent', 3, 'SISTEMA');
