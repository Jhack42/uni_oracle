import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def obtener_correos_profesores():
    # Conectarse a la base de datos
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='universidad_uni'
    )
    
    cursor = conexion.cursor()
    
    # Obtener correos electrónicos de los profesores
    cursor.execute("SELECT correo_electronico FROM profesores")
    correos = [registro[0] for registro in cursor.fetchall()]
    
    conexion.close()
    return correos

def enviar_correo_bienvenida(lista_correos, nombre_docente, curso_seccion, listado_estudiantes, listado_sesiones, listado_evaluaciones):
    correo_emisor = '1364822@senati.pe'  # Cambiar por tu correo
    contraseña_emisor = 'JC221101f'  # Cambiar por tu contraseña
    servidor_smtp = 'smtp.office365.com'
    puerto_smtp = 587

    mensaje = f"Bienvenido {nombre_docente} al ciclo 2024-1\n\nCurso/Sección: {curso_seccion}\n\nListado de estudiantes: {listado_estudiantes}\n\nDonde cargar su material\n\nListado de sesiones, fecha y hora:\n{listado_sesiones}\n\nListado de evaluaciones, fecha y hora, cargar sus evaluaciones:\n{listado_evaluaciones}"

    # Configuración del correo
    msg = MIMEMultipart()
    msg['From'] = correo_emisor
    msg['To'] = ', '.join(lista_correos)  # Lista de correos separados por coma
    msg['Subject'] = 'Bienvenida al ciclo 2024-1'
    msg.attach(MIMEText(mensaje, 'plain'))

    # Conexión al servidor SMTP y envío del correo
    try:
        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        servidor.starttls()
        servidor.login(correo_emisor, contraseña_emisor)
        servidor.sendmail(correo_emisor, lista_correos, msg.as_string())
        servidor.quit()
        print("Correo de bienvenida enviado exitosamente.")
    except Exception as e:
        print("Error al enviar el correo:", e)

# Obtener correos de los profesores desde la base de datos
correos_profesores = obtener_correos_profesores()

# Ejemplo de uso con los correos obtenidos de la base de datos
enviar_correo_bienvenida(
    correos_profesores,
    'Nombre del Profesor',
    'Curso XYZ - Sección A',
    'Estudiante 1, Estudiante 2, Estudiante 3',
    'Sesión 1: Fecha y hora, Sesión 2: Fecha y hora',
    'Evaluación 1: Fecha y hora, Evaluación 2: Fecha y hora'
)
