<?php
include 'conexion.php'; // Incluir el archivo de conexión a la base de datos

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $email = $_POST['email'];

    if (!empty($nombre) && !empty($email)) {
        $sql = "INSERT INTO usuarios (nombre, email) VALUES ('$nombre', '$email')";

        if ($conn->query($sql) === TRUE) {
            echo "Registro guardado exitosamente";
        } else {
            echo "Error al guardar el registro: " . $conn->error;
        }
    } else {
        echo "Por favor, completa todos los campos";
    }
}

$conn->close();
?>
