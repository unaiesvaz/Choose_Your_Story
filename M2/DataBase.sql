/*M!999999\- enable the sandbox mode */
-- MariaDB dump 10.19  Distrib 10.6.22-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: choose_your_story
-- ------------------------------------------------------
-- Server version       10.6.22-MariaDB-0ubuntu0.22.04.1
CREATE DATABASE IF NOT EXISTS `choose_your_story`;
USE `choose_your_story`;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `adventure_characters`
--

DROP TABLE IF EXISTS `adventure_characters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `adventure_characters` (
  `id_adventure` int(10) unsigned NOT NULL,
  `id_character` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id_adventure`,`id_character`),
  KEY `id_character` (`id_character`),
  CONSTRAINT `adventure_characters_ibfk_1` FOREIGN KEY (`id_adventure`) REFERENCES `adventures` (`id_adventure`),
  CONSTRAINT `adventure_characters_ibfk_2` FOREIGN KEY (`id_character`) REFERENCES `characters` (`id_character`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adventure_characters`
--

LOCK TABLES `adventure_characters` WRITE;
/*!40000 ALTER TABLE `adventure_characters` DISABLE KEYS */;
INSERT INTO `adventure_characters` VALUES (1,1),(1,2),(2,3),(2,4),(3,5);
/*!40000 ALTER TABLE `adventure_characters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adventure_steps`
--

DROP TABLE IF EXISTS `adventure_steps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `adventure_steps` (
  `id_step` int(10) unsigned NOT NULL,
  `description` text NOT NULL,
  `is_final_step` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id_step`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adventure_steps`
--

LOCK TABLES `adventure_steps` WRITE;
/*!40000 ALTER TABLE `adventure_steps` DISABLE KEYS */;
INSERT INTO `adventure_steps` VALUES (101,'Mientras caminas por un sendero del bosque, escuchas un llanto.\nEntre los árboles ves a un niño llorando, solo y asustado.\n¿Qué debería hacer el héroe?',0),(102,'Llegas a una encrucijada:',0),(103,'Dentro de la cueva encuentras un antiguo cofre.\n¿Qué deberías hacer?',0),(301,'Mientras caminas por un bosque, ves a un niño llorando junto al camino.\n¿Qué debería hacer el héroe?',0),(302,'Llegas a una encrucijada:\nEl camino se divide en tres direcciones.',0),(303,'Dentro de la cueva encuentras un cofre antiguo.\n¿Qué deberías hacer?',0),(501,'Durante la patrulla, Kael ve a una mujer herida sentada al borde del camino.\n¿Qué debería hacer el héroe?',0),(502,'Kael llega a una zona peligrosa y debe elegir cómo actuar.',0),(503,'Era una emboscada. El guardián es derrotado.',1),(504,'Kael ignora la amenaza y la ciudad es atacada. Falla en su misión.',1),(505,'Kael cae en una trampa mortal.',1),(506,'La ciudad se prepara a tiempo y logra defenderse. Kael salva Eldoria.',1),(507,'Kael sobrevive, pero la amenaza continúa.',1),(701,'Has muerto. FIN.',1),(702,'Tu historia acaba aquí.\nNo has encontrado la espada pero sigues con vida',1),(703,'Consigues salir del bosque con la espada.\nHas conseguido tu objetivo y salido con vida\nFelicidades!',1),(704,'Era una trampa. El héroe es derrotado.',1),(705,'El héroe queda atrapado y no puede continuar su misión.',1),(706,'Encuentras una espada antigua que te prepara para futuras aventuras.',1),(707,'El héroe sobrevive, pero abandona su misión.',1);
/*!40000 ALTER TABLE `adventure_steps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adventures`
--

DROP TABLE IF EXISTS `adventures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `adventures` (
  `id_adventure` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `id_initial_step` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`id_adventure`),
  KEY `id_initial_step` (`id_initial_step`),
  CONSTRAINT `adventures_ibfk_1` FOREIGN KEY (`id_initial_step`) REFERENCES `adventure_steps` (`id_step`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adventures`
--

LOCK TABLES `adventures` WRITE;
/*!40000 ALTER TABLE `adventures` DISABLE KEYS */;
INSERT INTO `adventures` VALUES (1,'El héroe y su espada','Esta historia trata sobre un héroe en busca de una antigua espada...',101),(2,'El héroe y sus decisiones','En el reino de Lunaria, la paz se ha visto amenazada por sucesos extraños.\nUn joven héroe llamado {} decide salir de su aldea para ayudar y descubrir qué está ocurriendo.\nEn su camino, cada decisión puede cambiar su destino.',301),(3,'La decisión del guardián','En una ciudad amurallada llamada Eldoria, los caminos exteriores se han vuelto peligrosos.\n\nUn guardián llamado Kael recibe la misión de patrullar los alrededores y proteger a los viajeros.\n\nCada decisión que tome puede salvar vidas… o acabar con la suya.\n\n\nKael, guardián de la ciudad de Eldoria, debe tomar decisiones difíciles mientras protege los caminos exteriores.\n\nDurante su patrulla se enfrenta a engaños, trampas y situaciones en las que confiar o no confiar puede marcar la diferencia.\n\nA lo largo de su misión, Kael aprende que la prudencia y la responsabilidad son tan importantes como la valentía,\n\ny que cada decisión tiene consecuencias que afectan no solo a su destino, sino también al de la ciudad que juró proteger.',501);
/*!40000 ALTER TABLE `adventures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `characters`
--

DROP TABLE IF EXISTS `characters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `characters` (
  `id_character` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id_character`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `characters`
--

LOCK TABLES `characters` WRITE;
/*!40000 ALTER TABLE `characters` DISABLE KEYS */;
INSERT INTO `characters` VALUES (1,'Joselito'),(2,'Juan el superheroe'),(3,'Ardan'),(4,'Halfdan'),(5,'Kael');
/*!40000 ALTER TABLE `characters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `id_game` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `id_user` int(10) unsigned DEFAULT NULL,
  `id_character` int(10) unsigned DEFAULT NULL,
  `id_adventure` int(10) unsigned DEFAULT NULL,
  `current_step` text DEFAULT NULL,
  `game_date` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id_game`),
  KEY `id_user` (`id_user`),
  KEY `id_character` (`id_character`),
  KEY `id_adventure` (`id_adventure`),
  CONSTRAINT `games_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`),
  CONSTRAINT `games_ibfk_2` FOREIGN KEY (`id_character`) REFERENCES `characters` (`id_character`),
  CONSTRAINT `games_ibfk_3` FOREIGN KEY (`id_adventure`) REFERENCES `adventures` (`id_adventure`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (3,1,2,1,'[203, 205, 207]','2026-01-20 19:07:09'),(4,1,1,1,'[201]','2026-01-20 19:48:08'),(5,1,1,1,'[203, 205, 208]','2026-01-20 19:49:22'),(6,4,4,2,'[302]','2026-01-20 23:41:34'),(7,1,2,1,'[203, 205, 207]','2026-01-21 15:08:42'),(9,14,4,2,'[302]','2026-01-21 15:39:45'),(11,16,5,3,'[501]','2026-01-21 18:58:04'),(12,16,3,2,'[303, 306]','2026-01-21 18:59:36'),(13,16,4,2,'[303, 306]','2026-01-21 19:02:19'),(14,16,4,2,'[301]','2026-01-21 19:03:44'),(15,16,2,1,'[202]','2026-01-21 19:04:11'),(16,16,2,1,'[202]','2026-01-21 19:04:23'),(17,16,5,3,'[502]','2026-01-21 19:05:44'),(18,1,4,2,'[302]','2026-01-21 19:35:49');
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb3_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_AUTO_VALUE_ON_ZERO' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `increment_games_played` AFTER INSERT ON `games` FOR EACH ROW BEGIN
    UPDATE users
    SET games_played = games_played + 1
    WHERE id_user = NEW.id_user;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `step_answers`
--

DROP TABLE IF EXISTS `step_answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `step_answers` (
  `id_answer` int(10) unsigned NOT NULL,
  `id_current_step` int(10) unsigned DEFAULT NULL,
  `answer_text` text NOT NULL,
  `resolution_text` text DEFAULT NULL,
  `id_next_step` int(10) unsigned DEFAULT NULL,
  `times_reached` int(10) unsigned DEFAULT 0,
  PRIMARY KEY (`id_answer`),
  KEY `id_current_step` (`id_current_step`),
  KEY `id_next_step` (`id_next_step`),
  CONSTRAINT `step_answers_ibfk_1` FOREIGN KEY (`id_current_step`) REFERENCES `adventure_steps` (`id_step`),
  CONSTRAINT `step_answers_ibfk_2` FOREIGN KEY (`id_next_step`) REFERENCES `adventure_steps` (`id_step`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `step_answers`
--

LOCK TABLES `step_answers` WRITE;
/*!40000 ALTER TABLE `step_answers` DISABLE KEYS */;
INSERT INTO `step_answers` VALUES (201,101,'Acercarse al niño para ayudarlo.','Cuando te aproximas, el niño levanta la cabeza… y sonríe.\nDe repente, se transforma en una criatura oscura que te ataca por sorpresa.\nNo tienes tiempo de reaccionar.\nEra una trampa. El héroe cae en el bosque y su historia termina aquí.',701,2),(202,101,'Ignorar al niño y seguir el camino.','Sigues caminando, pero el llanto se vuelve más fuerte.\nDe pronto, el suelo bajo tus pies cede y caes en un foso oculto.\nLa culpa te distrajo. El héroe queda atrapado sin salida.',701,2),(203,101,'Esconderse y observar desde la distancia.','Notas algo extraño: el niño no deja huellas en el suelo.\nDecides no acercarte y rodeas la zona con cuidado.\nMás adelante, el camino se divide en tres.',102,3),(204,102,'Tomar el camino de la montaña.','El camino es peligroso y resbaladizo. Una tormenta comienza de repente.\nUn rayo cae cerca y pierdes el equilibrio.\nEl héroe cae por el acantilado.',701,0),(205,102,'Entrar en una cueva oscura.','Al entrar a la cueva, te encuentras un antiguo cofre\n¿Qué deberías hacer?',103,3),(206,102,'Seguir el sendero que baja hacia un pueblo.','El pueblo parece tranquilo, pero demasiado silencioso.\nAl entrar, las puertas se cierran de golpe.\nFinalmente, te das cuenta de que es una trampa y el héroe cae derrotado',701,0),(207,103,'Abrir el cofre.','Abres el cofre y resulta estar maldito,\nEl cofre cobra vida y acaba con el héroe',701,2),(208,103,'Ignorarlo y seguir avanzando.','Más adelante, encuentras una espada antigua que te protege de la oscuridad.\nDe esta manera, consigues tu objetivo y sales victorioso de la cueva',703,1),(209,103,'Salir de la cueva inmediatamente.','Al intentar salir de la cueva, te pierdes en el bosque.\nNo consigues encontrar el camino de vuelta al bosque.\nHas fracasado en tu misión y no has encontrado la espada',702,0),(301,301,'Acercarse para ayudar al niño.','El niño deja de llorar y se transforma en una criatura que ataca al héroe por sorpresa.',704,1),(302,301,'Ignorar al niño y seguir caminando.','Sigues tu camino, pero caes en una trampa escondida en el suelo.',705,3),(303,301,'Observar al niño desde lejos.','Notas que algo no es normal y decides rodear la zona con cuidado.\nMás adelante llegas a una encrucijada.',302,2),(304,302,'Entrar en una cueva oscura.','Entras en la cueva y encuentras un cofre antiguo.',303,0),(305,302,'Subir por el camino de la montaña.','El camino es peligroso y el clima empeora.\nResbalas y caes por el acantilado.',704,0),(306,302,'Ir hacia un pequeño pueblo cercano.','El pueblo parece vacío, pero tranquilo.\nEncuentras refugio y ayuda, completando tu misión con éxito.',706,2),(307,303,'Abrir el cofre.','El cofre estaba maldito y acaba con el héroe.',704,0),(308,303,'Ignorarlo y avanzar.','Encuentras una espada antigua que te prepara para futuras aventuras.',706,0),(309,303,'Salir de la cueva.','Decides abandonar la cueva.\nEl héroe sobrevive, pero abandona su misión.',707,0),(501,501,'Acercarse rápidamente para ayudarla.','Cuando Kael se inclina para ayudarla, varios bandidos salen de su escondite.',503,1),(502,501,'Ignorarla y seguir patrullando.','Kael sigue su camino, pero más adelante la ciudad es atacada por los mismos bandidos.',504,2),(503,501,'Hablarle desde lejos y observar con cuidado.','Kael nota movimientos extraños entre los árboles y decide no bajar la guardia.',502,0),(504,502,'Perseguir a los bandidos.','Los bandidos conducen a Kael hacia un terreno peligroso.',503,0),(505,502,'Regresar a la ciudad para avisar.','La ciudad se prepara a tiempo y logra defenderse.',505,0),(506,502,'Esconderse y esperar refuerzos.','Los refuerzos nunca llegan y el peligro se extiende.',506,0);
/*!40000 ALTER TABLE `step_answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id_user` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(10) NOT NULL,
  `password` varchar(45) NOT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `games_played` int(10) unsigned DEFAULT 0,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Unai','1234','2026-01-17 22:54:17',8),(3,'Jose','prueba1234','2026-01-18 20:05:45',0),(4,'Pepe','prueba2343','2026-01-18 20:10:39',1),(5,'rayan','12345678','2026-01-19 18:48:49',0),(6,'aitor09','200609Aa#','2026-01-20 20:23:06',0),(7,'aitormera','123456789','2026-01-20 20:28:00',0),(8,'aitor0099','123456789','2026-01-20 20:31:56',0),(9,'aitorrr','123456789','2026-01-20 20:33:51',0),(10,'User-prue','pruebacont','2026-01-21 15:18:45',0),(11,'prubidus','pass2134_','2026-01-21 15:33:55',0),(12,'uprueba34','coanfioahf','2026-01-21 15:35:45',0),(13,'userproba','contrasne','2026-01-21 15:37:58',0),(14,'unaiesvaz','unaiesvaz21','2026-01-21 15:38:48',1),(15,'123231132','12345678L.','2026-01-21 18:53:26',0),(16,'Joseliooo','123123123L.','2026-01-21 18:57:15',7),(17,'manuela','1234567S.','2026-01-21 19:00:14',0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
