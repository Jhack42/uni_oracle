<?php
include 'conexion.php'; // Incluir el archivo de conexión a la base de datos

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $id = $_POST['id'];
    $nombre = $_POST['nombre'];
    $email = $_POST['email'];

    if (!empty($id) && !empty($nombre) && !empty($email)) {
        $sql = "UPDATE usuarios SET nombre='$nombre', email='$email' WHERE id=$id";

        if ($conn->query($sql) === TRUE) {
            echo "Registro actualizado exitosamente";
        } else {
            echo "Error al actualizar el registro: " . $conn->error;
        }
    } else {
        echo "Por favor, completa todos los campos";
    }
}

$conn->close();
?>
