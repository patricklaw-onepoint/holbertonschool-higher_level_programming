-- create the MySQL server user user_0d_1
--   user_0d_1 should have all privileges on your MySQL server
--   The user_0d_1 password should be set to user_0d_1_pwd
--   If the user user_0d_1 already exists, your script should not fail
-- run: cat 1-create_user.sql | mysql -hlocalhost -uroot -p
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';