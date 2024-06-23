-- Script: 7-cities.sql
-- Script to create database hbtn_0d_usa and table cities in MySQL server

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Create table cities if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
