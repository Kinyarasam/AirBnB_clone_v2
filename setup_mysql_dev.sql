-- This script prepares a MySQL server for the project
-- Create project development database with the name : hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating a new user named : hbnb_dev with all priveleges on the db hbnb_dev_db
-- with the password : hbnb_dev_pwd if it  doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Granting all privIleges to the new user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- granting the SELECT privilege for the user hbnb_dev in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
