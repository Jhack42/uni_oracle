import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def obtener_informacion_clase():
    # Conectarse a la base de datos
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='universidad_uni'
    )
    
    cursor = conexion.cursor()
    
    # Ejemplo de consulta para obtener la información de la clase y los correos de los profesores
    cursor.execute("SELECT P.nombres, P.apellidos, P.correo_electronico, SC.fecha_inicio, C.nombre_curso FROM Profesores P INNER JOIN Cursos C ON P.id_profesor = C.id_profesor INNER JOIN Sesiones_Curso SC ON SC.id_curso = C.id_curso WHERE SC.id_sesion = 1")
    
    # Obtener los datos de la consulta
    resultado = cursor.fetchone()
    
    conexion.close()
    return resultado

def enviar_notificacion_toma_clase():
    # Configuración del servidor SMTP
    correo_emisor = '1364822@senati.pe'  # Cambiar por tu correo
    contraseña_emisor = 'JC221101f'  # Cambiar por tu contraseña
    servidor_smtp = 'smtp.office365.com'
    puerto_smtp = 587

    # Obtener la información de la clase y los correos de los profesores desde la base de datos
    info_clase = obtener_informacion_clase()
    
    if info_clase:
        nombre_docente, apellidos_docente, correo_docente, dia_clase, nombre_curso = info_clase

        # Contenido del correo
        mensaje = f"Estimado {nombre_docente} {apellidos_docente},\n\nSe le hace recordar que el día {dia_clase} tiene sesión del curso '{nombre_curso}'.\n\n<Texto argumentativo>"

        # Configuración del correo
        msg = MIMEMultipart()
        msg['From'] = correo_emisor
        msg['To'] = correo_docente  # Usar el correo del docente obtenido de la base de datos
        msg['Subject'] = 'Recordatorio de sesión de curso'
        msg.attach(MIMEText(mensaje, 'plain'))

        # Conexión al servidor SMTP y envío del correo
        try:
            servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
            servidor.starttls()
            servidor.login(correo_emisor, contraseña_emisor)
            servidor.sendmail(correo_emisor, msg['To'], msg.as_string())
            servidor.quit()
            print("Correo de notificación enviado exitosamente.")
        except Exception as e:
            print("Error al enviar el correo:", e)

# Ejecutar la función para enviar la notificación de la clase
enviar_notificacion_toma_clase()
