import cx_Oracle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Función para obtener información de profesores desde la base de datos Oracle
def obtener_info_profesores():
    try:
        conexion = cx_Oracle.connect('db_curso/curso123@localhost:1521/orcl')
        cursor = conexion.cursor()
        cursor.execute("SELECT id_profesor, nombres, apellidos, correo_electronico FROM Profesores")
        resultados = cursor.fetchall()
        conexion.close()
        return resultados
    except cx_Oracle.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return []

# Función para enviar correos de bienvenida a los profesores
def enviar_correo_bienvenida():
    correo_emisor = '1364822@senati.pe'
    contraseña_emisor = 'JC221101f'
    servidor_smtp = 'smtp.office365.com'
    puerto_smtp = 587

    info_profesores = obtener_info_profesores()

    if info_profesores:
        for info_profesor in info_profesores:
            id_profesor, nombre_profesor, apellido_profesor, correo_profesor = info_profesor
            curso_seccion = f'Curso XYZ - Sección {id_profesor}'  # Ajustar según la información del profesor
            listado_estudiantes = 'Estudiante 1, Estudiante 2, Estudiante 3'  # Agregar estudiantes
            listado_sesiones = 'Sesión 1: Fecha y hora, Sesión 2: Fecha y hora'  # Agregar sesiones
            listado_evaluaciones = 'Evaluación 1: Fecha y hora, Evaluación 2: Fecha y hora'  # Agregar evaluaciones

            # Construir el mensaje personalizado para cada profesor con HTML y CSS
            mensaje = f"""
            <html>
            <head>
            <style>
                /* Estilos CSS para el diseño del mensaje */
                .container {{
                    font-family: Arial, sans-serif;
                    background-color: #ffffff;
                    padding: 20px;
                    width: 100%;
                    max-width: 600px;
                    margin: 20px auto;
                    border: 2px solid maroon;
                    border-radius: 10px;
                    text-align: center;
                }}
                /*------------encabezado-------------*/
                .encabezado {{
                    background-color: rgb(230, 217, 170);
                    padding: 10px;
                    display: flex;
                    text-align: center;
                    font-weight: bold;
                    font-size: 24px;
                    margin-bottom: 20px;
                    border-radius: 10px;
                    text-align: left; /* Alineación a la izquierda */
                }}
                .texto-uni-orce {{
                    font-size: 48px;
                    font-weight: bold;
                    text-transform: uppercase;
                    margin-right: 20px;
                    color: #711610
                }}
                /* Estilos para la imagen dentro del encabezado */
                .header .img-container {{
                    float: right; /* Alineación a la derecha */
                    margin-left: 10px; /* Espaciado entre la imagen y el texto */
                }}
                
                .imagen {{
                    max-width: 100px;
                    /* Ajusta el tamaño de la imagen según sea necesario */
                }}
                /*------------content-------------*/
                .content {{
                    background-color: white;
                    padding: 20px;
                    color: #711610
                }}
                <!--------------pie_de_página--------------->
                <div class="pie_de_página">
                    <!--------------direccion--------------->
                    <div class="text_direccion" style="display: inline-block;">
                        <p>Contacto</p>
                        <p>Av. Túpac Amaru 210 - Rímac.</p>
                        <p>Apartado 1301. Lima - Perú</p>
                        <p>Telf.: 4811070</p>
                    </div>
                    <!--------------text--------------->
                    <div class="text" style="display: inline-block;">
                        <p style="text-align: center;">2022 © Derechos Reservados</p>
                    </div>
                </div>
            </style>
            </head>
            <body>
                <div class="container">
                    <!--------------encabezado--------------->
                    <div class="encabezado" >
                        <div class="texto-uni-orce" style="display: inline-block;">
                            UNI<br>ORCE
                        </div>
                        <div class="img-container" style="display: inline-block;">
                            <img class="imagen" src="imajenes/imagen1.png">
                        </div>
                    </div>
                    <!--------------contenido--------------->
                    <div class="content">
                        <p>Bienvenido {nombre_profesor} {apellido_profesor}</p>
                        <p>al ciclo 2022-1</p>
                        <ul>
                            <p>Curso: Curso XYZ - Sección {id_profesor}</p>
                            <p>{curso_seccion}</p>
                            <p>Listado de estudiantes:{listado_estudiantes}</p>
                            <p>Donde cargar su material</p>
                            <p>Listado de sesiones, fecha y hora:</p>
                            <p>{listado_sesiones}</p>
                            <p>Listado de evaluaciones, fecha y hora, cargar sus evaluaciones:</p>
                            <p>{listado_evaluaciones}</p>
                        </ul>
                        <p>¡Esperamos un excelente ciclo!</p>
                    </div>
                    <!--------------pie_de_página--------------->
                    <div class="pie_de_página">
                        <!--------------direccion--------------->
                        <div class="text_direccion" style="display: block; text-align: right;>
                            <p style="text-align: left;">Contacto</p>
                            <p style="text-align: left;">Av. Túpac Amaru 210 - Rímac.</p>
                            <p style="text-align: left;">Apartado 1301. Lima - Perú</p>
                            <p style="text-align: left;">Telf.: 4811070</p>
                        </div>
                        <!--------------text--------------->
                        <div class="text" style="display: block; text-align: center;">
                            <p>2022 © Derechos Reservados</p>
                        </div>
                    </div>
                </div>
            </body>
            </html>
            """

            # Crear mensaje y enviar correo
            msg = MIMEMultipart()
            msg['From'] = correo_emisor
            msg['To'] = correo_profesor
            msg['Subject'] = 'Bienvenida al ciclo 2022-1'
            msg.attach(MIMEText(mensaje, 'html'))

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
