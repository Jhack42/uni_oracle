CREATE DATABASE universidad_uni;

USE universidad_uni;

CREATE TABLE estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100),
    apellidos VARCHAR(100),
    dni VARCHAR(20),
    correo_electronico VARCHAR(100)
);

CREATE TABLE profesores (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100),
    apellidos VARCHAR(100),
    dni VARCHAR(20),
    correo_electronico VARCHAR(100)
);

CREATE TABLE cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100),
    descripcion TEXT,
    id_profesor INT,
    fecha_inicio DATETIME, -- Fecha y hora de inicio del curso
    duracion_minutos INT, -- Duración del curso en minutos
    FOREIGN KEY (id_profesor) REFERENCES Profesores(id_profesor)
);

CREATE TABLE evaluaciones (
    id_evaluacion INT AUTO_INCREMENT PRIMARY KEY,
    id_curso INT,
    nombre_evaluacion VARCHAR(100),
    fecha_evaluacion DATETIME, -- Fecha y hora de la evaluación
    FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);

INSERT INTO Profesores (nombres, apellidos, dni, correo_electronico) VALUES
('Juan', 'Pérez', '12345678', 'cacereshilsasacajhack@gmail.com'),
('María', 'García', '98765432', 'margaritahilasaca@gmail.com');

