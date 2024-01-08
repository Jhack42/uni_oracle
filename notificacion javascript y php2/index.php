<?php
// Incluye el archivo de conexión a la base de datos
include 'conexion.php';

// Define la cantidad de resultados por página y obtiene el número de página actual
$results_per_page = 10;
$page = isset($_GET['page']) ? $_GET['page'] : 1;

// Calcula el índice de inicio para la consulta de base de datos
$start_from = ($page - 1) * $results_per_page;

// Obtiene el valor para buscar en la base de datos
$search = isset($_GET['buscar']) ? $_GET['buscar'] : '';

// Construye la consulta SQL para seleccionar usuarios
$query = "SELECT * FROM usuarios";
if (!empty($search)) {
    // Agrega una cláusula WHERE para filtrar por nombre o email en caso de búsqueda
    $query .= " WHERE nombre LIKE '%$search%' OR email LIKE '%$search%'";
}
// Agrega la limitación para la paginación
$query .= " LIMIT $start_from, $results_per_page";

// Ejecuta la consulta SQL
$result = $conn->query($query);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Lista de Usuarios</title>
    <link rel="stylesheet" href="estilos/estilos.css">
</head>
<body>
<div class="container">
    <h1>Lista de Usuarios</h1>

    <!-- Botón para agregar un nuevo usuario -->
    <button onclick="openModal('agregar')">Agregar Nuevo Usuario</button>

    <!-- Formulario para buscar usuarios por nombre o email -->
    <form action="index.php" method="GET">
        <input type="text" name="buscar" placeholder="Buscar por nombre o email">
        <input type="submit" value="Buscar">
    </form>

    <!-- Tabla que muestra la información de los usuarios -->
    <table class="styled-table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Email</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            <?php
            // Itera a través de los resultados de la consulta y muestra los usuarios en la tabla
            while ($row = $result->fetch_assoc()) {
                echo "<tr>";
                echo "<td>" . $row['id'] . "</td>";
                echo "<td>" . $row['nombre'] . "</td>";
                echo "<td>" . $row['email'] . "</td>";
                echo "<td>
                        <!-- Botones para editar y eliminar usuarios -->
                        <button onclick=\"openModal('editar', {$row['id']}, '{$row['nombre']}', '{$row['email']}')\">Editar</button>
                        <button onclick=\"eliminarUsuario({$row['id']})\">Eliminar</button>
                    </td>";
                echo "</tr>";
            }
            ?>
        </tbody>
    </table>

    <!-- Sección de paginación -->
    <div class="pagination">
        <?php
        // Calcula el total de páginas y crea enlaces para la paginación
        $sql = "SELECT COUNT(id) AS total FROM usuarios";
        $result = $conn->query($sql);
        $row = $result->fetch_assoc();
        $total_pages = ceil($row['total'] / $results_per_page);

        for ($i = 1; $i <= $total_pages; $i++) {
            echo "<a href='index.php?page=" . $i . "'>" . $i . "</a> ";
        }
        ?>
    </div>

    <!-- Modal para agregar/editar usuarios -->
    <div id="myModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal()">&times;</span>
            <form id="formUsuario" method="post" onsubmit="return guardarDatos()">
                <input type="hidden" id="id" name="id">
                <label for="nombre">Nombre:</label><br>
                <input type="text" id="nombre" name="nombre" required><br><br>

                <label for="email">Email:</label><br>
                <input type="email" id="email" name="email" required><br><br>

                <input type="hidden" id="accion" name="accion" value="">
                <input type="submit" value="Guardar">
            </form>
        </div>
    </div>
</div>

<!-- Script JavaScript para funcionalidades del modal y acciones de usuario -->
<script>
    // Función para abrir el modal y prellenar datos si es edición
    function openModal(accion, id = null, nombre = '', email = '') {
        document.getElementById('accion').value = accion;
        document.getElementById('myModal').style.display = 'block';

        if (accion === 'editar') {
            document.getElementById('id').value = id;
            document.getElementById('nombre').value = nombre;
            document.getElementById('email').value = email;
        }
    }

    // Función para cerrar el modal
    function closeModal() {
        document.getElementById('myModal').style.display = 'none';
    }

    // Función para guardar datos (requiere implementación de lógica)
    function guardarDatos() {
        var accion = document.getElementById('accion').value;

        // Agrega lógica para guardar datos según la acción (editar o agregar)

        closeModal();
        return false;
    }

    // Función para eliminar un usuario (requiere implementación de lógica)
    function eliminarUsuario(id) {
        // Agrega lógica para eliminar un usuario con el ID proporcionado
    }
</script>
</body>
</html>
