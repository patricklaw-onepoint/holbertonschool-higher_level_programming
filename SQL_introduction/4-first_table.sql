-- create a table called first_table in the current database in your MySQL server.
-- run: cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
CREATE TABLE IF NOT EXISTS first_table (
    id INT DEFAULT 1,
    name VARCHAR(256)
);