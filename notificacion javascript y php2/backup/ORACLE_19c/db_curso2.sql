CREATE TABLE estudiantes (
    id_estudiante NUMBER PRIMARY KEY,
    nombres VARCHAR2(100),
    apellidos VARCHAR2(100),
    dni VARCHAR2(20),
    correo_electronico VARCHAR2(100)
);

CREATE TABLE profesores (
    id_profesor NUMBER PRIMARY KEY,
    nombres VARCHAR2(100),
    apellidos VARCHAR2(100),
    dni VARCHAR2(20),
    correo_electronico VARCHAR2(100)
);

CREATE TABLE cursos (
    id_curso NUMBER PRIMARY KEY,
    nombre_curso VARCHAR2(100),
    descripcion CLOB,
    id_profesor NUMBER,
    CONSTRAINT fk_profesor FOREIGN KEY (id_profesor) REFERENCES Profesores(id_profesor)
);

CREATE TABLE sesiones_Curso (
    id_sesion NUMBER PRIMARY KEY,
    id_curso NUMBER,
    fecha_inicio TIMESTAMP,
    duracion_minutos NUMBER,
    descripcion CLOB,
    CONSTRAINT fk_curso FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);

CREATE TABLE evaluaciones (
    id_evaluacion NUMBER PRIMARY KEY,
    id_curso NUMBER,
    nombre_evaluacion VARCHAR2(100),
    fecha_evaluacion TIMESTAMP,
    CONSTRAINT fk_curso_eval FOREIGN KEY (id_curso) REFERENCES Cursos(id_curso)
);





INSERT INTO Estudiantes (id_estudiante, nombres, apellidos, dni, correo_electronico)
VALUES
    (1, 'Juan', 'Perez', '12345678', 'juanperez@example.com');

INSERT INTO Profesores (id_profesor, nombres, apellidos, dni, correo_electronico)
VALUES
    (1, 'Pedro', 'Martínez', '54321678', 'pedromartinez@example.com');

INSERT INTO Cursos (id_curso, nombre_curso, descripcion, id_profesor)
VALUES
    (1, 'Matemáticas', 'Curso avanzado de matemáticas', 1);

INSERT INTO Sesiones_Curso (id_sesion, id_curso, fecha_inicio, duracion_minutos, descripcion)
VALUES
    (1, 1, TO_TIMESTAMP('2023-10-01 08:00:00', 'YYYY-MM-DD HH24:MI:SS'), 90, 'Introducción al cálculo diferencial');

INSERT INTO Evaluaciones (id_evaluacion, id_curso, nombre_evaluacion, fecha_evaluacion)
VALUES
    (1, 1, 'Examen parcial', TO_TIMESTAMP('2023-11-15 10:00:00', 'YYYY-MM-DD HH24:MI:SS'));

