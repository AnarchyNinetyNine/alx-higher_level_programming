-- Script: 5-unique_id.sql
-- Script to create table unique_id in MySQL database hbtn_0d_2

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

