<?php
// Datos del remitente
$correo_emisor = '1364822@senati.pe';  // Cambiar por tu correo
$contraseña_emisor = 'JC221101f';  // Cambiar por tu contraseña

// Configuración del servidor SMTP
$servidor_smtp = 'smtp.office365.com';
$puerto_smtp = 587;

// Función para enviar correos de bienvenida
function enviar_correo_bienvenida($destinatario, $nombre_profesor, $apellido_profesor) {
    global $correo_emisor, $contraseña_emisor, $servidor_smtp, $puerto_smtp;

    $curso_seccion = 'Curso XYZ - Sección';  // Ejemplo: Cambia esto para cada profesor
    $listado_estudiantes = 'Estudiante 1, Estudiante 2, Estudiante 3';  // Agrega los estudiantes
    $listado_sesiones = 'Sesión 1: Fecha y hora, Sesión 2: Fecha y hora';  // Agrega las sesiones
    $listado_evaluaciones = 'Evaluación 1: Fecha y hora, Evaluación 2: Fecha y hora';  // Agrega las evaluaciones

    $mensaje = "Bienvenido $nombre_profesor $apellido_profesor al ciclo 2022-1\n\n$curso_seccion\n\nListado de estudiantes:\n$listado_estudiantes\n\nDonde cargar su material\n\nListado de sesiones, fecha y hora:\n$listado_sesiones\n\nListado de evaluaciones, fecha y hora, cargar sus evaluaciones:\n$listado_evaluaciones";

    $cabeceras = "From: $correo_emisor\r\n";
    $cabeceras .= "Content-type: text/plain; charset=UTF-8\r\n";

    try {
        $resultado = mail($destinatario, 'Bienvenida al ciclo 2022-1', $mensaje, $cabeceras);
        if ($resultado) {
            echo "Correo de bienvenida enviado exitosamente a $destinatario.";
        } else {
            echo "Error al enviar el correo.";
        }
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}

// Ejemplo de uso
$destinatario = 'cacereshilasacajhack@gmail.com';  // Cambiar por el correo del profesor
$nombre_profesor = 'Jhack';
$apellido_profesor = 'Caceres';

enviar_correo_bienvenida($destinatario, $nombre_profesor, $apellido_profesor);
?>
