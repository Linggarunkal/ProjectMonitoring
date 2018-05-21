-- MySQL dump 10.16  Distrib 10.2.15-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: project_management
-- ------------------------------------------------------
-- Server version	10.2.15-MariaDB-10.2.15+maria~xenial

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `audit_trail`
--

DROP TABLE IF EXISTS `audit_trail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_trail` (
  `AuditTrail_ID` varchar(10) NOT NULL,
  `Audit_Activity` varchar(50) NOT NULL,
  `Audit_Field` varchar(20) NOT NULL,
  `Audit_Before` varchar(50) NOT NULL,
  `Audit_After` varchar(50) NOT NULL,
  `Audit_Date` date NOT NULL,
  `Audit_Time` time NOT NULL,
  `Audit_User` varchar(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_trail`
--

LOCK TABLES `audit_trail` WRITE;
/*!40000 ALTER TABLE `audit_trail` DISABLE KEYS */;
/*!40000 ALTER TABLE `audit_trail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `Category_ID` char(1) NOT NULL,
  `Category_Name` varchar(20) NOT NULL,
  `Category_Desc` varchar(100) NOT NULL,
  PRIMARY KEY (`Category_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `client` (
  `Client_ID` varchar(12) NOT NULL,
  `Client_Name` varchar(20) NOT NULL,
  `Client_Address` varchar(100) NOT NULL,
  `Client_Email` varchar(50) NOT NULL,
  PRIMARY KEY (`Client_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `department_id` varchar(20) NOT NULL DEFAULT '0',
  `department_name` varchar(50) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `created_date` datetime NOT NULL DEFAULT current_timestamp(),
  `created_by` varchar(10) NOT NULL DEFAULT 'system',
  `modify_date` datetime NOT NULL DEFAULT current_timestamp(),
  `modify_by` varchar(10) NOT NULL DEFAULT 'system'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('DEPT00002','Marketing',NULL,'2018-05-20 22:53:18','system','2018-05-20 22:53:18','system'),('DEPT00003','IT',NULL,'2018-05-20 22:53:29','system','2018-05-20 22:53:29','system');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 trigger tg_department
before insert on department
for each row
begin
declare x int;
declare y int;
set y := (select seq_lastno from sequence where seq_table = 'department');
update sequence set seq_lastno =  y+1 where seq_table = 'department';
set x := (select seq_lastno from sequence where seq_table = 'department');
set new.department_id = concat('DEPT', LPAD(x, 5, '0'));
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `document`
--

DROP TABLE IF EXISTS `document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `document` (
  `Document_No` varchar(20) NOT NULL,
  `Document_Name` varchar(50) NOT NULL,
  `Document_Desc` varchar(100) NOT NULL,
  `Document_URL` varchar(100) NOT NULL,
  `Document_Status` varchar(10) NOT NULL,
  PRIMARY KEY (`Document_No`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `document`
--

LOCK TABLES `document` WRITE;
/*!40000 ALTER TABLE `document` DISABLE KEYS */;
/*!40000 ALTER TABLE `document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `NIK` varchar(7) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Email` varchar(20) NOT NULL,
  `Position` varchar(20) NOT NULL,
  `Password` varchar(20) NOT NULL,
  PRIMARY KEY (`NIK`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job` (
  `Job_ID` char(2) NOT NULL,
  `Job_Name` varchar(30) NOT NULL,
  `Job_Desc` varchar(50) NOT NULL,
  PRIMARY KEY (`Job_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notification` (
  `Notif_ID` varchar(12) NOT NULL,
  `NIK` varchar(7) NOT NULL,
  `Notif_Name` varchar(20) NOT NULL,
  `Notif_Desc` varchar(100) NOT NULL,
  `Notif_Date` date NOT NULL,
  PRIMARY KEY (`Notif_ID`),
  KEY `FKNotificati823642` (`NIK`),
  CONSTRAINT `FKNotificati823642` FOREIGN KEY (`NIK`) REFERENCES `employee` (`NIK`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prl`
--

DROP TABLE IF EXISTS `prl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prl` (
  `PRL_ID` varchar(12) NOT NULL,
  `Task_ID` varchar(12) NOT NULL,
  `PRL_Name` varchar(50) NOT NULL,
  `PRL_Desc` int(100) NOT NULL,
  `PRL_StartDate` date NOT NULL,
  `PRL_EndDate` date NOT NULL,
  `PRL_Target` date NOT NULL,
  `PRL_Status` char(1) NOT NULL,
  `PRL_Notes` varchar(200) NOT NULL,
  `PRL_Document_No` varchar(20) NOT NULL,
  KEY `FKPRL502490` (`Task_ID`),
  KEY `FKPRL68957` (`PRL_Status`),
  KEY `FKPRL165153` (`PRL_Document_No`),
  CONSTRAINT `FKPRL165152` FOREIGN KEY (`PRL_Document_No`) REFERENCES `document` (`Document_No`),
  CONSTRAINT `FKPRL165153` FOREIGN KEY (`PRL_Document_No`) REFERENCES `document` (`Document_No`),
  CONSTRAINT `FKPRL502490` FOREIGN KEY (`Task_ID`) REFERENCES `task` (`Task_ID`),
  CONSTRAINT `FKPRL68957` FOREIGN KEY (`PRL_Status`) REFERENCES `status` (`Status_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prl`
--

LOCK TABLES `prl` WRITE;
/*!40000 ALTER TABLE `prl` DISABLE KEYS */;
/*!40000 ALTER TABLE `prl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `Project_ID` varchar(12) NOT NULL,
  `Customer_ID` varchar(12) NOT NULL,
  `Project_Name` varchar(50) NOT NULL,
  `Project_Mandays` int(10) NOT NULL,
  `Project_StartDate` date NOT NULL,
  `Project_EndDate` date NOT NULL,
  `Project_Status` char(1) NOT NULL,
  PRIMARY KEY (`Project_ID`),
  KEY `FKProject664944` (`Project_Status`),
  KEY `FKProject820043` (`Customer_ID`),
  CONSTRAINT `FKProject664944` FOREIGN KEY (`Project_Status`) REFERENCES `status` (`Status_ID`),
  CONSTRAINT `FKProject820043` FOREIGN KEY (`Customer_ID`) REFERENCES `client` (`Client_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sequence`
--

DROP TABLE IF EXISTS `sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sequence` (
  `seq_table` varchar(20) NOT NULL,
  `seq_lastno` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sequence`
--

LOCK TABLES `sequence` WRITE;
/*!40000 ALTER TABLE `sequence` DISABLE KEYS */;
INSERT INTO `sequence` VALUES ('audit_trail',0),('client',0),('document',0),('employee',0),('prl',0),('project',0),('task',0),('team_project',0),('department',3);
/*!40000 ALTER TABLE `sequence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `status` (
  `Status_ID` char(1) NOT NULL,
  `Status_Name` varchar(20) NOT NULL,
  `Status_Desc` varchar(100) NOT NULL,
  PRIMARY KEY (`Status_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task` (
  `Task_ID` varchar(12) NOT NULL,
  `Project_ID` varchar(12) NOT NULL,
  `Category_ID` char(1) NOT NULL,
  `TeamProject_ID` varchar(12) NOT NULL,
  `Task_StartDate` date NOT NULL,
  `Task_EndDate` date NOT NULL,
  `Task_Target` date NOT NULL,
  `Task_Name` varchar(20) NOT NULL,
  `Task_Status` char(1) NOT NULL,
  `Task_Document_No` varchar(20) NOT NULL,
  `Task_Notes` varchar(200) NOT NULL,
  PRIMARY KEY (`Task_ID`),
  KEY `FKTask857121` (`Task_Status`),
  KEY `FKTask390397` (`Task_Document_No`),
  KEY `FKTask885393` (`Category_ID`),
  CONSTRAINT `FKTask390397` FOREIGN KEY (`Task_Document_No`) REFERENCES `document` (`Document_No`),
  CONSTRAINT `FKTask857121` FOREIGN KEY (`Task_Status`) REFERENCES `status` (`Status_ID`),
  CONSTRAINT `FKTask885393` FOREIGN KEY (`Category_ID`) REFERENCES `category` (`Category_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team_project`
--

DROP TABLE IF EXISTS `team_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `team_project` (
  `TeamProject_ID` varchar(12) NOT NULL,
  `NIK` varchar(7) NOT NULL,
  `Project_ID` varchar(12) NOT NULL,
  `Job_ID` char(2) NOT NULL,
  `Task_ID` varchar(12) NOT NULL,
  PRIMARY KEY (`TeamProject_ID`),
  KEY `FKTeam_proje214919` (`NIK`),
  KEY `FKTeam_proje153194` (`Project_ID`),
  KEY `FKTeam_proje756887` (`Job_ID`),
  KEY `FKTeam_proje910071` (`Task_ID`),
  CONSTRAINT `FKTeam_proje153194` FOREIGN KEY (`Project_ID`) REFERENCES `project` (`Project_ID`),
  CONSTRAINT `FKTeam_proje214919` FOREIGN KEY (`NIK`) REFERENCES `employee` (`NIK`),
  CONSTRAINT `FKTeam_proje756887` FOREIGN KEY (`Job_ID`) REFERENCES `job` (`Job_ID`),
  CONSTRAINT `FKTeam_proje910071` FOREIGN KEY (`Task_ID`) REFERENCES `task` (`Task_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team_project`
--

LOCK TABLES `team_project` WRITE;
/*!40000 ALTER TABLE `team_project` DISABLE KEYS */;
/*!40000 ALTER TABLE `team_project` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-21  9:00:07
