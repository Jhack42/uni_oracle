<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Registro</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <?php
        $conexion = new mysqli('localhost', 'root', '', 'ecommerce');
        
        if ($conexion->connect_error) {
            die("Error de conexión: " . $conexion->connect_error);
        }

        if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET['id'])) {
            $id = $_GET['id'];
            $query = "SELECT * FROM tabla WHERE id = $id";
            $result = $conexion->query($query);

            if ($result->num_rows > 0) {
                $row = $result->fetch_assoc();
        ?>
                <h2>Editar Registro</h2>
                <form action="procesar.php" method="post">
                    <!-- Campos del formulario -->
                    <input type="hidden" name="id" value="<?php echo $row['id']; ?>">
                    <label for="nombre">Nombre:</label>
                    <input type="text" name="nombre" value="<?php echo $row['nombre']; ?>" required>
                    <br>
                    <label for="descripcion">Descripción:</label>
                    <textarea name="descripcion" required><?php echo $row['descripcion']; ?></textarea>
                    <br>
                    <input type="submit" value="Actualizar">
                </form>
        <?php
            } else {
                echo "Registro no encontrado.";
            }
        } else {
            echo "Parámetros inválidos.";
        }
        ?>
    </div>
</body>
</html>
