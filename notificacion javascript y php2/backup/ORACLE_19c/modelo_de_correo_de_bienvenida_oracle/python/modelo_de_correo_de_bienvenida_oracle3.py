import cx_Oracle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def obtener_info_profesores():
    # Conexión a la base de datos Oracle
    try:
        conexion = cx_Oracle.connect('db_curso/curso123@localhost:1521/orcl')  # Ajusta según tu configuración
        cursor = conexion.cursor()

        # Obtener información de profesores
        cursor.execute("SELECT id_profesor, nombres, apellidos, correo_electronico FROM Profesores")
        resultados = cursor.fetchall()

        conexion.close()
        return resultados
    except cx_Oracle.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return []

def enviar_correo_bienvenida():
    # Configuración de parámetros para enviar correos
    correo_emisor = '1364822@senati.pe'  # Cambiar por tu correo
    contraseña_emisor = 'JC221101f'  # Cambiar por tu contraseña
    servidor_smtp = 'smtp.office365.com'
    puerto_smtp = 587

    info_profesores = obtener_info_profesores()

    if info_profesores:
        for info_profesor in info_profesores:
            # Detalles del profesor y el mensaje de bienvenida
            id_profesor, nombre_profesor, apellido_profesor, correo_profesor = info_profesor
            curso_seccion = f'Curso XYZ - Sección {id_profesor}'  # Ajustar según la información del profesor
            listado_estudiantes = 'Estudiante 1, Estudiante 2, Estudiante 3'  # Agregar estudiantes
            listado_sesiones = 'Sesión 1: Fecha y hora, Sesión 2: Fecha y hora'  # Agregar sesiones
            listado_evaluaciones = 'Evaluación 1: Fecha y hora, Evaluación 2: Fecha y hora'  # Agregar evaluaciones

            mensaje = (
                f"Bienvenido {nombre_profesor} {apellido_profesor} al ciclo 2022-1\n\n"
                f"{curso_seccion}\n\nListado de estudiantes:\n{listado_estudiantes}\n\n"
                f"Donde cargar su material\n\nListado de sesiones, fecha y hora:\n{listado_sesiones}\n\n"
                f"Listado de evaluaciones, fecha y hora, cargar sus evaluaciones:\n{listado_evaluaciones}"
            )

            # Crear mensaje y enviar correo
            msg = MIMEMultipart()
            msg['From'] = correo_emisor
            msg['To'] = correo_profesor
            msg['Subject'] = 'Bienvenida al ciclo 2022-1'
            msg.attach(MIMEText(mensaje, 'plain'))

            try:
                # Enviar correo
                with smtplib.SMTP(servidor_smtp, puerto_smtp) as servidor:
                    servidor.starttls()
                    servidor.login(correo_emisor, contraseña_emisor)
                    servidor.sendmail(correo_emisor, correo_profesor, msg.as_string())
                print(f"Correo de bienvenida enviado exitosamente a {correo_profesor}.")
            except Exception as e:
                print("Error al enviar el correo:", e)

if __name__ == "__main__":
    enviar_correo_bienvenida()

