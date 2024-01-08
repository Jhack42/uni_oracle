import cx_Oracle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def obtener_info_profesores():
    conexion = cx_Oracle.connect('db_curso/curso123@localhost:1521/orcl')  # Ajusta según tu configuración
    cursor = conexion.cursor()

    consulta = """
    SELECT 
        p.id_profesor, p.nombres, p.apellidos, p.correo_electronico,
        c.nombre_curso, c.descripcion as descripcion_curso,
        ec.fecha_inicio, ec.duracion_minutos, ec.descripcion as descripcion_sesion,
        ev.nombre_evaluacion, ev.fecha_evaluacion as fecha_evaluacion_evaluacion
    FROM 
        Profesores p
    INNER JOIN 
        Cursos c ON p.id_profesor = c.id_profesor
    LEFT JOIN 
        Sesiones_Curso ec ON c.id_curso = ec.id_curso
    LEFT JOIN 
        Evaluaciones ev ON c.id_curso = ev.id_curso
    """
    cursor.execute(consulta)
    resultados = cursor.fetchall()

    conexion.close()
    return resultados

def enviar_correo_bienvenida():
    correo_emisor = 'tu_correo@example.com'  # Cambiar por tu correo
    servidor_smtp = 'smtp.office365.com'
    puerto_smtp = 587

    info_profesores = obtener_info_profesores()

    if info_profesores:
        for info_profesor in info_profesores:
            (
                id_profesor, nombre_profesor, apellido_profesor, correo_profesor,
                nombre_curso, descripcion_curso, fecha_sesion, duracion_sesion, descripcion_sesion,
                nombre_evaluacion, fecha_evaluacion
            ) = info_profesor

            mensaje = f"Bienvenido {nombre_profesor} {apellido_profesor} al ciclo 2022-1\n\nCurso: {nombre_curso}\nDescripción del curso: {descripcion_curso}\n\n"
            if fecha_sesion:
                mensaje += f"Sesión: {fecha_sesion}, Duración: {duracion_sesion} minutos\nDescripción de la sesión: {descripcion_sesion}\n\n"
            if nombre_evaluacion:
                mensaje += f"Próxima evaluación: {nombre_evaluacion}, Fecha: {fecha_evaluacion}\n"

            msg = MIMEMultipart()
            msg['From'] = correo_emisor
            msg['To'] = correo_profesor
            msg['Subject'] = 'Bienvenida al ciclo 2022-1'
            msg.attach(MIMEText(mensaje, 'plain'))

            try:
                with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
                    servidor.starttls()
                    servidor.login(correo_emisor, input("Contraseña: "))  # Solicitar contraseña de manera segura
                    servidor.send_message(msg)
                print(f"Correo de bienvenida enviado exitosamente a {correo_profesor}.")
            except Exception as e:
                print(f"Error al enviar el correo a {correo_profesor}: {e}")

enviar_correo_bienvenida()
