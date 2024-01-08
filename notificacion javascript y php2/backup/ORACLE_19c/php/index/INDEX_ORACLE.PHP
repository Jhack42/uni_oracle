<?php
// Datos de conexión
$usuario = 'db_curso';
$contrasena = 'curso123';
$nombre_servidor = 'localhost';
$puerto = '1521';
$sid = 'orcl';

// Crear la cadena de conexión
$cadena_conexion = "(DESCRIPTION=(ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = $nombre_servidor)(PORT = $puerto)))(CONNECT_DATA=(SID=$sid)))";

// Intentar la conexión
$conexion = oci_connect($usuario, $contrasena, $cadena_conexion);

// Verificar la conexión
if (!$conexion) {
    $error = oci_error();
    echo "Error de conexión: " . $error['message'];
} else {
    echo "Conexión exitosa a Oracle!";
    // Realizar consultas u operaciones en la base de datos aquí
    // No olvides cerrar la conexión cuando hayas terminado:
    oci_close($conexion);
}
?>
