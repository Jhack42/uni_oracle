<?php
include 'conexion.php'; // Incluir el archivo de conexión a la base de datos

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $email = $_POST['email'];

    // Validar los datos ingresados (puedes añadir más validaciones según tus requisitos)
    if (!empty($nombre) && !empty($email)) {
        // Preparar la consulta para insertar un nuevo usuario
        $sql = "INSERT INTO usuarios (nombre, email) VALUES ('$nombre', '$email')";

        // Ejecutar la consulta
        if ($conn->query($sql) === TRUE) {
            echo "Registro creado exitosamente";
        } else {
            echo "Error al crear el registro: " . $conn->error;
        }
    } else {
        echo "Por favor, completa todos los campos";
    }
}

$conn->close();
?>
