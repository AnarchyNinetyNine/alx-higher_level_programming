-- Script: 100-move_to_utf8.sql
-- Script to convert hbtn_0c_0 database, first_table, and name field in first_table to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Convert the database to UTF8
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Convert the table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
