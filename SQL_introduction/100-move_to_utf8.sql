-- convert hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- run: cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 

-- Convert the Database Character Set
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE hbtn_0c_0;

-- Convert the Table Character Set
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;