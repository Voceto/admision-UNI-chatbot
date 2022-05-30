import mysql
import mysql.connector

contexto_tot="""La tasa de selectividad o admisión es de un ingresante por cada nueve postulantes. 
La Oficina de Central de Admisión (OCAD) inició sus actividades en 1980. 
La Universidad Nacional de Ingeniería es una universidad pública peruana.
La Universidad Nacional de Ingeniería es conocida también por sus siglas: UNI.
La OCAD se encarga de organizar, ejecutar y evaluar el proceso de ingreso a la Universidad, asegurando la incorporación de alumnos por sus méritos, que tengan las capacidades requeridas para seguir estudios universitarios.
El proceso automático de calificación de los exámenes se lleva a cabo en el Centro de Cómputo de la Oficina de Admisión bajo la supervisión de las autoridades de la universidad.
Las modalidades de admisión a la UNI son ordinario y extraordinario.
La carrera más demandada es Ingeniería Civil.
El proceso de admisión consta de tres exámenes que evalúan matemáticas, letras y física y química, cada examen dura tres horas.
El examen de admisión consta de tres partes que son evaluadas en tres fechas (lunes, miércoles y viernes) y tienen una duración de tres horas cada una.
Son 10 modalidades extraordinarias.
Las inscripciones al proceso de Admisión 2022-2 comienzan el 06 de junio y terminan el 30 de julio del 2022.
El prospecto cuesta S/ 90.00. El pago para dar o rendir el examen es de S/ 410.00.
Los pagos se realizarán en el banco BCP, agentes BCP o banca por internet BCP.
Los telefonos para consultas son 981609170, 981600816, 981606955 y 981607508.
El correo para informes es informes@admisionuni.edu.pe.
El correo para quejas es quejas@admisionuni.edu.pe.
La UNI ofrece 29 especialidades dentro de sus 11 facultades.
Se puede postular varias veces a la UNI, no hay límites para postular.
La UNI queda en Av. Tupac Amaru 210 Rímac.
El orden de mérito en cada Especialidad se determina mediante la nota final que obtenga el postulante.
El puntaje máximo del examen de letras es de 745 puntos.
El puntaje máximo del examen de matemáticas es de 600 puntos.
El puntaje máximo del examen de física y química es de 500 puntos.
El puntaje máximo de los tres examenes es de 1845.
El puntaje mínimo para ingresar es 11.
Los resultados se publican en la página de la OCAD.
El Concurso de Admisión consiste en la evaluación de conocimientos, aptitudes, intereses vocacionales y la formación integral de los postulantes.
La UNI ofrece en total 1106 vacantes.
Los postulantes del examen de admision 2022-I, cuya cantidad exacta es de 5293, compitieron por una de las 1.388 vacantes (ingreso ordinario y extraordinario) de las 28 especialidades que ofrece la UNI.
1225 fueron mujeres y 4068 fueron varones en el examen de admision 2022-I.
El horario de atención es de Lunes a Viernes de 9:00 a.m. a 6:00 p.m.
El examen de admisión 2022-2 abarca los días 15, 17 y 19 de agosto.
En Arquitectura hay 52 vacantes, la tasa de ingreso es del 5.04%, a su vez, en Arquitectura, la nota mínima para ingresar es de 13.049.
En Física hay 27 vacantes, la tasa de ingreso es del 2.65%, a su vez, en Física, la nota mínima para ingresar es de 11.874.
En Matemática hay 23 vacantes, la tasa de ingreso es del 1.06%, a su vez, en Matemática, la nota mínima para ingresar es de 11.002.
En Química hay 23 vacantes, la tasa de ingreso es del 0.53%, a su vez, en Química, la nota mínima para ingresar es de 11.124.
En Ingeniería Física hay 34 vacantes, la tasa de ingreso es del 1.86%, a su vez, en Ingeniería Física, conocida como Ing. Física, la nota mínima para ingresar es de 11.423.
En Ciencia de la Computación hay 27 vacantes, la tasa de ingreso es del 2.92%, a su vez, en Ciencia de la Computación, la nota mínima para ingresar es de 11.971.
En Ingeniería Sanitaria hay 34 vacantes, la tasa de ingreso es del 1.99%, a su vez, en Ingeniería Sanitaria, conocida como Ing. Sanitaria, la nota mínima para ingresar es de 11.618.
En Ingeniería de Higiene y Seg. Industrial hay 33 vacantes, la tasa de ingreso es del 1.86%, a su vez, en Ingeniería de Higiene y Seg. Industrial, conocida como Ing. de Higiene y Seg. Industrial, la nota mínima para ingresar es de 11.311.
En Ingeniería Ambiental hay 33 vacantes, la tasa de ingreso es del 3.58%, a su vez, en Ingeniería Ambiental, conocida como Ing. Ambiental, la nota mínima para ingresar es de 11.821.
En Ingeniería Civil hay 128 vacantes, la tasa de ingreso es del 15.52%, a su vez, en Ingeniería Civil, conocida como Ing. Civil, la nota mínima para ingresar es de 13.805.
En Ingeniería Económica hay 44 vacantes, la tasa de ingreso es del 4.77%, a su vez, en Ingeniería Económica, conocida como Ing. Económica, la nota mínima para ingresar es de 11.343.
En Ingeniería Estadística hay 37 vacantes, la tasa de ingreso es del 1.19%, a su vez, en Ingeniería Estadística, conocida como Ing. Estadística, la nota mínima para ingresar es de 11.103.
En Ingeniería Eléctrica hay 29 vacantes, la tasa de ingreso es del 3.58%, a su vez, en Ingeniería Eléctrica, conocida como Ing. Eléctrica, la nota mínima para ingresar es de 13.293.
En Ingeniería Electrónica hay 30 vacantes, la tasa de ingreso es del 3.58%, a su vez, en Ingeniería Electrónica, conocida como Ing. Electrónica, la nota mínima para ingresar es de 13.513.
En Ingeniería de Telecomunicaciones hay 29 vacantes, la tasa de ingreso es del 3.58%, a su vez, en Ingeniería de Telecomunicaciones, conocida como Ing. de Telecomunicaciones, la nota mínima para ingresar es de 13.25.
En Ingeniería de Ciberseguridad hay 29 vacantes, conocida como Ing. de Ciberseguridad.
En Ingeniería Geológica hay 21 vacantes, la tasa de ingreso es del 3.05%, a su vez, en Ingeniería Geológica, conocida como Ing. Geológica, la nota mínima para ingresar es de 12.44.
En Ingeniería Metalúrgica hay 30 vacantes, la tasa de ingreso es del 3.98%, a su vez, en Ingeniería Metalúrgica, conocida como Ing. Metalúrgica, la nota mínima para ingresar es de 12.256.
En Ingeniería de Minas hay 27 vacantes, la tasa de ingreso es del 3.32%, a su vez, en Ingeniería de Minas, conocida como Ing. de Minas, la nota mínima para ingresar es de 12.65.
En Ingeniería Industrial hay 80 vacantes, la tasa de ingreso es del 8.36%, a su vez, en Ingeniería Industrial, conocida como Ing. Industrial, la nota mínima para ingresar es de 13.425.
En Ingeniería de Sistemas hay 81 vacantes, la tasa de ingreso es del 8.36%, a su vez, en Ingeniería de Sistemas, conocida como Ing. de Sistemas, la nota mínima para ingresar es de 13.469.
En Ingeniería Mecánica hay 34 vacantes, la tasa de ingreso es del 3.85%, a su vez, en Ingeniería Mecánica, conocida como Ing. Mecánica, la nota mínima para ingresar es de 13.937.
En Ingeniería Mecánica Eléctrica hay 33 vacantes, la tasa de ingreso es del 3.45%, a su vez, en Ingeniería Mecánica Eléctrica, conocida como Ing. Mecánica Eléctrica, la nota mínima para ingresar es de 13.794.
En Ingeniería Naval hay 23 vacantes, la tasa de ingreso es del 2.12%, a su vez, en Ingeniería Naval, conocida como Ing. Naval, la nota mínima para ingresar es de 13.325.
En Ingeniería Mecatrónica hay 33 vacantes, la tasa de ingreso es del 3.58%, a su vez, en Ingeniería Mecatrónica, conocida como Ing. Mecatrónica, la nota mínima para ingresar es de 14.329.
En Ingeniería Petroquímica hay 13 vacantes, la tasa de ingreso es del 1.19%, a su vez, en Ingeniería Petroquímica, conocida como Ing. Petroquímica, la nota mínima para ingresar es de 11.125.
En Ingeniería de Petroleo y Gas Natural hay 13 vacantes, la tasa de ingreso es del 0.66%, a su vez, en Ingeniería de Petroleo y Gas Natural, conocida como Ing. de Petroleo y Gas Natural, la nota mínima para ingresar es de 11.04.
En Ingeniería Química hay 54 vacantes, la tasa de ingreso es del 3.58%, a su vez, en Ingeniería Química, conocida como Ing. Química, la nota mínima para ingresar es de 12.043.
En Ingeniería Textil hay 34 vacantes, la tasa de ingreso es del 0.8%, a su vez, en Ingeniería Textil, conocida como Ing. Textil, la nota mínima para ingresar es de 11.394.
La Facultad de Arquitectura Urbanismo y Arte, también conocida como FAUA, está conformada por la carrera de Arquitectura.
La Facultad de Ciencias, también conocida como FC, está conformada por las carreras de Física, Matemática, Química, Ingeniería Física y Ciencia de la Computación.
La Facultad de Ingeniería Ambiental, también conocida como FIA, está conformada por las carreras de: Ingeniería Sanitaria, Ingeniería de Higiene y Seg. Industrial e Ingeniería Ambiental.
La Facultad de Ingeniería Civil, también conocida como FIC, está conformada por las carrera de Ingeniería Civil.
La Facultad de Ingeniería Económica, Estadística y Ciencias Sociales, también conocida como FIEECS, está conformada por las carreras de Ingeniería Económica e Ingeniería Estadística.
La Facultad de Ingeniería Eléctrica y Electrónica, también conocida como FIEE, está conformada por las carreras de Ingeniería Electrónica e Ingeniería de Telecomunicaciones.
La Facultad de Ingeniería Geológica Minera y Metalurgia, también conocida como FIGMM, está conformada por las carreras de Ingeniería Geológica, Ingeniería Metalúrgica e Ingeniería de Minas.
La Facultad de Ingeniería Industrial y Sistemas, también conocida como FIIS, está conformada por las carreras de Ingeniería Industrial e Ingeniería de Sistemas.
La Facultad de Ingeniería Mecánica, también conocida como FIM, está conformada por las carreras de Ingeniería Mecánica, Ingeniería Mecánica Eléctrica, Ingeniería Naval e Ingeniería Mecatrónica.
La Facultad de Ingeniería de Petroleo Gas Natural y Petroquímica, también conocida como FIP, está conformada por las carreras de Ingeniería Petroquímica e Ingeniería de Petroleo y Gas Natural.
La Facultad de Ingeniería Química y Textíl, también conocida como FIQT, está conformada por las carreras de Ingeniería Química e Ingeniería Textil.
"""
def conexion(conexion_switch = 1):
    import mysql
    import mysql.connector
    if conexion_switch == 1:
        cnx = mysql.connector.connect(user='sql10496327', password='yBzj62dSxP',
                                  host='sql10.freesqldatabase.com',
                                  database='sql10496327')
    elif conexion_switch == 2:
        cnx = mysql.connector.connect(user='chatbot_app', password='analitica_datos_UNI_E12',
                                  host='127.0.0.1',
                                  database='chatbot_admision')
    return cnx


# Insertar contexto en la BD
def inserta_contexto(contexto, conexion_switch=1):
    cnx = conexion(conexion_switch)
    cursor = cnx.cursor()
    # Borrando datos previos en la tabla
    #cursor.execute("TRUNCATE TABLE hechos")

    # Creando lista de tuplas para bulk insert
    hechos = contexto.split("\n")
    value_data = []
    for i, j in enumerate(hechos):
        value_data.append((i, j))

    add_data = ("INSERT INTO hechos "
                "(id, hecho)"
                "VALUES (%s, %s)")
    cursor.executemany(add_data, value_data)
    print(f"{cursor.rowcount} registros insertados")

    cnx.commit()
    # cnx.rollback()
    cursor.close()
    cnx.close()
    

def run():
    inserta_contexto(contexto_tot)
if __name__ == "__main__":
    run()