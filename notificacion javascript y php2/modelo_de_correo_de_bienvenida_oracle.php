
<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/autoload.php'; // Asegúrate de incluir la ruta correcta a PHPMailer

$mail = new PHPMailer(true);

try {
    // Configuración del servidor SMTP
    $mail->isSMTP();
    $mail->Host = 'smtp-mail.outlook.com';
    $mail->SMTPAuth = true;
    $mail->Username = '1364822@senati.pe'; // Cambiar por tu correo
    $mail->Password = 'JC221101f'; // Cambiar por tu contraseña
    $mail->SMTPSecure = 'tls';
    $mail->Port = 587;

    // Contenido del correo
    $mail->setFrom('1364822@senati.pe', 'Nombre Remitente');
    $mail->addAddress('cacereshilasacajhack@gmail.com', 'Nombre Destinatario');
    $mail->Subject = 'Asunto del correo';
    $mail->Body = 'Contenido del correo...';

    // Envío del correo
    $mail->send();
    echo 'Correo enviado correctamente';
} catch (Exception $e) {
    echo 'Error al enviar el correo: ', $mail->ErrorInfo;
}
?>
