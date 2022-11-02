-- Create a database and table using CREATE
-- Create database hbtn_0d_usa and table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT, FOREIGN KEY(state_id) REFERENCES states(state_id) NOT NULL, name VARCHAR(256) NOT NULL);
