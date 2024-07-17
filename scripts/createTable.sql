CREATE DATABASE IF NOT EXISTS leet;

USE leet;

CREATE TABLE IF NOT EXISTS names (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS tags (
    id INT,
    tag VARCHAR(30)
);

CREATE TABLE IF NOT EXISTS question (
    id INT PRIMARY KEY,
    info VARCHAR(13999)
);

CREATE TABLE IF NOT EXISTS sol (
    id INT,
    details BLOB,
    title VARCHAR(100),
    langs VARCHAR(40)
);

CREATE TABLE IF NOT EXISTS python (
    id INT,
    code BLOB
);

CREATE TABLE IF NOT EXISTS java (
    id INT,
    code BLOB
);

CREATE TABLE IF NOT EXISTS mysql (
    id INT,
    code BLOB
);

CREATE TABLE IF NOT EXISTS url (
    id INT PRIMARY KEY,
    info VARCHAR(400)
);


CREATE TABLE IF NOT EXISTS tags_count (
    tag VARCHAR(30) PRIMARY KEY,
    count INT
);

CREATE TABLE IF NOT EXISTS tags_cache (
    tag VARCHAR(30) PRIMARY KEY,
    data MEDIUMBLOB
);

CREATE TABLE IF NOT EXISTS diff (
    rate INT PRIMARY KEY,
    ids VARCHAR(14000)
);