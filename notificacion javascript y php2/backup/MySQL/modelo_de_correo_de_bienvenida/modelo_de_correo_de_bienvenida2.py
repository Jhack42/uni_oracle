import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def obtener_info_profesor():
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='universidad_uni'
    )

    cursor = conexion.cursor()

    cursor.execute("SELECT nombres, apellidos, correo_electronico FROM Profesores WHERE id_profesor = 1")  # Ajusta según el profesor deseado
    resultado = cursor.fetchone()

    conexion.close()
    return resultado

def enviar_correo_bienvenida():
    correo_emisor = '1364822@senati.pe'  # Cambiar por tu correo
    contraseña_emisor = 'JC221101f'  # Cambiar por tu contraseña
    servidor_smtp = 'smtp.office365.com'
    puerto_smtp = 587

    info_profesor = obtener_info_profesor()

    if info_profesor:
        nombre_profesor, apellidos_profesor, correo_profesor = info_profesor
        curso_seccion = 'Curso XYZ - Sección A'  # Agrega la sección del curso
        listado_estudiantes = 'Estudiante 1, Estudiante 2, Estudiante 3'  # Agrega los estudiantes
        listado_sesiones = 'Sesión 1: Fecha y hora, Sesión 2: Fecha y hora'  # Agrega las sesiones
        listado_evaluaciones = 'Evaluación 1: Fecha y hora, Evaluación 2: Fecha y hora'  # Agrega las evaluaciones

        mensaje = f"Bienvenido {nombre_profesor} {apellidos_profesor} al ciclo 2022-1\n\n{curso_seccion}\n\nListado de estudiantes:\n{listado_estudiantes}\n\nDonde cargar su material\n\nListado de sesiones, fecha y hora:\n{listado_sesiones}\n\nListado de evaluaciones, fecha y hora, cargar sus evaluaciones:\n{listado_evaluaciones}"

        msg = MIMEMultipart()
        msg['From'] = correo_emisor
        msg['To'] = correo_profesor
        msg['Subject'] = 'Bienvenida al ciclo 2022-1'
        msg.attach(MIMEText(mensaje, 'plain'))

        try:
            servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
            servidor.starttls()
            servidor.login(correo_emisor, contraseña_emisor)
            servidor.sendmail(correo_emisor, correo_profesor, msg.as_string())
            servidor.quit()
            print("Correo de bienvenida enviado exitosamente.")
        except Exception as e:
            print("Error al enviar el correo:", e)

enviar_correo_bienvenida()
