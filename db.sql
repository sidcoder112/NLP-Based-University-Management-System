/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - nlp
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`nlp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `nlp`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can add permission',2,'add_permission'),
(5,'Can change permission',2,'change_permission'),
(6,'Can delete permission',2,'delete_permission'),
(7,'Can add group',3,'add_group'),
(8,'Can change group',3,'change_group'),
(9,'Can delete group',3,'delete_group'),
(10,'Can add user',4,'add_user'),
(11,'Can change user',4,'change_user'),
(12,'Can delete user',4,'delete_user'),
(13,'Can add content type',5,'add_contenttype'),
(14,'Can change content type',5,'change_contenttype'),
(15,'Can delete content type',5,'delete_contenttype'),
(16,'Can add session',6,'add_session'),
(17,'Can change session',6,'change_session'),
(18,'Can delete session',6,'delete_session'),
(19,'Can add academic_ calendar',7,'add_academic_calendar'),
(20,'Can change academic_ calendar',7,'change_academic_calendar'),
(21,'Can delete academic_ calendar',7,'delete_academic_calendar'),
(22,'Can add collage',8,'add_collage'),
(23,'Can change collage',8,'change_collage'),
(24,'Can delete collage',8,'delete_collage'),
(25,'Can add course',9,'add_course'),
(26,'Can change course',9,'change_course'),
(27,'Can delete course',9,'delete_course'),
(28,'Can add exan_timetable',10,'add_exan_timetable'),
(29,'Can change exan_timetable',10,'change_exan_timetable'),
(30,'Can delete exan_timetable',10,'delete_exan_timetable'),
(31,'Can add external_ mark',11,'add_external_mark'),
(32,'Can change external_ mark',11,'change_external_mark'),
(33,'Can delete external_ mark',11,'delete_external_mark'),
(34,'Can add internal_mark',12,'add_internal_mark'),
(35,'Can change internal_mark',12,'change_internal_mark'),
(36,'Can delete internal_mark',12,'delete_internal_mark'),
(37,'Can add login',13,'add_login'),
(38,'Can change login',13,'change_login'),
(39,'Can delete login',13,'delete_login'),
(40,'Can add notification',14,'add_notification'),
(41,'Can change notification',14,'change_notification'),
(42,'Can delete notification',14,'delete_notification'),
(43,'Can add own_list',15,'add_own_list'),
(44,'Can change own_list',15,'change_own_list'),
(45,'Can delete own_list',15,'delete_own_list'),
(46,'Can add research_article',16,'add_research_article'),
(47,'Can change research_article',16,'change_research_article'),
(48,'Can delete research_article',16,'delete_research_article'),
(49,'Can add student',17,'add_student'),
(50,'Can change student',17,'change_student'),
(51,'Can delete student',17,'delete_student'),
(52,'Can add subject',18,'add_subject'),
(53,'Can change subject',18,'change_subject'),
(54,'Can delete subject',18,'delete_subject');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(7,'NLP','academic_calendar'),
(8,'NLP','collage'),
(9,'NLP','course'),
(10,'NLP','exan_timetable'),
(11,'NLP','external_mark'),
(12,'NLP','internal_mark'),
(13,'NLP','login'),
(14,'NLP','notification'),
(15,'NLP','own_list'),
(16,'NLP','research_article'),
(17,'NLP','student'),
(18,'NLP','subject'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'NLP','0001_initial','2024-03-16 05:38:40.118874'),
(2,'contenttypes','0001_initial','2024-03-16 05:38:40.165743'),
(3,'auth','0001_initial','2024-03-16 05:38:40.728104'),
(4,'admin','0001_initial','2024-03-16 05:38:40.837453'),
(5,'admin','0002_logentry_remove_auto_add','2024-03-16 05:38:40.853103'),
(6,'contenttypes','0002_remove_content_type_name','2024-03-16 05:38:40.962425'),
(7,'auth','0002_alter_permission_name_max_length','2024-03-16 05:38:41.024909'),
(8,'auth','0003_alter_user_email_max_length','2024-03-16 05:38:41.103018'),
(9,'auth','0004_alter_user_username_opts','2024-03-16 05:38:41.134311'),
(10,'auth','0005_alter_user_last_login_null','2024-03-16 05:38:41.212370'),
(11,'auth','0006_require_contenttypes_0002','2024-03-16 05:38:41.212370'),
(12,'auth','0007_alter_validators_add_error_messages','2024-03-16 05:38:41.259262'),
(13,'auth','0008_alter_user_username_max_length','2024-03-16 05:38:41.337337'),
(14,'auth','0009_alter_user_last_name_max_length','2024-03-16 05:38:41.431063'),
(15,'sessions','0001_initial','2024-03-16 05:38:41.493587'),
(16,'NLP','0002_own_list_fee','2024-03-16 09:38:22.256971'),
(17,'NLP','0003_course_stream','2024-04-07 06:00:01.620421'),
(18,'NLP','0004_notification_type','2024-04-07 06:46:27.981225');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('8co6s0kzsxplnxv8ut10zsdbcswd6879','NmU5ZWUyYWQzMTAzZWY5ODc4Zjg1Mjk0YjEwYTI0MWEzOTdjMmUwNTp7ImxpZCI6MywibG9nIjoibG8iLCJjaWQiOiIxIiwic3RpZCI6IjEifQ==','2024-04-20 12:42:35.887581');

/*Table structure for table `nlp_academic_calendar` */

DROP TABLE IF EXISTS `nlp_academic_calendar`;

CREATE TABLE `nlp_academic_calendar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Year` varchar(100) NOT NULL,
  `Calendar` varchar(200) NOT NULL,
  `COURSE_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `NLP_academic_calendar_COURSE_id_0684a7e8_fk_NLP_course_id` (`COURSE_id`),
  CONSTRAINT `NLP_academic_calendar_COURSE_id_0684a7e8_fk_NLP_course_id` FOREIGN KEY (`COURSE_id`) REFERENCES `nlp_course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_academic_calendar` */

insert  into `nlp_academic_calendar`(`id`,`Year`,`Calendar`,`COURSE_id`) values 
(2,'2022','/static/proj_files/20240314_131058.pdf',1);

/*Table structure for table `nlp_collage` */

DROP TABLE IF EXISTS `nlp_collage`;

CREATE TABLE `nlp_collage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `NLP_collage_LOGIN_id_a7881d07_fk_NLP_login_id` (`LOGIN_id`),
  CONSTRAINT `NLP_collage_LOGIN_id_a7881d07_fk_NLP_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `nlp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_collage` */

insert  into `nlp_collage`(`id`,`name`,`email`,`phone`,`place`,`post`,`pin`,`latitude`,`longitude`,`LOGIN_id`) values 
(1,'mggac mahe','mg@gmail.com','9911223344','Thrissur','poas','673545','','',2),
(2,'admin','admin@gmail.com','9911223344','Thrissur','Thrissur','673545','','',4);

/*Table structure for table `nlp_course` */

DROP TABLE IF EXISTS `nlp_course`;

CREATE TABLE `nlp_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Course_Name` varchar(100) NOT NULL,
  `Course_code` varchar(100) NOT NULL,
  `Stream` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_course` */

insert  into `nlp_course`(`id`,`Course_Name`,`Course_code`,`Stream`) values 
(1,'bca','bca123',''),
(2,'bsc','bsc123',''),
(3,'Block chain','cst301',''),
(4,'ss','cst301','');

/*Table structure for table `nlp_exan_timetable` */

DROP TABLE IF EXISTS `nlp_exan_timetable`;

CREATE TABLE `nlp_exan_timetable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(100) NOT NULL,
  `time` varchar(100) NOT NULL,
  `SUBJECT_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `NLP_exan_timetable_SUBJECT_id_767d20b6_fk_NLP_subject_id` (`SUBJECT_id`),
  CONSTRAINT `NLP_exan_timetable_SUBJECT_id_767d20b6_fk_NLP_subject_id` FOREIGN KEY (`SUBJECT_id`) REFERENCES `nlp_subject` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_exan_timetable` */

insert  into `nlp_exan_timetable`(`id`,`date`,`time`,`SUBJECT_id`) values 
(6,'2024-04-11','09:39',2);

/*Table structure for table `nlp_external_mark` */

DROP TABLE IF EXISTS `nlp_external_mark`;

CREATE TABLE `nlp_external_mark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `max_mark` varchar(100) NOT NULL,
  `STUDENT_id` int(11) NOT NULL,
  `SUBJECT_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `NLP_external_mark_STUDENT_id_9bc70a3f_fk_NLP_student_id` (`STUDENT_id`),
  KEY `NLP_external_mark_SUBJECT_id_5181b0fd_fk_NLP_subject_id` (`SUBJECT_id`),
  CONSTRAINT `NLP_external_mark_SUBJECT_id_5181b0fd_fk_NLP_subject_id` FOREIGN KEY (`SUBJECT_id`) REFERENCES `nlp_subject` (`id`),
  CONSTRAINT `NLP_external_mark_STUDENT_id_9bc70a3f_fk_NLP_student_id` FOREIGN KEY (`STUDENT_id`) REFERENCES `nlp_student` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `nlp_external_mark` */

/*Table structure for table `nlp_internal_mark` */

DROP TABLE IF EXISTS `nlp_internal_mark`;

CREATE TABLE `nlp_internal_mark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `max_mark` varchar(100) NOT NULL,
  `STUDENT_id` int(11) NOT NULL,
  `SUBJECT_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `NLP_internal_mark_STUDENT_id_df3e2051_fk_NLP_student_id` (`STUDENT_id`),
  KEY `NLP_internal_mark_SUBJECT_id_954d71e6_fk_NLP_subject_id` (`SUBJECT_id`),
  CONSTRAINT `NLP_internal_mark_SUBJECT_id_954d71e6_fk_NLP_subject_id` FOREIGN KEY (`SUBJECT_id`) REFERENCES `nlp_subject` (`id`),
  CONSTRAINT `NLP_internal_mark_STUDENT_id_df3e2051_fk_NLP_student_id` FOREIGN KEY (`STUDENT_id`) REFERENCES `nlp_student` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_internal_mark` */

insert  into `nlp_internal_mark`(`id`,`max_mark`,`STUDENT_id`,`SUBJECT_id`) values 
(2,'67',1,2);

/*Table structure for table `nlp_login` */

DROP TABLE IF EXISTS `nlp_login`;

CREATE TABLE `nlp_login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `usertype` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_login` */

insert  into `nlp_login`(`id`,`username`,`password`,`usertype`) values 
(1,'a','123','admin'),
(2,'mg@gmail.com','123','college'),
(3,'s@gmail.com','15269','student'),
(4,'admin@gmail.com','admin@1','college'),
(5,'naveenkmathew100@gmail.com','49656','student');

/*Table structure for table `nlp_notification` */

DROP TABLE IF EXISTS `nlp_notification`;

CREATE TABLE `nlp_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Notification` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_notification` */

insert  into `nlp_notification`(`id`,`Notification`,`date`,`type`) values 
(1,'Mca course will be conducted for 2 years duration.','2024-03-14','student');

/*Table structure for table `nlp_own_list` */

DROP TABLE IF EXISTS `nlp_own_list`;

CREATE TABLE `nlp_own_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `COLLEGE_id` int(11) NOT NULL,
  `COURSE_id` int(11) NOT NULL,
  `fee` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `NLP_own_list_COLLEGE_id_77ef2dd9_fk_NLP_collage_id` (`COLLEGE_id`),
  KEY `NLP_own_list_COURSE_id_27d01a78_fk_NLP_course_id` (`COURSE_id`),
  CONSTRAINT `NLP_own_list_COLLEGE_id_77ef2dd9_fk_NLP_collage_id` FOREIGN KEY (`COLLEGE_id`) REFERENCES `nlp_collage` (`id`),
  CONSTRAINT `NLP_own_list_COURSE_id_27d01a78_fk_NLP_course_id` FOREIGN KEY (`COURSE_id`) REFERENCES `nlp_course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_own_list` */

insert  into `nlp_own_list`(`id`,`COLLEGE_id`,`COURSE_id`,`fee`) values 
(1,1,1,'20000');

/*Table structure for table `nlp_research_article` */

DROP TABLE IF EXISTS `nlp_research_article`;

CREATE TABLE `nlp_research_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Article` varchar(100) NOT NULL,
  `Author` varchar(100) NOT NULL,
  `Abstract` varchar(1000) NOT NULL,
  `date` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_research_article` */

insert  into `nlp_research_article`(`id`,`Article`,`Author`,`Abstract`,`date`) values 
(1,'/static/proj_files/20240314_131241.pdf','swami@gmail.com','Deep learning is a method in artificial intelligence (AI) that teaches computers to process data in a way that is inspired by the human brain. Deep learning models can recognize complex patterns in pictures, text, sounds, and other data to produce accurate insights and predictions.','2024-03-21'),
(2,'/static/proj_files/20240314_154947.pdf','s@gmail.com','Machine learning is a subfield of artificial intelligence(AI), which is broadly defined as the capability of a machine to imitate intelligent human behavior. Artificial intelligence systems are used to perform complex tasks in a way that is similar to how humans solve problems.','2024-03-15'),
(3,'/static/proj_files/20240406_175621.pdf','r','','2024-05-02');

/*Table structure for table `nlp_student` */

DROP TABLE IF EXISTS `nlp_student`;

CREATE TABLE `nlp_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `semester` varchar(100) NOT NULL,
  `reg_no` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `COLLAGE_id` int(11) NOT NULL,
  `COURSE_id` int(11) NOT NULL,
  `LOGIN_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `NLP_student_COLLAGE_id_a4689676_fk_NLP_collage_id` (`COLLAGE_id`),
  KEY `NLP_student_COURSE_id_72af269d_fk_NLP_course_id` (`COURSE_id`),
  KEY `NLP_student_LOGIN_id_495653e3_fk_NLP_login_id` (`LOGIN_id`),
  CONSTRAINT `NLP_student_LOGIN_id_495653e3_fk_NLP_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `nlp_login` (`id`),
  CONSTRAINT `NLP_student_COLLAGE_id_a4689676_fk_NLP_collage_id` FOREIGN KEY (`COLLAGE_id`) REFERENCES `nlp_collage` (`id`),
  CONSTRAINT `NLP_student_COURSE_id_72af269d_fk_NLP_course_id` FOREIGN KEY (`COURSE_id`) REFERENCES `nlp_course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_student` */

insert  into `nlp_student`(`id`,`name`,`semester`,`reg_no`,`age`,`place`,`email`,`phone`,`COLLAGE_id`,`COURSE_id`,`LOGIN_id`) values 
(1,'std','1','1234','20','punjab','s@gmail.com','9911223344',1,1,3),
(2,'naveen','1','673597','22','wayanad','naveenkmathew100@gmail.com','866286001',1,1,5);

/*Table structure for table `nlp_subject` */

DROP TABLE IF EXISTS `nlp_subject`;

CREATE TABLE `nlp_subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(100) NOT NULL,
  `semester` varchar(100) NOT NULL,
  `credit` varchar(100) NOT NULL,
  `COURSE_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `NLP_subject_COURSE_id_e10a5fcb_fk_NLP_course_id` (`COURSE_id`),
  CONSTRAINT `NLP_subject_COURSE_id_e10a5fcb_fk_NLP_course_id` FOREIGN KEY (`COURSE_id`) REFERENCES `nlp_course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `nlp_subject` */

insert  into `nlp_subject`(`id`,`subject_name`,`semester`,`credit`,`COURSE_id`) values 
(2,'maths','1','12',1),
(3,'block','1','2',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
