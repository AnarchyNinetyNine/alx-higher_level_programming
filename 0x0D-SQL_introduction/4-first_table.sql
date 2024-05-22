-- Script: 4-first_table.sql
-- This script creates a table called first_table with columns id and name if it does not already exist.

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
