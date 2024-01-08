<?php
include 'conexion.php'; // Incluir el archivo de conexión a la base de datos

if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET['id'])) {
    $id = $_GET['id'];

    // Consultar si el ID existe en la base de datos
    $check_query = "SELECT * FROM usuarios WHERE id=$id";
    $check_result = $conn->query($check_query);

    if ($check_result->num_rows > 0) {
        // Eliminar el registro
        $delete_query = "DELETE FROM usuarios WHERE id=$id";
        if ($conn->query($delete_query) === TRUE) {
            // Redirigir a index.php después de eliminar el registro
            header("Location: index.php");
            exit(); // Asegura que el script se detenga después de redirigir
        } else {
            echo "Error al intentar eliminar el registro: " . $conn->error;
        }
    } else {
        echo "El registro con el ID proporcionado no existe";
    }
} else {
    echo "No se proporcionó un ID válido para eliminar";
}
?>
