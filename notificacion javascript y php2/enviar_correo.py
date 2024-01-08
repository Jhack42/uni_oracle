import cx_Oracle
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo(asunto, mensaje, destinatario, remitente, contraseña):
    try:
        msg = MIMEMultipart()
        msg['From'] = remitente
        msg['To'] = destinatario
        msg['Subject'] = asunto
        msg.attach(MIMEText(mensaje, 'plain'))

        servidor_smtp = 'smtp-mail.outlook.com'
        puerto = 587

        with smtplib.SMTP(servidor_smtp, puerto) as server:
            server.starttls()
            server.login(remitente, contraseña)
            server.sendmail(remitente, destinatario, msg.as_string())
            print(f"Correo enviado a {destinatario} exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo a {destinatario}: {e}")

def obtener_correos(remitente, contraseña):
    try:
        print("Conectando a la base de datos...")
        conexion = cx_Oracle.connect('db_curso/curso123@localhost:1521/orcl')
        print("Conexión exitosa")

        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT email FROM usuarios")
            print("Consulta ejecutada correctamente")

            for row in cursor:
                correo_destino = row[0]
                enviar_correo('Asunto del correo', 'Mensaje de prueba', correo_destino, remitente, contraseña)

            print("Todos los correos enviados")
        except cx_Oracle.Error as error:
            print(f"Error en la consulta: {error}")
        finally:
            cursor.close()
            conexion.close()
    except cx_Oracle.Error as error_db:
        print(f"Error de conexión a la base de datos: {error_db}")

remitente = '1364822@senati.pe'
contraseña = 'JC221101f'

obtener_correos(remitente, contraseña)
