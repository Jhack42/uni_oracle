import cx_Oracle
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(asunto, mensaje, destinatario, remitente, contraseña):
    print(f"Enviando correo a: {destinatario}")
    # Configuración del correo electrónico
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto
    msg.attach(MIMEText(mensaje, 'plain'))

    # Configuración del servidor SMTP
    servidor_smtp = 'smtp-mail.outlook.com'
    puerto = 587

    try:
        with smtplib.SMTP(servidor_smtp, puerto) as server:
            server.starttls()
            server.login(remitente, contraseña)
            server.sendmail(remitente, destinatario, msg.as_string())
            print("Correo enviado exitosamente")
    except smtplib.SMTPAuthenticationError as auth_error:
        print(f"Error de autenticación SMTP: {auth_error}")
    except smtplib.SMTPException as smtp_error:
        print(f"Error SMTP general: {smtp_error}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

def obtener_correos(remitente, contraseña):
    print("Conectando a la base de datos...")
    # Conexión a la base de datos Oracle
    conexion = cx_Oracle.connect('db_curso/curso123@localhost:1521/orcl')

    # Crear un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT email FROM usuarios")

        for row in cursor:
            correo_destino = row[0]
            asunto = 'Asunto del correo'
            mensaje = 'Hola, esto es una prueba de correo desde Python.'
            enviar_correo(asunto, mensaje, correo_destino, remitente, contraseña)
    except cx_Oracle.Error as error:
        print(f"Error en la consulta: {error}")
    finally:
        cursor.close()
        conexion.close()

remitente = '1364822@senati.pe'
contraseña = 'JC221101f'

obtener_correos(remitente, contraseña)