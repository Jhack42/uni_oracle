<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Agregar Nuevo Usuario</title>
</head>
<body>
    <h1>Agregar Nuevo Usuario</h1>

    <?php
    include 'conexion.php'; // Incluir el archivo de conexión

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $nombre = $_POST['nombre'];
        $email = $_POST['email'];

        if (!empty($nombre) && !empty($email)) {
            $sql = "INSERT INTO usuarios (nombre, email) VALUES ('$nombre', '$email')";

            if ($conn->query($sql) === TRUE) {
                // Mensaje de registro exitoso
                echo "<p>Registro guardado correctamente</p>";
            } else {
                // Mensaje si hay un error en la inserción
                echo "<p>El registro no pudo guardarse. Error: " . $conn->error . "</p>";
            }
        } else {
            // Mensaje si faltan datos
            echo "<p>Por favor, completa todos los campos</p>";
        }
    }
    ?>

    <!-- Formulario para agregar nuevo usuario -->
    <form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
        <label for="nombre">Nombre:</label><br>
        <input type="text" id="nombre" name="nombre"><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email"><br><br>

        <input type="submit" value="Agregar usuario">
    </form>

    <!-- Botón para regresar a index.php -->
    <a href="index.php">Regresar a la lista de usuarios</a>

    <?php $conn->close(); ?>
</body>
</html>
