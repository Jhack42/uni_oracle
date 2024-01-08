-- Tabla de Estudiantes
CREATE TABLE Estudiantes (
    id_estudiante NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    nombres VARCHAR2(100),
    apellidos VARCHAR2(100),
    dni VARCHAR2(20),
    correo_electronico VARCHAR2(100)
);


-- Tabla de Profesores
CREATE TABLE Profesores (
    id_profesor NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    nombres VARCHAR2(100),
    apellidos VARCHAR2(100),
    dni VARCHAR2(20),
    correo_electronico VARCHAR2(100)
);


-- Tabla de Cursos
CREATE TABLE Cursos (
    id_curso NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    nombre_curso VARCHAR2(100),
    descripcion CLOB,
    id_profesor NUMBER,
    CONSTRAINT fk_profesor FOREIGN KEY (id_profesor) REFERENCES Profesores(id_profesor)
);


-- Tabla de Sesiones de Curso
CREATE TABLE Sesiones_Curso (
    id_sesion NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    id_curso NUMBER,
    fecha_inicio TIMESTAMP,
    duracion_minutos INT,
    descripcion CLOB,
    CONSTRAINT fk_curso FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);

-- Tabla de Evaluaciones
CREATE TABLE Evaluaciones (
    id_evaluacion NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    id_curso NUMBER,
    nombre_evaluacion VARCHAR2(100),
    fecha_evaluacion TIMESTAMP,
    CONSTRAINT fk_curso_evaluacion FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);

-- Insertar datos en la tabla Estudiantes
INSERT INTO Estudiantes (nombres, apellidos, dni, correo_electronico)
VALUES
    ('Juan', 'Perez', '12345678', 'juanperez@example.com');

INSERT INTO Estudiantes (nombres, apellidos, dni, correo_electronico)
VALUES
    ('María', 'García', '87654321', 'mariagarcia@example.com');

INSERT INTO Estudiantes (nombres, apellidos, dni, correo_electronico)
VALUES
    ('Carlos', 'López', '98765432', 'carloslopez@example.com');

-- Insertar datos en la tabla Profesores
INSERT INTO Profesores (nombres, apellidos, dni, correo_electronico)
VALUES
    ('Pedro', 'Martínez', '54321678', 'pedromartinez@example.com');

INSERT INTO Profesores (nombres, apellidos, dni, correo_electronico)
VALUES
    ('Ana', 'Rodríguez', '13579246', 'anarodriguez@example.com');

-- Insertar datos en la tabla Cursos
INSERT INTO Cursos (nombre_curso, descripcion, id_profesor)
VALUES
    ('Matemáticas', 'Curso avanzado de matemáticas', 1);

INSERT INTO Cursos (nombre_curso, descripcion, id_profesor)
VALUES
    ('Ciencias', 'Introducción a las ciencias', 2);

-- Insertar datos en la tabla Sesiones_Curso
INSERT INTO Sesiones_Curso (id_curso, fecha_inicio, duracion_minutos, descripcion)
VALUES
    (1, TIMESTAMP '2023-10-01 08:00:00', 90, 'Introducción al cálculo diferencial');

INSERT INTO Sesiones_Curso (id_curso, fecha_inicio, duracion_minutos, descripcion)
VALUES
    (2, TIMESTAMP '2023-09-15 09:30:00', 120, 'Clases introductorias de biología');

-- Insertar datos en la tabla Evaluaciones
INSERT INTO Evaluaciones (id_curso, nombre_evaluacion, fecha_evaluacion)
VALUES
    (1, 'Examen parcial', TIMESTAMP '2023-11-15 10:00:00');

INSERT INTO Evaluaciones (id_curso, nombre_evaluacion, fecha_evaluacion)
VALUES
    (2, 'Examen final', TIMESTAMP '2023-12-10 14:00:00');