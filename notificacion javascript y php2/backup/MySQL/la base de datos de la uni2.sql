CREATE DATABASE universidad_uni;

USE universidad_uni;

-- Tabla de Estudiantes
CREATE TABLE Estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100),
    apellidos VARCHAR(100),
    dni VARCHAR(20),
    correo_electronico VARCHAR(100)
);

-- Tabla de Profesores
CREATE TABLE Profesores (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100),
    apellidos VARCHAR(100),
    dni VARCHAR(20),
    correo_electronico VARCHAR(100)
);

-- Tabla de Cursos
CREATE TABLE Cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100),
    descripcion TEXT,
    id_profesor INT,
    FOREIGN KEY (id_profesor) REFERENCES Profesores(id_profesor)
);

-- Tabla de Sesiones de Curso
CREATE TABLE Sesiones_Curso (
    id_sesion INT AUTO_INCREMENT PRIMARY KEY,
    id_curso INT,
    fecha_inicio DATETIME,
    duracion_minutos INT,
    descripcion TEXT,
    FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);

-- Tabla de Evaluaciones
CREATE TABLE Evaluaciones (
    id_evaluacion INT AUTO_INCREMENT PRIMARY KEY,
    id_curso INT,
    nombre_evaluacion VARCHAR(100),
    fecha_evaluacion DATETIME,
    FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);

-- Insertar datos en la tabla Estudiantes
INSERT INTO Estudiantes (nombres, apellidos, dni, correo_electronico)
VALUES
    ('Juan', 'Perez', '12345678', 'juanperez@example.com'),
    ('María', 'García', '87654321', 'mariagarcia@example.com'),
    ('Carlos', 'López', '98765432', 'carloslopez@example.com');

-- Insertar datos en la tabla Profesores
INSERT INTO Profesores (nombres, apellidos, dni, correo_electronico)
VALUES
    ('Pedro', 'Martínez', '54321678', 'pedromartinez@example.com'),
    ('Ana', 'Rodríguez', '13579246', 'anarodriguez@example.com');

-- Insertar datos en la tabla Cursos
INSERT INTO Cursos (nombre_curso, descripcion, id_profesor)
VALUES
    ('Matemáticas', 'Curso avanzado de matemáticas', 1),
    ('Ciencias', 'Introducción a las ciencias', 2);

-- Insertar datos en la tabla Sesiones_Curso
INSERT INTO Sesiones_Curso (id_curso, fecha_inicio, duracion_minutos, descripcion)
VALUES
    (1, '2023-10-01 08:00:00', 90, 'Introducción al cálculo diferencial'),
    (2, '2023-09-15 09:30:00', 120, 'Clases introductorias de biología');

-- Insertar datos en la tabla Evaluaciones
INSERT INTO Evaluaciones (id_curso, nombre_evaluacion, fecha_evaluacion)
VALUES
    (1, 'Examen parcial', '2023-11-15 10:00:00'),
    (2, 'Examen final', '2023-12-10 14:00:00');


