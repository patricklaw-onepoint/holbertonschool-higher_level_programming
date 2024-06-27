-- list all records of the table second_table
-- Don't list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
-- The database name will be passed as an argument to the mysql command
-- run: 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;