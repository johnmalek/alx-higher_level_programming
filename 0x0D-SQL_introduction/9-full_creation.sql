-- Creates a new table using CREATE
-- Creates a table second_table
CREATE TABLE if NOT EXISTS second_table (id INT, name VARCHAR, score INT);
-- query to insert first row into the table
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10);
-- Query to insert second row into the table
INSERT INTO second_table (id, name, score)
VALUES (2, 'Alex', 3);
-- Quert to insert third row into the table
INSERT INTO second_table (id, name, score)
VALUES (3, 'Bob', 14);
-- Query to insert fourth row into the table
INSERT INTO second_table (id, name, score)
VALUES (4, 'George', 8);

