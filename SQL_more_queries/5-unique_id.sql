-- Creates the table unique_id on your MySQL server
-- run: cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2 
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);