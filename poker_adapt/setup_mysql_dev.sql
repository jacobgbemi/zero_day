-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS poker_dev_db;
CREATE USER IF NOT EXISTS 'poker_dev'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON `poker_dev_db`.* TO 'poker_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'poker_dev'@'localhost';
FLUSH PRIVILEGES;