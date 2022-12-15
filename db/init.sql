CREATE DATABASE some_medical_service;
CREATE ROLE admin WITH CREATEDB LOGIN PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE some_medical_service TO admin;