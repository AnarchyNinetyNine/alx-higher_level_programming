-- Script: 4-never_empty.sql
-- Script to create table id_not_null in MySQL database hbtn_0d_2

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
