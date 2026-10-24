CREATE DATABASE IF NOT EXISTS taller_mecanico_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

SHOW DATABASES;

CREATE USER 'taller_user'@'localhost'
IDENTIFIED BY 'CAMBIAR_POR_CONTRASENA_LOCAL';

GRANT ALL PRIVILEGES
ON taller_mecanico_db.*
TO 'taller_user'@'localhost';

FLUSH PRIVILEGES;

SHOW GRANTS FOR 'taller_user'@'localhost';
