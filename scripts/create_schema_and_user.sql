CREATE SCHEMA IF NOT EXISTS `locafan` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `locafan`;
CREATE USER 'tcc'@'localhost' IDENTIFIED BY '#jm7&vf0$';
GRANT ALL ON locafan.* TO 'tcc'@'localhost';
FLUSH PRIVILEGES;
