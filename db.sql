

DROP TABLE IF EXISTS `alumno_alumno`;

CREATE TABLE `alumno_alumno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alumno_id` int(11) NOT NULL,
  `sexo` varchar(20) DEFAULT NULL,
  `curp` varchar(20) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `localidad` varchar(30) DEFAULT NULL,
  `municipio` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `dia` varchar(20) DEFAULT NULL,
  `telefono` varchar(20) DEFAULT NULL,
  `grupo_id` int(11) DEFAULT NULL,
  `tutor_id` int(11) DEFAULT NULL,
  `horario_id` int(11) DEFAULT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alumno_id` (`alumno_id`),
  KEY `alumno_alumno_cbe01404` (`grupo_id`),
  KEY `alumno_alumno_3eab0ada` (`tutor_id`),
  KEY `alumno_alumno_6e64cd21` (`horario_id`),
  CONSTRAINT `grupo_id_refs_id_88bbda16` FOREIGN KEY (`grupo_id`) REFERENCES `grupo_grupo` (`id`),
  CONSTRAINT `horario_id_refs_id_8f0d0aab` FOREIGN KEY (`horario_id`) REFERENCES `horario_horario` (`id`),
  CONSTRAINT `tutor_id_refs_id_1c918335` FOREIGN KEY (`tutor_id`) REFERENCES `tutor_tutor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno_alumno`
--

LOCK TABLES `alumno_alumno` WRITE;
/*!40000 ALTER TABLE `alumno_alumno` DISABLE KEYS */;
INSERT INTO `alumno_alumno` VALUES (1,6,'Hombre','3044309jj3r3jr','2014-11-13','pitzocali','ixhuatlan','alex@alex.com','lunes','4655756765',2,2,2,0),(2,7,'Hombre','66546456','2014-11-17','cacahuatengo','ixhuatlan','alex@alex.com','martes','2123144354',2,1,2,1);
/*!40000 ALTER TABLE `alumno_alumno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alumno_alumno_materias`
--

DROP TABLE IF EXISTS `alumno_alumno_materias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alumno_alumno_materias` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alumno_id` int(11) NOT NULL,
  `materia_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alumno_id` (`alumno_id`,`materia_id`),
  KEY `alumno_alumno_materias_fcd07de9` (`alumno_id`),
  KEY `alumno_alumno_materias_ce3d2f7b` (`materia_id`),
  CONSTRAINT `alumno_id_refs_id_12b49f96` FOREIGN KEY (`alumno_id`) REFERENCES `alumno_alumno` (`id`),
  CONSTRAINT `materia_id_refs_id_9170dfa6` FOREIGN KEY (`materia_id`) REFERENCES `materia_materia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno_alumno_materias`
--

LOCK TABLES `alumno_alumno_materias` WRITE;
/*!40000 ALTER TABLE `alumno_alumno_materias` DISABLE KEYS */;
INSERT INTO `alumno_alumno_materias` VALUES (3,1,3),(4,1,5),(5,2,1);
/*!40000 ALTER TABLE `alumno_alumno_materias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alumno_alumno_semestre`
--

DROP TABLE IF EXISTS `alumno_alumno_semestre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alumno_alumno_semestre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alumno_id` int(11) NOT NULL,
  `semestre_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `alumno_id` (`alumno_id`,`semestre_id`),
  KEY `alumno_alumno_semestre_fcd07de9` (`alumno_id`),
  KEY `alumno_alumno_semestre_cf648163` (`semestre_id`),
  CONSTRAINT `alumno_id_refs_id_0b74503a` FOREIGN KEY (`alumno_id`) REFERENCES `alumno_alumno` (`id`),
  CONSTRAINT `semestre_id_refs_id_14a9ab2d` FOREIGN KEY (`semestre_id`) REFERENCES `semestre_semestre` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alumno_alumno_semestre`
--

LOCK TABLES `alumno_alumno_semestre` WRITE;
/*!40000 ALTER TABLE `alumno_alumno_semestre` DISABLE KEYS */;
INSERT INTO `alumno_alumno_semestre` VALUES (2,1,1),(3,1,2),(4,2,3);
/*!40000 ALTER TABLE `alumno_alumno_semestre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asistencia_alumno_asistencia_alumno`
--

DROP TABLE IF EXISTS `asistencia_alumno_asistencia_alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asistencia_alumno_asistencia_alumno` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `empleado_id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `asistencia_alumno_asistencia_alumno_060bf3b5` (`empleado_id`),
  CONSTRAINT `empleado_id_refs_id_388a715a` FOREIGN KEY (`empleado_id`) REFERENCES `empleado_empleado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencia_alumno_asistencia_alumno`
--

LOCK TABLES `asistencia_alumno_asistencia_alumno` WRITE;
/*!40000 ALTER TABLE `asistencia_alumno_asistencia_alumno` DISABLE KEYS */;
INSERT INTO `asistencia_alumno_asistencia_alumno` VALUES (1,1,'2014-11-18',1),(2,1,'2014-11-14',1),(3,1,'2014-11-14',1);
/*!40000 ALTER TABLE `asistencia_alumno_asistencia_alumno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asistencia_alumno_asistencia_alumno_alumnos`
--

DROP TABLE IF EXISTS `asistencia_alumno_asistencia_alumno_alumnos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asistencia_alumno_asistencia_alumno_alumnos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asistencia_alumno_id` int(11) NOT NULL,
  `alumno_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `asistencia_alumno_id` (`asistencia_alumno_id`,`alumno_id`),
  KEY `asistencia_alumno_asistencia_alumno_alumnos_f29e6b9a` (`asistencia_alumno_id`),
  KEY `asistencia_alumno_asistencia_alumno_alumnos_fcd07de9` (`alumno_id`),
  CONSTRAINT `alumno_id_refs_id_ba7f1bbe` FOREIGN KEY (`alumno_id`) REFERENCES `alumno_alumno` (`id`),
  CONSTRAINT `asistencia_alumno_id_refs_id_28f34641` FOREIGN KEY (`asistencia_alumno_id`) REFERENCES `asistencia_alumno_asistencia_alumno` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencia_alumno_asistencia_alumno_alumnos`
--

LOCK TABLES `asistencia_alumno_asistencia_alumno_alumnos` WRITE;
/*!40000 ALTER TABLE `asistencia_alumno_asistencia_alumno_alumnos` DISABLE KEYS */;
INSERT INTO `asistencia_alumno_asistencia_alumno_alumnos` VALUES (5,1,1),(4,3,2);
/*!40000 ALTER TABLE `asistencia_alumno_asistencia_alumno_alumnos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asistencia_empleado_asistencia_empleado`
--

DROP TABLE IF EXISTS `asistencia_empleado_asistencia_empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asistencia_empleado_asistencia_empleado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hora_entrada` time NOT NULL,
  `hora_salida` time NOT NULL,
  `fecha` date NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencia_empleado_asistencia_empleado`
--

LOCK TABLES `asistencia_empleado_asistencia_empleado` WRITE;
/*!40000 ALTER TABLE `asistencia_empleado_asistencia_empleado` DISABLE KEYS */;
INSERT INTO `asistencia_empleado_asistencia_empleado` VALUES (1,'03:35:13','06:58:22','2014-11-14',1),(2,'05:53:12','06:58:22','2013-11-05',1);
/*!40000 ALTER TABLE `asistencia_empleado_asistencia_empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asistencia_empleado_asistencia_empleado_empleados`
--

DROP TABLE IF EXISTS `asistencia_empleado_asistencia_empleado_empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asistencia_empleado_asistencia_empleado_empleados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asistencia_empleado_id` int(11) NOT NULL,
  `empleado_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `asistencia_empleado_id` (`asistencia_empleado_id`,`empleado_id`),
  KEY `asistencia_empleado_asistencia_empleado_empleados_254fee92` (`asistencia_empleado_id`),
  KEY `asistencia_empleado_asistencia_empleado_empleados_060bf3b5` (`empleado_id`),
  CONSTRAINT `asistencia_empleado_id_refs_id_94cd466d` FOREIGN KEY (`asistencia_empleado_id`) REFERENCES `asistencia_empleado_asistencia_empleado` (`id`),
  CONSTRAINT `empleado_id_refs_id_df4a5c5f` FOREIGN KEY (`empleado_id`) REFERENCES `empleado_empleado` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asistencia_empleado_asistencia_empleado_empleados`
--

LOCK TABLES `asistencia_empleado_asistencia_empleado_empleados` WRITE;
/*!40000 ALTER TABLE `asistencia_empleado_asistencia_empleado_empleados` DISABLE KEYS */;
INSERT INTO `asistencia_empleado_asistencia_empleado_empleados` VALUES (1,1,1),(5,2,1),(6,2,2),(7,2,3);
/*!40000 ALTER TABLE `asistencia_empleado_asistencia_empleado_empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add asistencia_alumno',7,'add_asistencia_alumno'),(20,'Can change asistencia_alumno',7,'change_asistencia_alumno'),(21,'Can delete asistencia_alumno',7,'delete_asistencia_alumno'),(22,'Can add asistencia_empleado',8,'add_asistencia_empleado'),(23,'Can change asistencia_empleado',8,'change_asistencia_empleado'),(24,'Can delete asistencia_empleado',8,'delete_asistencia_empleado'),(25,'Can add concepto_pago',9,'add_concepto_pago'),(26,'Can change concepto_pago',9,'change_concepto_pago'),(27,'Can delete concepto_pago',9,'delete_concepto_pago'),(28,'Can add empleado',10,'add_empleado'),(29,'Can change empleado',10,'change_empleado'),(30,'Can delete empleado',10,'delete_empleado'),(31,'Can add alumno',11,'add_alumno'),(32,'Can change alumno',11,'change_alumno'),(33,'Can delete alumno',11,'delete_alumno'),(34,'Can add grupo',12,'add_grupo'),(35,'Can change grupo',12,'change_grupo'),(36,'Can delete grupo',12,'delete_grupo'),(37,'Can add pago',13,'add_pago'),(38,'Can change pago',13,'change_pago'),(39,'Can delete pago',13,'delete_pago'),(40,'Can add nomina',14,'add_nomina'),(41,'Can change nomina',14,'change_nomina'),(42,'Can delete nomina',14,'delete_nomina'),(43,'Can add horario',15,'add_horario'),(44,'Can change horario',15,'change_horario'),(45,'Can delete horario',15,'delete_horario'),(46,'Can add materia',16,'add_materia'),(47,'Can change materia',16,'change_materia'),(48,'Can delete materia',16,'delete_materia'),(49,'Can add perfil',17,'add_perfil'),(50,'Can change perfil',17,'change_perfil'),(51,'Can delete perfil',17,'delete_perfil'),(52,'Can add semestre',18,'add_semestre'),(53,'Can change semestre',18,'change_semestre'),(54,'Can delete semestre',18,'delete_semestre'),(55,'Can add tutor',19,'add_tutor'),(56,'Can change tutor',19,'change_tutor'),(57,'Can delete tutor',19,'delete_tutor'),(58,'Can add observacion',20,'add_observacion'),(59,'Can change observacion',20,'change_observacion'),(60,'Can delete observacion',20,'delete_observacion'),(61,'Can add calificacion',21,'add_calificacion'),(62,'Can change calificacion',21,'change_calificacion'),(63,'Can delete calificacion',21,'delete_calificacion');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$12rvb8eynyi5$7ADb7xh+5KNHc+sbMNHV7DvJHrczoeGiozp+MCpykvs=','2014-11-18 06:58:08',1,'root','','','',1,1,'2014-11-17 04:35:47'),(2,'pbkdf2_sha256$12000$tFaNhcN5EweG$RMvM5sOfnoeDmjs0VgLhQ9FAgZUGGuREuM/V3yvbsNQ=','2014-11-17 06:41:15',0,'mario','mario alberto','hernandez hernandez','',1,1,'2014-11-17 06:41:15'),(4,'pbkdf2_sha256$12000$omxu0QPenRWY$MdntF7vA/uUWS4J+2asm2ypPkiXgwxXom05YsABLycE=','2014-11-17 06:50:03',0,'fredy','Alfredo Santiago','Hernandes','',0,1,'2014-11-17 06:50:03'),(5,'pbkdf2_sha256$12000$Pi7I8FcIAN5f$GlSSVpXsdUqpFkE5orJAr+yJWM4rzSn/9ny5pWTrn1c=','2014-11-17 06:53:20',0,'linux','Linus ','Torvals','',0,1,'2014-11-17 06:53:20'),(6,'pbkdf2_sha256$12000$MMhIYXiQnN22$Fgnr/QJJvYjTcpDNOQwdMW5YVNOjEIOj+Tc0y7YEyY8=','2014-11-17 06:57:12',0,'alex','Alejandro','Martinez Cabrera','',0,1,'2014-11-17 06:57:12'),(7,'pbkdf2_sha256$12000$GGTwH6faAqmJ$OhK47To/p6X52gr+eQ9PIXq9NBLlvrfHr26OGd3LYMc=','2014-11-17 07:15:41',0,'ali','ali','','',0,1,'2014-11-17 07:15:41');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calificacion_calificacion`
--

DROP TABLE IF EXISTS `calificacion_calificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calificacion_calificacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alumno_id` int(11) NOT NULL,
  `materia_id` int(11) NOT NULL,
  `calificacion` double NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `semestre_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `calificacion_calificacion_fcd07de9` (`alumno_id`),
  KEY `calificacion_calificacion_ce3d2f7b` (`materia_id`),
  KEY `calificacion_calificacion_cf648163` (`semestre_id`),
  CONSTRAINT `alumno_id_refs_id_9fd1754d` FOREIGN KEY (`alumno_id`) REFERENCES `alumno_alumno` (`id`),
  CONSTRAINT `materia_id_refs_id_affb5fea` FOREIGN KEY (`materia_id`) REFERENCES `materia_materia` (`id`),
  CONSTRAINT `semestre_id_refs_id_fc7f6cee` FOREIGN KEY (`semestre_id`) REFERENCES `semestre_semestre` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calificacion_calificacion`
--

LOCK TABLES `calificacion_calificacion` WRITE;
/*!40000 ALTER TABLE `calificacion_calificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `calificacion_calificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `concepto_pago_concepto_pago`
--

DROP TABLE IF EXISTS `concepto_pago_concepto_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `concepto_pago_concepto_pago` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `concepto_pago_concepto_pago`
--

LOCK TABLES `concepto_pago_concepto_pago` WRITE;
/*!40000 ALTER TABLE `concepto_pago_concepto_pago` DISABLE KEYS */;
INSERT INTO `concepto_pago_concepto_pago` VALUES (1,'Inscripcion',1),(2,'Pago Semanal',1),(3,'Pago Mensual',1),(4,'Pagoo Anual',0);
/*!40000 ALTER TABLE `concepto_pago_concepto_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-11-17 06:49:43','3','fredy',3,'',4,1),(2,'2014-11-17 08:25:57','2','ali',2,'Modifica sexo,curp,fecha_nacimiento,localidad,municipio,email,dia,telefono,grupo,tutor,horario,materias,semestre y activo.',11,1),(3,'2014-11-17 08:26:47','3','Linus ',2,'Modifica activo.',10,1),(4,'2014-11-17 08:26:52','1','mario alberto',2,'Modifica activo.',10,1),(5,'2014-11-17 08:40:58','1','mario alberto',2,'Modifica activo.',10,1),(6,'2014-11-17 08:41:06','2','Alfredo Santiago',2,'No ha modificado ningún campo.',10,1),(7,'2014-11-17 08:42:28','3','Linus ',2,'Modifica activo.',10,1),(8,'2014-11-17 08:42:33','1','mario alberto',2,'Modifica activo.',10,1),(9,'2014-11-17 08:43:41','2','Alfredo Santiago',2,'Modifica activo.',10,1),(10,'2014-11-17 09:04:47','3','Linus ',2,'Modifica activo.',10,1),(11,'2014-11-17 09:04:51','2','Alfredo Santiago',2,'Modifica activo.',10,1),(12,'2014-11-17 09:04:56','1','mario alberto',2,'Modifica activo.',10,1),(13,'2014-11-18 06:58:27','1','2014-11-18',1,'',7,1),(14,'2014-11-18 07:02:29','1','2014-11-18',2,'Modifica alumnos.',7,1),(15,'2014-11-18 07:31:58','1','2014-11-18',2,'No ha modificado ningún campo.',7,1),(16,'2014-11-18 07:50:43','2','2013-11-05',2,'No ha modificado ningún campo.',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'asistencia_alumno','asistencia_alumno','asistencia_alumno'),(8,'asistencia_empleado','asistencia_empleado','asistencia_empleado'),(9,'concepto_pago','concepto_pago','concepto_pago'),(10,'empleado','empleado','empleado'),(11,'alumno','alumno','alumno'),(12,'grupo','grupo','grupo'),(13,'pago','pago','pago'),(14,'nomina','nomina','nomina'),(15,'horario','horario','horario'),(16,'materia','materia','materia'),(17,'perfil','perfil','perfil'),(18,'semestre','semestre','semestre'),(19,'tutor','tutor','tutor'),(20,'observacion','observacion','observacion'),(21,'calificacion','calificacion','calificacion');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2014-11-17 04:35:15'),(2,'auth','0001_initial','2014-11-17 04:35:18'),(3,'admin','0001_initial','2014-11-17 04:35:20'),(4,'sessions','0001_initial','2014-11-17 04:35:20'),(5,'asistencia_alumno','0001_initial','2014-11-18 07:37:00'),(6,'asistencia_alumno','0002_auto_20141118_0738','2014-11-18 07:40:35'),(7,'asistencia_alumno','0003_auto_20141118_0747','2014-11-18 07:48:17'),(8,'asistencia_empleado','0001_initial','2014-11-18 07:52:50');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1dflwogpxhkmekqb6k44s0o0v73iya4l','Y2ExNTU0OTcyZjBlOTYwMWNmYmFkNmJmMjU0YTBiNGQwZTUyODg2Zjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM4N2JmMjliNTA0MjRjYmUwNmRhNmFiYTI1ZDkyNTU5ZDJlNTc3MDciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2014-12-02 06:58:08');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleado_empleado`
--

DROP TABLE IF EXISTS `empleado_empleado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empleado_empleado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `empleado_id` int(11) NOT NULL,
  `localidad` varchar(30) DEFAULT NULL,
  `municipio` varchar(30) DEFAULT NULL,
  `telefono` varchar(30) DEFAULT NULL,
  `sexo` varchar(30) DEFAULT NULL,
  `perfil_id` int(11) DEFAULT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `empleado_empleado_060bf3b5` (`empleado_id`),
  KEY `empleado_empleado_7fdfc031` (`perfil_id`),
  CONSTRAINT `perfil_id_refs_id_7e12f974` FOREIGN KEY (`perfil_id`) REFERENCES `perfil_perfil` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleado_empleado`
--

LOCK TABLES `empleado_empleado` WRITE;
/*!40000 ALTER TABLE `empleado_empleado` DISABLE KEYS */;
INSERT INTO `empleado_empleado` VALUES (1,2,'pitzocali','ixhuatlan','83984623964','Mujer',3,1),(2,4,'cacahuatengo','ixhuatlan','6545756765','Hombre',2,1),(3,5,'Australis','Finladia','45564645','Hombre',1,1);
/*!40000 ALTER TABLE `empleado_empleado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grupo_grupo`
--

DROP TABLE IF EXISTS `grupo_grupo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grupo_grupo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grupo_grupo`
--

LOCK TABLES `grupo_grupo` WRITE;
/*!40000 ALTER TABLE `grupo_grupo` DISABLE KEYS */;
INSERT INTO `grupo_grupo` VALUES (1,'A',1),(2,'B',1),(3,'C',1),(4,'D',1),(5,'E',0);
/*!40000 ALTER TABLE `grupo_grupo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `horario_horario`
--

DROP TABLE IF EXISTS `horario_horario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `horario_horario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `horario_horario`
--

LOCK TABLES `horario_horario` WRITE;
/*!40000 ALTER TABLE `horario_horario` DISABLE KEYS */;
INSERT INTO `horario_horario` VALUES (1,'9:00 am a 12:00 pmm',1),(2,'12:00 am a  4:00 pm',0);
/*!40000 ALTER TABLE `horario_horario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materia_materia`
--

DROP TABLE IF EXISTS `materia_materia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `materia_materia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materia_materia`
--

LOCK TABLES `materia_materia` WRITE;
/*!40000 ALTER TABLE `materia_materia` DISABLE KEYS */;
INSERT INTO `materia_materia` VALUES (1,'matematicass',1),(2,'fisica',1),(3,'quimica',1),(4,'sociales',0),(5,'Informatica',1);
/*!40000 ALTER TABLE `materia_materia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nomina_nomina`
--

DROP TABLE IF EXISTS `nomina_nomina`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nomina_nomina` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `empleado_id` int(11) NOT NULL,
  `cantidad` double NOT NULL,
  `fecha` datetime NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `nomina_nomina_060bf3b5` (`empleado_id`),
  CONSTRAINT `empleado_id_refs_id_0db1fbd5` FOREIGN KEY (`empleado_id`) REFERENCES `empleado_empleado` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nomina_nomina`
--

LOCK TABLES `nomina_nomina` WRITE;
/*!40000 ALTER TABLE `nomina_nomina` DISABLE KEYS */;
/*!40000 ALTER TABLE `nomina_nomina` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `observacion_observacion`
--

DROP TABLE IF EXISTS `observacion_observacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `observacion_observacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `observacion` varchar(50) NOT NULL,
  `alumno_id` int(11) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `observacion_observacion_fcd07de9` (`alumno_id`),
  CONSTRAINT `alumno_id_refs_id_76b9a111` FOREIGN KEY (`alumno_id`) REFERENCES `alumno_alumno` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `observacion_observacion`
--

LOCK TABLES `observacion_observacion` WRITE;
/*!40000 ALTER TABLE `observacion_observacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `observacion_observacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pago_pago`
--

DROP TABLE IF EXISTS `pago_pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pago_pago` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alumno_id` int(11) NOT NULL,
  `concepto_pago_id` int(11) NOT NULL,
  `fecha` datetime NOT NULL,
  `cantidad` double NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `pago_pago_fcd07de9` (`alumno_id`),
  KEY `pago_pago_05e4add6` (`concepto_pago_id`),
  CONSTRAINT `alumno_id_refs_id_0dce6e7d` FOREIGN KEY (`alumno_id`) REFERENCES `alumno_alumno` (`id`),
  CONSTRAINT `concepto_pago_id_refs_id_3496d453` FOREIGN KEY (`concepto_pago_id`) REFERENCES `concepto_pago_concepto_pago` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pago_pago`
--

LOCK TABLES `pago_pago` WRITE;
/*!40000 ALTER TABLE `pago_pago` DISABLE KEYS */;
/*!40000 ALTER TABLE `pago_pago` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perfil_perfil`
--

DROP TABLE IF EXISTS `perfil_perfil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `perfil_perfil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perfil_perfil`
--

LOCK TABLES `perfil_perfil` WRITE;
/*!40000 ALTER TABLE `perfil_perfil` DISABLE KEYS */;
INSERT INTO `perfil_perfil` VALUES (1,'Abogado',0),(2,'Licenciado1',1),(3,'Hacker2',1),(4,'emisario3',1),(5,'mesias3',1);
/*!40000 ALTER TABLE `perfil_perfil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `semestre_semestre`
--

DROP TABLE IF EXISTS `semestre_semestre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `semestre_semestre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `semestre_semestre`
--

LOCK TABLES `semestre_semestre` WRITE;
/*!40000 ALTER TABLE `semestre_semestre` DISABLE KEYS */;
INSERT INTO `semestre_semestre` VALUES (1,'primer Semestre1',1),(2,'Segundo Semestre2',1),(3,'Tercer Semestre',1),(4,'cuarto semestre',1),(5,'quinto semestre',0);
/*!40000 ALTER TABLE `semestre_semestre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tutor_tutor`
--

DROP TABLE IF EXISTS `tutor_tutor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tutor_tutor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `apellidos` varchar(30) DEFAULT NULL,
  `parentesco` varchar(30) DEFAULT NULL,
  `ocupacion` varchar(30) DEFAULT NULL,
  `activo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tutor_tutor`
--

LOCK TABLES `tutor_tutor` WRITE;
/*!40000 ALTER TABLE `tutor_tutor` DISABLE KEYS */;
INSERT INTO `tutor_tutor` VALUES (1,'Geronimo','hernandez hernandez','Bazquez','ALbañil',1),(2,'Rasputin','Garcia','Luna','Actor porno',1),(3,'Said ','Gerra Escudero','Maestro','Director ',0);
/*!40000 ALTER TABLE `tutor_tutor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-11-18  2:04:00
