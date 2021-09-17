-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: zoi_measurement
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `records`
--

DROP TABLE IF EXISTS `records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `records` (
  `Patient_Id` int NOT NULL AUTO_INCREMENT,
  `Patient_Sample_Number` varchar(100) DEFAULT NULL,
  `x1_Px` varchar(20) DEFAULT NULL,
  `x1_mm` varchar(20) DEFAULT NULL,
  `Comment_x1` varchar(20) DEFAULT NULL,
  `x2_Px` varchar(20) DEFAULT NULL,
  `x2_mm` varchar(20) DEFAULT NULL,
  `Comment_x2` varchar(20) DEFAULT NULL,
  `x3_Px` varchar(20) DEFAULT NULL,
  `x3_mm` varchar(20) DEFAULT NULL,
  `Comment_x3` varchar(20) DEFAULT NULL,
  `x4_Px` varchar(20) DEFAULT NULL,
  `x4_mm` varchar(20) DEFAULT NULL,
  `Comment_x4` varchar(20) DEFAULT NULL,
  `x5_Px` varchar(20) DEFAULT NULL,
  `x5_mm` varchar(20) DEFAULT NULL,
  `Comment_x5` varchar(20) DEFAULT NULL,
  `x6_Px` varchar(20) DEFAULT NULL,
  `x6_mm` varchar(20) DEFAULT NULL,
  `Comment_x6` varchar(20) DEFAULT NULL,
  `x7_Px` varchar(20) DEFAULT NULL,
  `x7_mm` varchar(20) DEFAULT NULL,
  `Comment_x7` varchar(20) DEFAULT NULL,
  `x8_Px` varchar(20) DEFAULT NULL,
  `x8_mm` varchar(20) DEFAULT NULL,
  `Comment_x8` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Patient_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `records`
--

LOCK TABLES `records` WRITE;
/*!40000 ALTER TABLE `records` DISABLE KEYS */;
INSERT INTO `records` VALUES (1,'x_55','86.0','16','Susceptible','86.0','16','Susceptible','50.0','13','Intermediate','86.0','16','Susceptible','26','9','Resistant','26','9','Resistant','26','9','Resistant','26','9','Resistant'),(2,'x_55','86.0','16','Susceptible','86.0','16','Susceptible','50.0','13','Intermediate','86.0','16','Susceptible','26','9','Resistant','26','9','Resistant','26','9','Resistant','26','9','Resistant'),(3,'x_14','86.0','16','Susceptible','80.0','16','Susceptible','44.0','12','Intermediate','86.0','16','Susceptible','26','9','Resistant','26','9','Resistant','26','9','Resistant','','',''),(4,'x_14','86.0','16','Susceptible','80.0','16','Susceptible','44.0','12','Intermediate','86.0','16','Susceptible','26','9','Resistant','26','9','Resistant','26','9','Resistant','','','');
/*!40000 ALTER TABLE `records` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'zoi_measurement'
--
/*!50003 DROP PROCEDURE IF EXISTS `insert_records` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_records`(
in Patient_Sample_Number varchar(100),
in x1_Px varchar(20),
in x1_mm varchar(20),
in Comment_x1 varchar(20),
IN x2_Px VARCHAR(20),
IN x2_mm VARCHAR(20),
IN Comment_x2 VARCHAR(20),
IN x3_Px VARCHAR(20),
IN x3_mm VARCHAR(20),
IN Comment_x3 VARCHAR(20),
IN x4_Px VARCHAR(20),
IN x4_mm VARCHAR(20),
IN Comment_x4 VARCHAR(20),
IN x5_Px VARCHAR(20),
IN x5_mm VARCHAR(20),
IN Comment_x5 VARCHAR(20),
IN x6_Px VARCHAR(20),
IN x6_mm VARCHAR(20),
IN Comment_x6 VARCHAR(20),
IN x7_Px VARCHAR(20),
IN x7_mm VARCHAR(20),
IN Comment_x7 VARCHAR(20),
IN x8_Px VARCHAR(20),
IN x8_mm VARCHAR(20),
IN Comment_x8 VARCHAR(20))
BEGIN
INSERT INTO records(
Patient_Sample_Number,
x1_Px,
x1_mm,
Comment_x1,
x2_Px,
x2_mm,
Comment_x2,
x3_Px,
x3_mm,
Comment_x3,
x4_Px,
x4_mm,
Comment_x4,
x5_Px,
x5_mm,
Comment_x5,
x6_Px,
x6_mm,
Comment_x6,
x7_Px,
x7_mm,
Comment_x7,
x8_Px,
x8_mm,
Comment_x8)
VALUES(Patient_Sample_Number,
x1_Px,
x1_mm,
Comment_x1,
x2_Px,
x2_mm,
Comment_x2,
x3_Px,
x3_mm,
Comment_x3,
x4_Px,
x4_mm,
Comment_x4,
x5_Px,
x5_mm,
Comment_x5,
x6_Px,
x6_mm,
Comment_x6,
x7_Px,
x7_mm,
Comment_x7,
x8_Px,
x8_mm,
Comment_x8);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-19 12:22:53
