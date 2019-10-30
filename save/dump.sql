-- MySQL dump 10.13  Distrib 8.0.17, for Linux (x86_64)
--
-- Host: localhost    Database: annotation_web
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookcompletion`
--

DROP TABLE IF EXISTS `bookcompletion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookcompletion` (
  `name` varchar(200) DEFAULT NULL,
  `total_pages` int(7) DEFAULT NULL,
  `completed_pages` int(7) DEFAULT NULL,
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookcompletion`
--

LOCK TABLES `bookcompletion` WRITE;
/*!40000 ALTER TABLE `bookcompletion` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookcompletion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookmarks`
--

DROP TABLE IF EXISTS `bookmarks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookmarks` (
  `file` varchar(200) DEFAULT NULL,
  UNIQUE KEY `file` (`file`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookmarks`
--

LOCK TABLES `bookmarks` WRITE;
/*!40000 ALTER TABLE `bookmarks` DISABLE KEYS */;
/*!40000 ALTER TABLE `bookmarks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `corrections`
--

DROP TABLE IF EXISTS `corrections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `corrections` (
  `pfile` varchar(250) DEFAULT NULL,
  `pfilepath` varchar(255) DEFAULT NULL,
  UNIQUE KEY `pfile` (`pfile`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `corrections`
--

LOCK TABLES `corrections` WRITE;
/*!40000 ALTER TABLE `corrections` DISABLE KEYS */;
/*!40000 ALTER TABLE `corrections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imagelinks`
--

DROP TABLE IF EXISTS `imagelinks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `imagelinks` (
  `file` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `links` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`file`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagelinks`
--

LOCK TABLES `imagelinks` WRITE;
/*!40000 ALTER TABLE `imagelinks` DISABLE KEYS */;
INSERT INTO `imagelinks` VALUES ('bhoomi--1093490973169165705','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/12.jpg'),('bhoomi--1149809547622203498','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/12.jpg'),('bhoomi--1153036631588387163','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/1.jpg'),('bhoomi--1214530269536087001','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/3.jpg'),('bhoomi--1530407934944341951','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/2.jpg'),('bhoomi--163968077602117075','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/7.jpg'),('bhoomi--1648154124739439919','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/13.jpg'),('bhoomi--1829823582449036195','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/1.jpg'),('bhoomi--1832682814360871311','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/11.jpg'),('bhoomi--2301899507806809514','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/3.jpg'),('bhoomi--2332437770289386356','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/1.jpg'),('bhoomi--2518655847716234397','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/1.jpg'),('bhoomi--2685754871933329813','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/6.jpg'),('bhoomi--2747376761122777554','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/4.jpg'),('bhoomi--3057064093742678955','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/6.jpg'),('bhoomi--3327592103742877520','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/9.jpg'),('bhoomi--3369574892944863656','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/9.jpg'),('bhoomi--3417212428220375271','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/1.jpg'),('bhoomi--3444993440243445950','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/2.jpg'),('bhoomi--3501126068029087664','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/4.jpg'),('bhoomi--3572160723760087690','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/4.jpg'),('bhoomi--3668006631648429258','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/8.jpg'),('bhoomi--3835323445165712295','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/12.jpg'),('bhoomi--3903274133037830413','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/10.jpg'),('bhoomi--3998612769072711668','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/15.jpg'),('bhoomi--4122080087369752791','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/5.jpg'),('bhoomi--4205136413881231392','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/5.jpg'),('bhoomi--4300176135291868723','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/2.jpg'),('bhoomi--4300201682789166292','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/5.jpg'),('bhoomi--4326035586504307148','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/19.jpg'),('bhoomi--4378305035816646806','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/15.jpg'),('bhoomi--4512002182141835029','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/5.jpg'),('bhoomi--4854093903012889688','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/17.jpg'),('bhoomi--4856018656486568279','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/2.jpg'),('bhoomi--4977723067281046149','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/8.jpg'),('bhoomi--5210680199637438812','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/21.jpg'),('bhoomi--5295192162689582587','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/8.jpg'),('bhoomi--5398929959677951585','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/11.jpg'),('bhoomi--5400825051246127780','main/myproject/static/imgdata/bhoomi/AAVARNI/RASB/6063/3.jpg'),('bhoomi--5496910326034051376','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/11.jpg'),('bhoomi--5626680384007940517','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/6.jpg'),('bhoomi--5680683570458724401','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/10.jpg'),('bhoomi--5739045167855037818','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/11.jpg'),('bhoomi--5980317329601085522','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/6.jpg'),('bhoomi--6192992679547893158','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/8.jpg'),('bhoomi--6240180405696524905','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/9.jpg'),('bhoomi--628160796054666214','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/16.jpg'),('bhoomi--644355459450021885','main/myproject/static/imgdata/bhoomi/AAVARNI/PIVS/001/2.jpg'),('bhoomi--6490030812207501226','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/7.jpg'),('bhoomi--6509064111990202495','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/1.jpg'),('bhoomi--6752272247853562846','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/4.jpg'),('bhoomi--6767515916530996557','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/4.jpg'),('bhoomi--7133814116017963242','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/19.jpg'),('bhoomi--7283689113395597857','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/1.jpg'),('bhoomi--7591503277631938244','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/6.jpg'),('bhoomi--7910772624570001565','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/24.jpg'),('bhoomi--7966632527004222396','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/8.jpg'),('bhoomi--8005299415329013592','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/14.jpg'),('bhoomi--8311304883806559539','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/18.jpg'),('bhoomi--8379351949920391366','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/3.jpg'),('bhoomi--8401583022463332384','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/8.jpg'),('bhoomi--8481043115068683608','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/2.jpg'),('bhoomi--892607477521247207','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/2.jpg'),('bhoomi--9017847702992455379','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/13.jpg'),('bhoomi--9075165665118640149','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/6.jpg'),('bhoomi--9137272454607564062','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/5.jpg'),('bhoomi-1060141343247689858','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/6.jpg'),('bhoomi-1143590845908397517','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/23.jpg'),('bhoomi-1214541125138534824','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/10.jpg'),('bhoomi-1384280729872624549','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/9.jpg'),('bhoomi-1615577910997926387','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/3.jpg'),('bhoomi-1751834333874715946','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/10.jpg'),('bhoomi-1773457499183188081','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/7.jpg'),('bhoomi-1884088325084804006','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/12.jpg'),('bhoomi-1941601945086899008','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/8.jpg'),('bhoomi-202172496370877890','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/7.jpg'),('bhoomi-2260128633510407767','main/myproject/static/imgdata/bhoomi/AAVARNI/RASB/6063/2.jpg'),('bhoomi-2266623138971916903','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/1.jpg'),('bhoomi-2268285183450400628','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/3.jpg'),('bhoomi-2428633733194604479','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/4.jpg'),('bhoomi-2450168306950605595','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/8.jpg'),('bhoomi-2495648404806631611','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/17.jpg'),('bhoomi-2506177675219143178','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/3.jpg'),('bhoomi-2552825917745920631','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/11.jpg'),('bhoomi-2617141176505668244','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/11.jpg'),('bhoomi-2675346796035398937','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/2.jpg'),('bhoomi-2720539447000410439','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/5.jpg'),('bhoomi-2786841608138200982','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/22.jpg'),('bhoomi-2828719640230018939','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/7.jpg'),('bhoomi-2889591101902406998','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/20.jpg'),('bhoomi-3045961226950800509','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/9.jpg'),('bhoomi-3066405152936351378','main/myproject/static/imgdata/bhoomi/AAVARNI/PIVS/001/1.jpg'),('bhoomi-3389373566478173707','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/3.jpg'),('bhoomi-340187814761394678','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/4.jpg'),('bhoomi-351596379554636260','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/20.jpg'),('bhoomi-3860000951415525143','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/9.jpg'),('bhoomi-3890983276294652753','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/10.jpg'),('bhoomi-4103008726801320197','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/3.jpg'),('bhoomi-4174637494763370330','main/myproject/static/imgdata/bhoomi/AAVARNI/RASB/6063/1.jpg'),('bhoomi-4304348651966554130','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/25.jpg'),('bhoomi-4377509471737622388','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/10.jpg'),('bhoomi-438200346575787890','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/13.jpg'),('bhoomi-4402623325782584249','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/8.jpg'),('bhoomi-4409360835246894406','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/2.jpg'),('bhoomi-4752667642132841198','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/3.jpg'),('bhoomi-4911869106254939790','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/10.jpg'),('bhoomi-4912950162027167351','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/7.jpg'),('bhoomi-4921964655472680065','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/9.jpg'),('bhoomi-4941397015411675944','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/1.jpg'),('bhoomi-4962579650374504684','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/13.jpg'),('bhoomi-500895774069005818','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/11.jpg'),('bhoomi-5413122343044646924','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/7.jpg'),('bhoomi-5570134114268502139','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/6.jpg'),('bhoomi-5576656591667647119','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/5.jpg'),('bhoomi-5749294375774732417','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/7.jpg'),('bhoomi-6098974743401645469','main/myproject/static/imgdata/bhoomi/AAVARNI/RASB/6063/4.jpg'),('bhoomi-6173973044966078331','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/2.jpg'),('bhoomi-6323621435175204764','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/26.jpg'),('bhoomi-6447503965191283276','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/14.jpg'),('bhoomi-6576771763648684302','main/myproject/static/imgdata/bhoomi/AAVARNI/PIVS/001/4.jpg'),('bhoomi-6789590521517604434','main/myproject/static/imgdata/bhoomi/ANINGYAM/PIVS/001/11.jpg'),('bhoomi-685192521001173524','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/KUML/2346/5.jpg'),('bhoomi-6886155759059415620','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/7.jpg'),('bhoomi-7089746171735043496','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/10.jpg'),('bhoomi-7092439844901314740','main/myproject/static/imgdata/bhoomi/AASOUCA SATAKAM/GOML/1456/4.jpg'),('bhoomi-7245466255443716618','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/GOML/991/18.jpg'),('bhoomi-7431838404784668226','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/5.jpg'),('bhoomi-7801073209830540965','main/myproject/static/imgdata/bhoomi/AAVARNI VYAKHYA/PIVS/001/12.jpg'),('bhoomi-7886230027992484135','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/12.jpg'),('bhoomi-7976367333016206220','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/4.jpg'),('bhoomi-844677419142644552','main/myproject/static/imgdata/bhoomi/AAVARNI/PIVS/001/3.jpg'),('bhoomi-8449498891935070686','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/10.jpg'),('bhoomi-8460658571991766229','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/6.jpg'),('bhoomi-8614659246688519033','main/myproject/static/imgdata/bhoomi/ANINGYAM/SVUORI/4378/9.jpg'),('bhoomi-892771800106616876','main/myproject/static/imgdata/bhoomi/ANINGYAM/RASB/6063/11.jpg'),('bhoomi-8962718112200385120','main/myproject/static/imgdata/bhoomi/AMARUKA SATAKAM/KUML/2346/16.jpg'),('bhoomi-9196257779637098583','main/myproject/static/imgdata/bhoomi/ANINGYAM/GOML/1456/9.jpg'),('pih--1091398746378946928','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/8.jpg'),('pih--1865536935808060970','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item2585-Kavaca/4.jpg'),('pih--2164793510888433266','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item155-Abhyudayikasraddhaprayoga/2.jpg'),('pih--2188362162319001649','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/2.jpg'),('pih--2435112576989681293','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item2585-Kavaca/6.jpg'),('pih--3033156982276490669','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/17.jpg'),('pih--3182723182205863154','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/2.jpg'),('pih--3441216045620422222','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/6.jpg'),('pih--3512244519265436505','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item155-Abhyudayikasraddhaprayoga/1.jpg'),('pih--365408623664544277','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1782-Bhairavaprasna/0.jpg'),('pih--3961623373125824315','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/1.jpg'),('pih--3991412297142134279','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item2585-Kavaca/2.jpg'),('pih--3999193889609736300','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1782-Bhairavaprasna/1.jpg'),('pih--4109957043816938828','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item2585-Kavaca/1.jpg'),('pih--4609354309901320827','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item2585-Kavaca/3.jpg'),('pih--5019169580274601768','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/7.jpg'),('pih--5277873156555676579','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item155-Abhyudayikasraddhaprayoga/4.jpg'),('pih--5343728178675712700','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/6.jpg'),('pih--5440220148313075476','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/5.jpg'),('pih--5958130249701978149','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/21.jpg'),('pih--6282010727792190741','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1782-Bhairavaprasna/7.jpg'),('pih--6573990459551949239','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/3.jpg'),('pih--7549963291179889818','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/12.jpg'),('pih--7895011958408169686','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/15.jpg'),('pih--813942853450432967','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item2585-Kavaca/0.jpg'),('pih--8483467933764941230','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item155-Abhyudayikasraddhaprayoga/5.jpg'),('pih--8524859030110874396','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/14.jpg'),('pih--8763076414201502846','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/18.jpg'),('pih--8859164206394784713','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/5.jpg'),('pih--9113139590902960706','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/1.jpg'),('pih--9207894531630984574','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/9.jpg'),('pih--956649187137983844','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/0.jpg'),('pih-1484995336820972115','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/7.jpg'),('pih-200115746061203059','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item155-Abhyudayikasraddhaprayoga/3.jpg'),('pih-2705264350855842983','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/9.jpg'),('pih-2838751884733910477','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/4.jpg'),('pih-2865701762223781425','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/16.jpg'),('pih-3270519910090936767','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1782-Bhairavaprasna/2.jpg'),('pih-3396615917522455035','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/20.jpg'),('pih-3476986173959729602','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item155-Abhyudayikasraddhaprayoga/7.jpg'),('pih-439018900550542180','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item155-Abhyudayikasraddhaprayoga/0.jpg'),('pih-4516950959610773572','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item2585-Kavaca/7.jpg'),('pih-4807251374567763225','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/0.jpg'),('pih-4867523729815735560','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/19.jpg'),('pih-5465209212468984892','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1782-Bhairavaprasna/5.jpg'),('pih-6207402043666453860','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1782-Bhairavaprasna/4.jpg'),('pih-6315486499773296083','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/8.jpg'),('pih-6415909481823578681','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/13.jpg'),('pih-6501338916916278721','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/10.jpg'),('pih-7460731887318056303','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/3.jpg'),('pih-7495319805357398091','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item2585-Kavaca/5.jpg'),('pih-7899590326061108364','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/11.jpg'),('pih-8115880921203675483','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1782-Bhairavaprasna/3.jpg'),('pih-8153975329029595484','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item396-Sivanamasahasra/10.jpg'),('pih-8871200124149300175','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item155-Abhyudayikasraddhaprayoga/6.jpg'),('pih-9195941713303106239','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1782-Bhairavaprasna/6.jpg'),('pih-925913242259322713','main/myproject/static/imgdata/penn-in-hand/Ms.Coll.390,Item1929-Kapila-Tattvasamasa/4.jpg');
/*!40000 ALTER TABLE `imagelinks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `info`
--

DROP TABLE IF EXISTS `info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `info` (
  `username` varchar(255) DEFAULT NULL,
  `file` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `localurl` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info`
--

LOCK TABLES `info` WRITE;
/*!40000 ALTER TABLE `info` DISABLE KEYS */;
/*!40000 ALTER TABLE `info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `json_v1`
--

DROP TABLE IF EXISTS `json_v1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `json_v1` (
  `filename` varchar(200) DEFAULT NULL,
  `json_data` text,
  `fileurl` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `json_v1`
--

LOCK TABLES `json_v1` WRITE;
/*!40000 ALTER TABLE `json_v1` DISABLE KEYS */;
/*!40000 ALTER TABLE `json_v1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `json_v2`
--

DROP TABLE IF EXISTS `json_v2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `json_v2` (
  `filename` varchar(200) DEFAULT NULL,
  `json_data` text,
  `fileurl` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `json_v2`
--

LOCK TABLES `json_v2` WRITE;
/*!40000 ALTER TABLE `json_v2` DISABLE KEYS */;
/*!40000 ALTER TABLE `json_v2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagerequests`
--

DROP TABLE IF EXISTS `pagerequests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagerequests` (
  `name` varchar(20) DEFAULT NULL,
  `book` varchar(40) DEFAULT NULL,
  `start_page` int(10) DEFAULT NULL,
  `current_page` int(10) DEFAULT NULL,
  `end_page` int(10) DEFAULT NULL,
  `skipped` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagerequests`
--

LOCK TABLES `pagerequests` WRITE;
/*!40000 ALTER TABLE `pagerequests` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagerequests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `puids`
--

DROP TABLE IF EXISTS `puids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `puids` (
  `pfile` varchar(255) DEFAULT NULL,
  `pfilepath` varchar(255) DEFAULT NULL,
  `saved_date` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `puids`
--

LOCK TABLES `puids` WRITE;
/*!40000 ALTER TABLE `puids` DISABLE KEYS */;
/*!40000 ALTER TABLE `puids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ruids`
--

DROP TABLE IF EXISTS `ruids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ruids` (
  `ruid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ruids`
--

LOCK TABLES `ruids` WRITE;
/*!40000 ALTER TABLE `ruids` DISABLE KEYS */;
/*!40000 ALTER TABLE `ruids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `uids`
--

DROP TABLE IF EXISTS `uids`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `uids` (
  `ufile` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `uids`
--

LOCK TABLES `uids` WRITE;
/*!40000 ALTER TABLE `uids` DISABLE KEYS */;
INSERT INTO `uids` VALUES ('pih--3512244519265436505'),('pih-439018900550542180'),('pih--5277873156555676579'),('pih-8871200124149300175'),('pih--2164793510888433266'),('pih--8483467933764941230'),('pih-200115746061203059'),('pih-3476986173959729602'),('pih--3961623373125824315'),('pih-8153975329029595484'),('pih--956649187137983844'),('pih--9207894531630984574'),('pih-2838751884733910477'),('pih--1091398746378946928'),('pih--5343728178675712700'),('pih--3182723182205863154'),('pih--5440220148313075476'),('pih-7460731887318056303'),('pih--5019169580274601768'),('pih--7549963291179889818'),('pih--9113139590902960706'),('pih--7895011958408169686'),('pih-4867523729815735560'),('pih-6501338916916278721'),('pih--5958130249701978149'),('pih-4807251374567763225'),('pih-2705264350855842983'),('pih-925913242259322713'),('pih-3396615917522455035'),('pih-6315486499773296083'),('pih--3441216045620422222'),('pih--3033156982276490669'),('pih--8524859030110874396'),('pih--2188362162319001649'),('pih-2865701762223781425'),('pih--8763076414201502846'),('pih--8859164206394784713'),('pih-7899590326061108364'),('pih--6573990459551949239'),('pih-1484995336820972115'),('pih-6415909481823578681'),('pih--3999193889609736300'),('pih--365408623664544277'),('pih-6207402043666453860'),('pih-9195941713303106239'),('pih-3270519910090936767'),('pih-5465209212468984892'),('pih-8115880921203675483'),('pih--6282010727792190741'),('pih--4109957043816938828'),('pih--813942853450432967'),('pih--1865536935808060970'),('pih--2435112576989681293'),('pih--3991412297142134279'),('pih-7495319805357398091'),('pih--4609354309901320827'),('pih-4516950959610773572'),('bhoomi--1149809547622203498'),('bhoomi--1829823582449036195'),('bhoomi--5680683570458724401'),('bhoomi--3369574892944863656'),('bhoomi-7092439844901314740'),('bhoomi--3668006631648429258'),('bhoomi--2685754871933329813'),('bhoomi--892607477521247207'),('bhoomi--4205136413881231392'),('bhoomi-2552825917745920631'),('bhoomi--8379351949920391366'),('bhoomi--6490030812207501226'),('bhoomi--3417212428220375271'),('bhoomi-1751834333874715946'),('bhoomi-8614659246688519033'),('bhoomi--3501126068029087664'),('bhoomi-4402623325782584249'),('bhoomi--5626680384007940517'),('bhoomi-6173973044966078331'),('bhoomi--4300201682789166292'),('bhoomi--5739045167855037818'),('bhoomi-2268285183450400628'),('bhoomi-202172496370877890'),('bhoomi--1153036631588387163'),('bhoomi-1214541125138534824'),('bhoomi-4921964655472680065'),('bhoomi-340187814761394678'),('bhoomi--8401583022463332384'),('bhoomi--7591503277631938244'),('bhoomi--4300176135291868723'),('bhoomi--4122080087369752791'),('bhoomi-6789590521517604434'),('bhoomi-3389373566478173707'),('bhoomi-5749294375774732417'),('bhoomi-7886230027992484135'),('bhoomi--7283689113395597857'),('bhoomi-8449498891935070686'),('bhoomi-1384280729872624549'),('bhoomi-7976367333016206220'),('bhoomi--7966632527004222396'),('bhoomi-8460658571991766229'),('bhoomi--8481043115068683608'),('bhoomi-5576656591667647119'),('bhoomi-892771800106616876'),('bhoomi-1615577910997926387'),('bhoomi-1773457499183188081'),('bhoomi--9017847702992455379'),('bhoomi-1884088325084804006'),('bhoomi--6509064111990202495'),('bhoomi--3903274133037830413'),('bhoomi-9196257779637098583'),('bhoomi-2428633733194604479'),('bhoomi-1941601945086899008'),('bhoomi-1060141343247689858'),('bhoomi--1530407934944341951'),('bhoomi--4512002182141835029'),('bhoomi-500895774069005818'),('bhoomi-4103008726801320197'),('bhoomi-6886155759059415620'),('bhoomi-4962579650374504684'),('bhoomi-3066405152936351378'),('bhoomi-6576771763648684302'),('bhoomi--644355459450021885'),('bhoomi-844677419142644552'),('bhoomi-4174637494763370330'),('bhoomi-6098974743401645469'),('bhoomi-2260128633510407767'),('bhoomi--5400825051246127780'),('bhoomi--1093490973169165705'),('bhoomi-2266623138971916903'),('bhoomi--3998612769072711668'),('bhoomi--7133814116017963242'),('bhoomi-4377509471737622388'),('bhoomi--3327592103742877520'),('bhoomi--6752272247853562846'),('bhoomi-2889591101902406998'),('bhoomi--6192992679547893158'),('bhoomi-5570134114268502139'),('bhoomi--4854093903012889688'),('bhoomi--8005299415329013592'),('bhoomi--4856018656486568279'),('bhoomi-8962718112200385120'),('bhoomi--8311304883806559539'),('bhoomi--9137272454607564062'),('bhoomi--5496910326034051376'),('bhoomi--1214530269536087001'),('bhoomi-5413122343044646924'),('bhoomi--1648154124739439919'),('bhoomi-7801073209830540965'),('bhoomi--2518655847716234397'),('bhoomi-4911869106254939790'),('bhoomi-3045961226950800509'),('bhoomi--3572160723760087690'),('bhoomi-2450168306950605595'),('bhoomi--5980317329601085522'),('bhoomi-2675346796035398937'),('bhoomi-7431838404784668226'),('bhoomi-2617141176505668244'),('bhoomi-2506177675219143178'),('bhoomi-2828719640230018939'),('bhoomi-4941397015411675944'),('bhoomi-3890983276294652753'),('bhoomi-3860000951415525143'),('bhoomi--6767515916530996557'),('bhoomi--4977723067281046149'),('bhoomi--9075165665118640149'),('bhoomi-4409360835246894406'),('bhoomi-685192521001173524'),('bhoomi--1832682814360871311'),('bhoomi-4752667642132841198'),('bhoomi-4912950162027167351'),('bhoomi--3835323445165712295'),('bhoomi--2332437770289386356'),('bhoomi--4378305035816646806'),('bhoomi--4326035586504307148'),('bhoomi-7089746171735043496'),('bhoomi--5210680199637438812'),('bhoomi--6240180405696524905'),('bhoomi--7910772624570001565'),('bhoomi--2747376761122777554'),('bhoomi-351596379554636260'),('bhoomi--5295192162689582587'),('bhoomi--3057064093742678955'),('bhoomi-2495648404806631611'),('bhoomi-6447503965191283276'),('bhoomi--3444993440243445950'),('bhoomi--628160796054666214'),('bhoomi-7245466255443716618'),('bhoomi-2720539447000410439'),('bhoomi-6323621435175204764'),('bhoomi--5398929959677951585'),('bhoomi--2301899507806809514'),('bhoomi-2786841608138200982'),('bhoomi--163968077602117075'),('bhoomi-4304348651966554130'),('bhoomi-1143590845908397517'),('bhoomi-438200346575787890');
/*!40000 ALTER TABLE `uids` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `viewer`
--

DROP TABLE IF EXISTS `viewer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `viewer` (
  `Website` char(100) DEFAULT NULL,
  `Link` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `viewer`
--

LOCK TABLES `viewer` WRITE;
/*!40000 ALTER TABLE `viewer` DISABLE KEYS */;
/*!40000 ALTER TABLE `viewer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-11 13:23:06
