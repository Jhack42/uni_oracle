<?php
// ... (Datos de conexión a la base de datos)

$conexion = oci_connect($usuario, $contrasena, $cadena_conexion);

if (!$conexion) {
    $error = oci_error();
    echo "Error de conexión: " . $error['message'];
} else {
    // Número de registros por página
    $registros_por_pagina = 10;

    // Página actual por defecto
    $pagina = isset($_GET['pagina']) ? $_GET['pagina'] : 1;

    // Calcular el offset
    $offset = ($pagina - 1) * $registros_por_pagina;

    // Consulta para obtener el total de profesores
    $total_query = "SELECT COUNT(*) AS total FROM Profesores";
    $total_statement = oci_parse($conexion, $total_query);
    oci_execute($total_statement);
    $row = oci_fetch_assoc($total_statement);
    $total_profesores = $row['TOTAL'];

    // Consulta con paginación
    $select_query = "SELECT * FROM (SELECT p.*, ROWNUM rnum FROM (SELECT * FROM Profesores) p WHERE ROWNUM <= :limite) WHERE rnum >= :offset";
    $select_statement = oci_parse($conexion, $select_query);
    oci_bind_by_name($select_statement, ":limite", $offset + $registros_por_pagina);
    oci_bind_by_name($select_statement, ":offset", $offset + 1);
    oci_execute($select_statement);

    echo "<h2>Lista de Profesores</h2>";
    echo "<ul>";
    while ($row = oci_fetch_assoc($select_statement)) {
        echo "<li>" . $row['NOMBRES'] . " " . $row['APELLIDOS'] . " - " . $row['CORREO_ELECTRONICO'] . "</li>";
    }
    echo "</ul>";

    // Paginación
    $total_paginas = ceil($total_profesores / $registros_por_pagina);
    echo "<p>Páginas:";
    for ($i = 1; $i <= $total_paginas; $i++) {
        echo "<a href='Read_oracle.php?pagina=" . $i . "'> " . $i . " </a>";
    }
    echo "</p>";

    // Cerrar la conexión
    oci_close($conexion);
}
?>
